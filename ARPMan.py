import platform
from UIout import UIout
from Attack import Disconnect
from Route import disable_ip_routing_linux, disable_ip_routing_windows, enable_ip_routing_linux, enable_ip_routing_windows 


def DisconnectTarget():
    target_ip = input("请输入目标IP:")
    target_mac = input("请输入目标MAC:")
    gateway_ip = input("请输入网关IP:")
    gateway_mac = input("请输入网关MAC:")
    fake_mac = input("请输入伪造的MAC:")
    timebreak = 0
    Disconnect(target_ip, target_mac, gateway_ip, gateway_mac, fake_mac, timebreak)

def OpenRoute():
    print("开启/关闭路由请以管理员的身份运行脚本")
    if platform.system() == "Windows":
        enable_ip_routing_windows()
    elif platform.system() == "Linux":
        enable_ip_routing_linux()

def CloseRoute():
    print("开启/关闭路由请以管理员的身份运行脚本")
    if platform.system() == "Windows":
        disable_ip_routing_windows()
    elif platform.system() == "Linux":
        disable_ip_routing_linux()

def CapturePacket():
    print("3")



if __name__ == "__main__":
    UIout()
    while True:
        ret = input("请输入指令:")
        if ret == "1":
            DisconnectTarget()
        elif ret == "2":
            OpenRoute()
        elif ret == "3":
            CloseRoute()
        elif ret == "4":
            CapturePacket()
        elif ret == "5":
            UIout()
    
