import subprocess
import platform

def clear_screen():
    cmd = "cls" if platform.system() == "Windows" else "clear"
    subprocess.call(cmd, shell=True)

def UIout():
    clear_screen()
    print("=" * 70)
    print(" " * 25 + "【ARP安全测试工具】" + " " * 25)
    print("=" * 70)
    print("┌" + "─" * 68 + "┐")
    print("│ [1] 断网攻击                                                       │")
    print("│ [2] 开启路由                                                       │")
    print("│ [3] 关闭路由                                                       │")
    print("│ [4] 捕获数据包                                                     │")
    print("│ [5] 使用帮助                                                       │")
    #print("│ [5] 扫描局域网设备                                                 │")
    #print("│ [0] 退出程序                                                       │")
    print("└" + "─" * 68 + "┘")
    print("=" * 70)
    print("注意: 请以管理员身份运行本脚本")
    print("=" * 70)
    print("")


if __name__ == "__main__":
    UIout()
    while True:
        a = 1
