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
    print("│ [2] 开启路由转发                                                   │")
    print("│ [3] 关闭路由转发                                                   │")
    print("│ [4] 捕获数据                                                       │")
    print("│ [5] 查看帮助(ip/mac获取方法)                                       │")
    print("└" + "─" * 68 + "┘")
    print("=" * 70)
    print(" " * 20 + "注意: 请以管理员身份运行本脚本" + " " * 20)
    print("=" * 70)
    print("")


if __name__ == "__main__":
    UIout()
    while True:
        a = 1
