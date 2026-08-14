# -*- coding: utf-8 -*-
import urllib.request, json, subprocess, os, sys, time

TOKEN = open("../csg_token.txt").read().strip()
OWNER = "hxj0515"
REPO = "csg-power-hub"
API = "https://api.github.com"
HUB = f"https://{OWNER}.github.io/{REPO}/"
HEAD = {"Authorization": "token " + TOKEN, "Accept": "application/vnd.github+json", "User-Agent": "hub-builder"}


def api(method, path, data=None):
    req = urllib.request.Request(API + path, data=(json.dumps(data).encode() if data else None),
                                 headers=HEAD, method=method)
    try:
        r = urllib.request.urlopen(req)
        return r.status, r.read().decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode("utf-8", "replace")


# 1) 仓库已存在则跳过创建
st, _ = api("GET", f"/repos/{OWNER}/{REPO}")
if st == 200:
    print("repo exists, skip create")
else:
    st, body = api("POST", "/user/repos", {
        "name": REPO,
        "description": "南方电网动态监测三大门户 · 微信分享聚合页",
        "public": True,
        "auto_init": False,
        "has_pages": True,
    })
    print("create repo:", st, body[:120] if st >= 400 else "")

# 2) git 初始化并推送
os.system('git init -q')
subprocess.run(["git", "add", "-A"], check=True)
subprocess.run(["git", "commit", "-q", "-m", "init: 南方电网三大门户分享页"], check=True)
subprocess.run(["git", "branch", "-M", "main"], check=True)
remote = f"https://{OWNER}:{TOKEN}@github.com/{OWNER}/{REPO}.git"
subprocess.run(["git", "remote", "remove", "origin"], capture_output=True)
subprocess.run(["git", "remote", "add", "origin", remote], check=True)
r = subprocess.run(["git", "push", "-u", "origin", "main", "--force"], capture_output=True, text=True)
print("push:", r.returncode, (r.stderr or r.stdout)[-200:])

# 3) 启用 GitHub Pages
st, body = api("POST", f"/repos/{OWNER}/{REPO}/pages", {"source": {"branch": "main", "path": "/"}})
print("enable pages:", st, body[:160] if st >= 400 else "")

# 4) 轮询站点可用性
ok = False
for i in range(10):
    time.sleep(4)
    try:
        code = urllib.request.urlopen(HUB, timeout=10).getcode()
        if code == 200:
            ok = True
            print("site HTTP 200 at attempt", i + 1)
            break
        print("attempt", i + 1, "code", code)
    except Exception as e:
        print("attempt", i + 1, "err", str(e)[:80])
print("HUB_URL", HUB, "OK" if ok else "NOT_READY")
