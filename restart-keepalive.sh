#!/bin/bash
# 重启保活服务（如果 Codespace 重启后）

if pgrep -f "keepalive-daemon.sh" > /dev/null; then
    echo "保活服务已在运行"
else
    echo "启动保活服务..."
    nohup /home/codespace/.openclaw/workspace/keepalive-daemon.sh > /dev/null 2>&1 &
    echo "保活服务已启动，PID: $!"
fi
