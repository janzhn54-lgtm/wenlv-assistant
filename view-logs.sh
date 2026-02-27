#!/bin/bash
# 查看 OpenClaw 日志的快捷脚本

echo "📋 OpenClaw 日志查看工具"
echo ""
echo "1. 查看实时日志 (按 Ctrl+C 退出)"
echo "2. 查看最近的错误"
echo "3. 查看健康检查历史"
echo "4. 清理旧日志"
echo ""

LOG_DIR="$HOME/.openclaw/logs"

if [ "$1" = "live" ] || [ "$1" = "1" ]; then
    echo "🔄 正在查看实时日志..."
    openclaw logs --follow
elif [ "$1" = "error" ] || [ "$1" = "2" ]; then
    echo "❌ 最近的错误日志："
    find "$LOG_DIR" -name "*.log" -type f -exec grep -l "ERROR\|error\|Error" {} \; | head -5
elif [ "$1" = "health" ] || [ "$1" = "3" ]; then
    echo "🏥 健康检查历史："
    ls -la "$LOG_DIR/health/" 2>/dev/null | tail -10
elif [ "$1" = "clean" ] || [ "$1" = "4" ]; then
    echo "🧹 清理30天前的日志..."
    find "$LOG_DIR" -name "*.log" -mtime +30 -delete
    echo "✅ 清理完成"
else
    echo "用法: ./view-logs.sh [live|error|health|clean]"
    echo "  live    - 实时日志"
    echo "  error   - 错误日志"
    echo "  health  - 健康检查"
    echo "  clean   - 清理旧日志"
fi
