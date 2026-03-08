from fastapi import FastAPI

app = FastAPI()

LATEST_VERSION = "1.2.3"
DOWNLOAD_URL = "https://appgallery.huawei.com/link/invite-xxx"

def parse_version(v: str) -> tuple:
    return tuple(map(int, v.split(".")))

def compare_version(current: str, latest: str) -> bool:
    return parse_version(current) < parse_version(latest)

@app.get("/check")
async def check_update(current: str = "1.0.0"):
    need_update = compare_version(current, LATEST_VERSION)
    
    return {
        "latest": LATEST_VERSION,
        "current": current,
        "need_update": need_update,
        "url": DOWNLOAD_URL if need_update else None,
        "changelog": "修复已知问题，优化用户体验" if need_update else None
    }
