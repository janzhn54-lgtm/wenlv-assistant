#!/usr/bin/env python3
"""
图片获取解决方案 - 自动下载项目图片
"""

import requests
import os
from urllib.parse import urlparse

def download_image(url, save_path):
    """下载单张图片"""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get(url, headers=headers, timeout=30)
        if response.status_code == 200:
            with open(save_path, 'wb') as f:
                f.write(response.content)
            return True
    except Exception as e:
        print(f"下载失败: {e}")
    return False

# 阿丽拉乌镇图片资源（公开可访问的）
image_sources = {
    "alila_wuzhen": [
        # 建筑外观
        "https://images.adsttc.com/media/images/5c12/5926/08a5/e54b/ad00/0df2/slideshow/-_HB_1018_0147_v3.jpg",
        # 水院景观
        "https://images.adsttc.com/media/images/5c12/5936/08a5/e54b/ad00/0df5/slideshow/-_HB_1018_0181_v2.jpg",
    ]
}

# 创建图片目录
os.makedirs("images/projects/alila_wuzhen", exist_ok=True)

print("🖼️ 自动下载项目图片...")
print("=" * 50)

# 尝试下载（可能会有权限问题，需要测试）
for project, urls in image_sources.items():
    print(f"\n项目: {project}")
    for i, url in enumerate(urls):
        filename = f"images/projects/{project}/image_{i+1}.jpg"
        print(f"  下载: {url[:50]}...")
        if download_image(url, filename):
            print(f"  ✅ 成功: {filename}")
        else:
            print(f"  ❌ 失败: 访问受限")

print("\n" + "=" * 50)
print("✅ 图片下载完成（部分可能因权限失败）")
