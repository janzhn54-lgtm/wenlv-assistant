#!/bin/bash
# 实时操作日志推送脚本
# 将操作实时推送到飞书

FEISHU_WEBHOOK="${FEISHU_WEBHOOK_URL}"
LOG_FILE="$HOME/.openclaw/logs/operations.log"

# 创建日志目录
mkdir -p "$HOME/.openclaw/logs"

# 记录操作并推送
log_and_notify() {
    local message="$1"
    local timestamp=$(date '+%Y-%m-%d %H:%M:%S')
    local full_message="[$timestamp] $message"
    
    # 写入本地日志
    echo "$full_message" >> "$LOG_FILE"
    
    # 推送到飞书（如果配置了 webhook）
    if [ -n "$FEISHU_WEBHOOK" ]; then
        curl -s -X POST "$FEISHU_WEBHOOK" \
            -H "Content-Type: application/json" \
            -d "{
                \"msg_type\": \"text\",
                \"content\": {
                    \"text\": \"小白操作日志: $message\"
                }
            }" > /dev/null 2>&1
    fi
}

# 使用方式
# log_and_notify "开始执行 xxx 任务"
