#!/bin/bash
# 每小时Token报告发送脚本
# 此脚本由 cron 每小时调用

cd /home/codespace/.openclaw/workspace

# 生成报告
REPORT=$(bash token-monitor.sh)

# 发送到飞书（通过消息工具）
echo "$REPORT"