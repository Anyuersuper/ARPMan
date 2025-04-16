import platform
import subprocess

def restart_router_windows():
    subprocess.run(['sc', 'stop', 'RemoteAccess'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    subprocess.run(['sc', 'start', 'RemoteAccess'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print("✅ Windows 路由服务已重启")

def enable_ip_routing_windows():
    subprocess.run(['reg', 'add', r"HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters",
                    '/v', 'IPEnableRouter', '/t', 'REG_DWORD', '/d', '1', '/f'], check=True)
    restart_router_windows()
    print("✅ Windows IP 路由已启用")

def disable_ip_routing_windows():
    subprocess.run(['reg', 'add', r"HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters",
                    '/v', 'IPEnableRouter', '/t', 'REG_DWORD', '/d', '0', '/f'], check=True)
    restart_router_windows()
    print("✅ Windows IP 路由已禁用")

def enable_ip_routing_termux():
    subprocess.run(['su', '-c', 'echo 1 > /proc/sys/net/ipv4/ip_forward'], shell=True)
    print("✅ Termux IP 路由已启用")

def disable_ip_routing_termux():
    subprocess.run(['su', '-c', 'echo 0 > /proc/sys/net/ipv4/ip_forward'], shell=True)
    print("✅ Termux IP 路由已禁用")

def enable_ip_routing_linux():
    subprocess.run(['sh', '-c', 'echo 1 > /proc/sys/net/ipv4/ip_forward'], check=True)
    subprocess.run(['sh', '-c', 'echo "net.ipv4.ip_forward = 1" >> /etc/sysctl.conf'], check=True)
    subprocess.run(['sysctl', '-p'], check=True)
    print("✅ Linux IP 路由已启用")

def disable_ip_routing_linux():
    subprocess.run(['sh', '-c', 'echo 0 > /proc/sys/net/ipv4/ip_forward'], check=True)
    subprocess.run(['sh', '-c', 'sed -i "s/net.ipv4.ip_forward = 1/net.ipv4.ip_forward = 0/" /etc/sysctl.conf'], check=True)
    subprocess.run(['sysctl', '-p'], check=True)
    print("✅ Linux IP 路由已禁用")

def detect_and_enable_routing():
    system = platform.system()
    if system == "Windows":
        enable_ip_routing_windows()
    elif system == "Linux":
        try:
            with open("/proc/version") as f:
                if "Android" in f.read():
                    enable_ip_routing_termux()
                else:
                    enable_ip_routing_linux()
        except Exception as e:
            print(f"检测失败: {e}")
    else:
        print("❌ 不支持的平台")

def detect_and_disable_routing():
    system = platform.system()
    if system == "Windows":
        disable_ip_routing_windows()
    elif system == "Linux":
        try:
            with open("/proc/version") as f:
                if "Android" in f.read():
                    disable_ip_routing_termux()
                else:
                    disable_ip_routing_linux()
        except Exception as e:
            print(f"检测失败: {e}")
    else:
        print("❌ 不支持的平台")


if __name__ == "__main__":
    detect_and_enable_routing()
