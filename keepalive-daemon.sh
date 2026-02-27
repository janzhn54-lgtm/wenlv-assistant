#!/bin/bash
# 强化保活脚本 - 每5分钟自动活动，防止 Codespace 休眠

LOG_FILE="$HOME/.codespace-keepalive.log"
REPO_DIR="/home/codespace/.openclaw/workspace"

echo "[$(date)] 保活服务启动" >> "$LOG_FILE"

cd "$REPO_DIR" || exit 1

while true; do
    # 1. 记录活动时间
    echo "[$(date)] Keepalive heartbeat" >> "$LOG_FILE"
    
    # 2. 创建空提交（模拟活动）
    git commit --allow-empty -m "keepalive: $(date -u +%Y-%m-%d_%H:%M:%S)" 2>/dev/null || true
    
    # 3. 推送（保持远程同步）
    git push origin main 2>/dev/null || true
    
    # 4. 写入系统活动日志
    echo "Codespace active at $(date)" > ~/.codespace-active.log
    
    # 5. 等待5分钟
    sleep 300
done
