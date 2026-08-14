# -*- coding: utf-8 -*-
import qrcode
from qrcode.image.svg import SvgPathImage

HUB = "https://hxj0515.github.io/csg-power-hub/"
sites = [
    {
        "ic": "⚡", "title": "南方电网电力讯息",
        "url": "https://hxj0515.github.io/csg-power-daily/",
        "desc": "全网电力运行、负荷、绿电交易、现货市场、重大工程等每日动态速览。",
        "tag": "csg-power-daily",
    },
    {
        "ic": "📑", "title": "南方电网招投标讯息",
        "url": "https://hxj0515.github.io/csg-power-daily2/",
        "desc": "供应商生态、招投标批次、中标分析、采购趋势与金额明细。",
        "tag": "csg-power-daily2",
    },
    {
        "ic": "🏢", "title": "南方电网组织动态",
        "url": "https://hxj0515.github.io/csg-power-daily3/",
        "desc": "组织架构全量名录、近期重大动作、未来战略方向四级拆解。",
        "tag": "csg-power-daily3",
    },
]

# 二维码（指向本页自身，方便「扫码分享/收藏」）
qr = qrcode.QRCode(box_size=10, border=2, error_correction=qrcode.constants.ERROR_CORRECT_M)
qr.add_data(HUB)
qr_svg = qr.make_image(image_factory=SvgPathImage).to_string().decode("utf-8")
if qr_svg.startswith("<?xml"):
    qr_svg = qr_svg.split(">", 1)[1]

cards = ""
for s in sites:
    cards += f"""
    <div class="card">
      <div class="ic">{s['ic']}</div>
      <div class="main">
        <h3>{s['title']}</h3>
        <p class="desc">{s['desc']}</p>
        <span class="tag">{s['tag']}</span>
      </div>
      <a class="open" href="{s['url']}" target="_blank" rel="noopener">打开 ↗</a>
    </div>"""

tpl = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1,user-scalable=no">
<title>南方电网动态监测 · 三大门户</title>
<meta name="description" content="南方电网电力讯息、招投标讯息、组织动态，三大每日更新门户，一键直达。">
<meta property="og:title" content="南方电网动态监测 · 三大门户">
<meta property="og:description" content="电力讯息 · 招投标讯息 · 组织动态，每日自动更新，一键直达。">
<meta property="og:type" content="website">
<meta property="og:url" content="__HUB__">
<meta name="theme-color" content="#0a4ea3">
<style>
:root{--bg:#eef2f9;--card:#fff;--ink:#16203a;--sub:#5b6b86;--brand:#0a4ea3;--brand2:#0fb6c4;--line:#e6ebf3}
*{box-sizing:border-box;-webkit-tap-highlight-color:transparent}
body{margin:0;background:var(--bg);color:var(--ink);font-family:-apple-system,BlinkMacSystemFont,"PingFang SC","Microsoft YaHei",sans-serif;line-height:1.6}
.wrap{max-width:560px;margin:0 auto;padding:0 16px 44px}
.hero{background:linear-gradient(135deg,#0a4ea3 0%,#0fb6c4 100%);color:#fff;padding:36px 20px 32px;text-align:center;border-radius:0 0 24px 24px}
.hero .badge{display:inline-block;background:rgba(255,255,255,.16);border:1px solid rgba(255,255,255,.32);padding:3px 12px;border-radius:999px;font-size:12px;margin-bottom:14px}
.hero h1{margin:0 0 8px;font-size:22px;letter-spacing:.5px}
.hero p{margin:0;font-size:13.5px;opacity:.92}
.cards{margin-top:-18px}
.card{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:16px;margin:14px 0;box-shadow:0 8px 22px rgba(20,40,80,.07);display:flex;gap:13px;align-items:center}
.card .ic{width:46px;height:46px;flex:0 0 46px;border-radius:12px;display:flex;align-items:center;justify-content:center;font-size:24px;background:linear-gradient(135deg,#eaf2ff,#e6fbff)}
.card .main{flex:1;min-width:0}
.card h3{margin:0 0 4px;font-size:16.5px;color:var(--ink)}
.card .desc{margin:0;font-size:12.5px;color:var(--sub);line-height:1.55}
.card .tag{display:inline-block;margin-top:7px;font-size:11px;color:var(--brand);background:#eaf2ff;padding:2px 8px;border-radius:6px}
.card a.open{display:inline-flex;align-items:center;justify-content:center;align-self:center;background:var(--brand);color:#fff;text-decoration:none;font-size:13px;font-weight:600;padding:9px 14px;border-radius:10px;white-space:nowrap}
.card a.open:active{opacity:.85}
.tip{background:#fff;border:1px solid var(--line);border-radius:14px;padding:16px 18px;margin:18px 0}
.tip h4{margin:0 0 8px;font-size:14.5px;color:var(--brand)}
.tip ol{margin:0;padding-left:20px;font-size:13px;color:var(--sub)}
.tip li{margin:6px 0}
.qr{text-align:center;margin:22px 0 6px}
.qr .box{display:inline-block;background:#fff;border:8px solid #fff;border-radius:18px;box-shadow:0 6px 20px rgba(20,40,80,.12)}
.qr .box svg{display:block;width:148px;height:148px}
.qr p{font-size:12px;color:var(--sub);margin:12px 0 0}
.foot{text-align:center;font-size:11.5px;color:#9aa7bd;margin-top:26px;line-height:1.7}
</style>
</head>
<body>
<div class="hero">
  <span class="badge">每日自动更新</span>
  <h1>南方电网动态监测 · 三大门户</h1>
  <p>电力讯息 · 招投标讯息 · 组织动态，一网打尽</p>
</div>
<div class="wrap">
  <div class="cards">__CARDS__
  </div>

  <div class="tip">
    <h4>📲 微信里怎么收藏 / 分享</h4>
    <ol>
      <li>点右上角 <b>···</b>，选「<b>发送给朋友</b>」或「<b>分享到朋友圈</b>」。</li>
      <li>选「<b>收藏</b>」，随时在微信「我 → 收藏」打开。</li>
      <li>在微信内置浏览器点「<b>··· → 在浏览器打开 / 添加到桌面</b>」，可生成手机快捷方式。</li>
      <li>把下面二维码发给同事，扫码即可直达本页。</li>
    </ol>
  </div>

  <div class="qr">
    <div class="box">__QR__</div>
    <p>长按或扫码，分享 / 收藏本页</p>
  </div>

  <div class="foot">
    南方电网动态监测三大门户 · 数据来源于公开渠道，每日自动更新<br>
    本页为导航聚合，内容以各子站为准
  </div>
</div>
</body>
</html>
"""

html = (tpl.replace("__HUB__", HUB)
            .replace("__CARDS__", cards)
            .replace("__QR__", qr_svg))

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("written index.html", len(html), "bytes")
