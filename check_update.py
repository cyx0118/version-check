import requests

SERVER_URL = "http://IP:8000/check"
CURRENT_VERSION = "1.0.0"

def check_update():
    try:
        resp = requests.get(
            SERVER_URL,
            params={"current": CURRENT_VERSION},
            timeout=5
        )
        data = resp.json()
        
        if data["need_update"]:
            print(f"发现新版本: {data['latest']} (当前: {data['current']})")
            print(f"更新内容: {data['changelog']}")
            print(f"下载地址: {data['url']}")
        else:
            print(f"已是最新版本 {data['current']}")
            
        return data
        
    except Exception as e:
        print(f"检查更新失败: {e}")
        return None

if __name__ == "__main__":
    check_update()
