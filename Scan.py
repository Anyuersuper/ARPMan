import subprocess
import platform
import re

def get_arp_table():
    system = platform.system()

    if system == "Windows":
        cmd = ["arp", "-a"]
    elif system == "Linux":
        cmd = ["ip", "neigh"]
    else:
        raise Exception(f"不支持的系统: {system}")

    try:
        if system == "Windows":
            # Windows 系统使用 GBK 编码
            output = subprocess.check_output(cmd, encoding='gbk')
        else:
            output = subprocess.check_output(cmd, encoding='utf-8')
        return output
    except Exception as e:
        print("命令执行失败:", e)
        return ""

def parse_arp_table(raw_output):
    ip_mac_list = []

    # Windows 格式
    win_pattern = re.compile(r"(\d+\.\d+\.\d+\.\d+)\s+([-\w]+)\s+(dynamic|static)")

    # Linux (ip neigh)
    linux_pattern = re.compile(r"(\d+\.\d+\.\d+\.\d+)\s+dev\s+\w+\s+lladdr\s+([\da-fA-F:]+)")

    for line in raw_output.splitlines():
        line = line.strip()

        # Windows
        if '-' in line and '.' in line:
            match = win_pattern.search(line)
            if match:
                ip, mac, _ = match.groups()
                ip_mac_list.append((ip, mac))

        # Linux
        elif 'lladdr' in line:
            match = linux_pattern.search(line)
            if match:
                ip, mac = match.groups()
                ip_mac_list.append((ip, mac))

    return ip_mac_list

if __name__ == "__main__":
    print("[*] 获取 ARP 表...")
    output = get_arp_table()
    devices = parse_arp_table(output)

    print("\n扫描结果：")
    for ip, mac in devices:
        print(f"{ip} - {mac}")
