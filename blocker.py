import platform
import sys

REDIRECT_IP = "127.0.0.1"


def hosts_path():
    if platform.system() == "Windows":
        return r"C:\Windows\System32\drivers\etc\hosts"
    return "/etc/hosts"


def block(site):
    with open(hosts_path(), "a") as f:
        f.write(f"\n{REDIRECT_IP} {site}\n{REDIRECT_IP} www.{site}\n")
    print("Blocked:", site)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python blocker.py youtube.com")
    else:
        block(sys.argv[1])