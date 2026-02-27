#!/bin/bash
# 每小时Token报告自动发送脚本
# 后台持续运行

while true; do
    # 获取当前时间
    current_hour=$(date +%H)
    current_min=$(date +%M)
    
    # 每小时的第0分钟发送报告
    if [ "$current_min" == "00" ]; then
        echo "[$(date)] 发送每小时Token报告..." >> /home/codespace/.openclaw/logs/token-cron.log
        
        # 生成并发送报告
        cd /home/codespace/.openclaw/workspace
        bash token-monitor.sh > /tmp/token-report.txt 2>&1
        
        # 这里可以添加发送到飞书的逻辑
        # 目前只是记录到日志
        cat /tmp/token-report.txt >> /home/codespace/.openclaw/logs/token-cron.log
        
        echo "[$(date)] 报告已发送" >> /home/codespace/.openclaw/logs/token-cron.log
        echo "---" >> /home/codespace/.openclaw/logs/token-cron.log
        
        # 等待60秒，避免同一分钟重复执行
        sleep 60
    fi
    
    # 每分钟检查一次
    sleep 60
done
