import subprocess

def restart_router_windows():
    """重启 Windows 上的路由服务"""
    subprocess.run(['sc', 'stop', 'RemoteAccess'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    subprocess.run(['sc', 'start', 'RemoteAccess'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print("Router restarted on Windows.")

def enable_ip_routing_windows():
    """启用 Windows 上的 IP 路由"""
    subprocess.run(['reg', 'add', r"HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters", '/v', 'IPEnableRouter', '/t', 'REG_DWORD', '/d', '1', '/f'], check=True)
    restart_router_windows()
    print("IP routing enabled on Windows.")

def disable_ip_routing_windows():
    """禁用 Windows 上的 IP 路由"""
    subprocess.run(['reg', 'add', r"HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters", '/v', 'IPEnableRouter', '/t', 'REG_DWORD', '/d', '0', '/f'], check=True)
    restart_router_windows()
    print("IP routing disabled on Windows.")

def restart_router_linux():
    """重启 Linux 上的路由服务"""
    subprocess.run(['systemctl', 'restart', 'networking'], check=True)
    print("Router restarted on Linux.")

def enable_ip_routing_linux():
    """启用 Linux 上的 IP 路由"""
    # 临时启用 IP 转发
    subprocess.run(['echo', '1', '>', '/proc/sys/net/ipv4/ip_forward'], shell=True, check=True)
    # 永久启用 IP 转发
    subprocess.run(['sh', '-c', 'echo "net.ipv4.ip_forward = 1" >> /etc/sysctl.conf'], check=True)
    # 使配置生效
    subprocess.run(['sysctl', '-p'], check=True)
    restart_router_linux()
    print("IP routing enabled on Linux.")

def disable_ip_routing_linux():
    """禁用 Linux 上的 IP 路由"""
    # 临时禁用 IP 转发
    subprocess.run(['echo', '0', '>', '/proc/sys/net/ipv4/ip_forward'], shell=True, check=True)
    # 永久禁用 IP 转发
    subprocess.run(['sh', '-c', 'sed -i "s/net.ipv4.ip_forward = 1/net.ipv4.ip_forward = 0/" /etc/sysctl.conf'], check=True)
    # 使配置生效
    subprocess.run(['sysctl', '-p'], check=True)
    restart_router_linux()
    print("IP routing disabled on Linux.")

if __name__ == "__main__":
    enable_ip_routing_windows()
