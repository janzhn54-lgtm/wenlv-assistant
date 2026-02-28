#!/usr/bin/env python3
"""
测试DeepSeek API连接
"""

import requests
import json

API_KEY = "sk-d55324c1bd464b4daee34ec09c027993"

# 测试不同的API端点
endpoints = [
    "https://api.deepseek.com/v1/chat/completions",
    "https://api.deepseek.com/chat/completions",
    "https://api.deepseek.com/v1/models",
]

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

print("🔍 测试DeepSeek API连接...")
print("=" * 50)

for url in endpoints:
    print(f"\n测试: {url}")
    try:
        if "chat" in url:
            payload = {
                "model": "deepseek-chat",
                "messages": [{"role": "user", "content": "Hello, test"}],
                "max_tokens": 10
            }
            response = requests.post(url, headers=headers, json=payload, timeout=10)
        else:
            response = requests.get(url, headers=headers, timeout=10)
        
        print(f"状态码: {response.status_code}")
        
        if response.status_code == 200:
            print("✅ 连接成功！")
            print(f"响应: {response.text[:200]}...")
        else:
            print(f"❌ 失败: {response.text[:200]}")
            
    except Exception as e:
        print(f"❌ 错误: {e}")

print("\n" + "=" * 50)
print("测试完成")
