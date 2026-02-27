#!/bin/bash
# OpenClaw 健康检查脚本
# 每30分钟运行一次，记录状态

LOG_DIR="$HOME/.openclaw/logs/health"
mkdir -p "$LOG_DIR"

TIMESTAMP=$(date '+%Y-%m-%d_%H-%M-%S')
LOG_FILE="$LOG_DIR/health-$TIMESTAMP.log"

echo "=== OpenClaw Health Check - $(date) ===" > "$LOG_FILE"
echo "" >> "$LOG_FILE"

# 检查状态
openclaw status >> "$LOG_FILE" 2>&1

echo "" >> "$LOG_FILE"
echo "=== Check completed at $(date) ===" >> "$LOG_FILE"

# 只保留最近30天的日志
find "$LOG_DIR" -name "health-*.log" -mtime +30 -delete

echo "Health check logged to $LOG_FILE"
