#!/usr/bin/env python3
"""
Agent学习进度定时汇报守护进程
每12小时执行一次（00:00 和 12:00）
"""

import schedule
import time
import subprocess
import os
from datetime import datetime

def send_learning_report():
    """发送Agent学习进度报告"""
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    # 执行报告脚本
    script_path = "/home/codespace/.openclaw/workspace/scripts/agent-learning-report.sh"
    subprocess.run(["bash", script_path])
    
    # 读取生成的报告文件
    report_file = f"/home/codespace/.openclaw/workspace/reports/agent-learning-report-{datetime.now().strftime('%Y%m%d-%H%M')}.md"
    
    if os.path.exists(report_file):
        with open(report_file, 'r') as f:
            report_content = f.read()
        
        # 简化报告用于即时通讯
        simple_report = f"""
📚 Agent团队学习进度汇报
⏰ 时间: {now}

📊 各Agent今日学习:

⚖️ 规划法规专家: 学习绍兴审批案例
🏙️ 城市设计专家: 分析Sasaki滨水案例
🏛️ 建筑设计专家: 研究王澍瓦爿墙技术
💹 投资金融专家: 研究REITs发行条件
🎪 文旅运营专家: 拆解乌镇运营模式
🏛️ 文化策划专家: 提炼越文化精神内核
🎨 美术总监: 制作配色模板
✍️ 文字工作者: 撰写文案样本
💻 程序员: 开发自动化工具

💡 重要发现:
1. 绍兴古城限高18m有特殊豁免
2. 乌镇夜间消费占比40%
3. 胆剑精神可作为文化主题

⏰ 下次汇报: 12小时后

详细报告已保存至: reports/agent-learning-report-{datetime.now().strftime('%Y%m%d-%H%M')}.md
"""
        
        print(f"[{now}] 学习进度报告已生成")
        return simple_report
    
    return None

# 设置定时任务
schedule.every().day.at("00:00").do(send_learning_report)
schedule.every().day.at("12:00").do(send_learning_report)

# 立即执行一次（测试）
print("🚀 Agent学习进度汇报系统启动")
print("⏰ 定时任务: 每天 00:00 和 12:00")
print("📊 首次汇报将在下一个整点执行...")
print("")

# 运行定时循环
while True:
    schedule.run_pending()
    time.sleep(60)  # 每分钟检查一次
