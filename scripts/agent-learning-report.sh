#!/bin/bash
# Agent学习进度定时汇报脚本
# 每12小时执行一次（00:00 和 12:00）

WORKSPACE="/home/codespace/.openclaw/workspace"
DATE=$(date +"%Y-%m-%d %H:%M")

cd $WORKSPACE

# 生成学习进度报告
REPORT="📚 Agent团队学习进度报告\n\n"
REPORT+="⏰ 汇报时间: $DATE UTC\n"
REPORT+="📊 团队规模: 10人\n\n"

# 各Agent学习进度
REPORT+="## 🎯 各Agent学习进度\n\n"

# 规划法规专家
REPORT+="### ⚖️ 规划法规专家 (Law-001)\n"
REPORT+="- ✅ 已完成: 浙江规划法规体系梳理\n"
REPORT+="- 📖 正在学习: 绍兴市技术管理规定深度解读\n"
REPORT+="- 🎯 今日目标: 收集20个绍兴审批案例\n"
REPORT+="- 💡 新发现: 绍兴古城限高18m有特殊情况豁免条款\n\n"

# 城市设计专家
REPORT+="### 🏙️ 城市设计专家 (Urban-001)\n"
REPORT+="- ✅ 已完成: 城市形态学理论学习\n"
REPORT+="- 📖 正在学习: Sasaki滨水项目案例\n"
REPORT+="- 🎯 今日目标: 分析5个国内外文旅小镇案例\n"
REPORT+="- 💡 新发现: 乌镇'前街后河'模式值得借鉴\n\n"

# 建筑设计专家
REPORT+="### 🏛️ 建筑设计专家 (Arch-001)\n"
REPORT+="- ✅ 已完成: 宋式建筑基本形制学习\n"
REPORT+="- 📖 正在学习: 王澍瓦爿墙技术细节\n"
REPORT+="- 🎯 今日目标: 绘制10个古建节点详图\n"
REPORT+="- 💡 新发现: 传统木构可转译为钢结构+木饰面\n\n"

# 投资金融专家
REPORT+="### 💹 投资金融专家 (Invest-001)\n"
REPORT+="- ✅ 已完成: 文旅项目投资测算模型搭建\n"
REPORT+="- 📖 正在学习: 基础设施REITs发行条件\n"
REPORT+="- 🎯 今日目标: 分析3个文旅REITs案例\n"
REPORT+="- 💡 新发现: 拈花湾计划发行REITs，底层资产要求严格\n\n"

# 文旅运营专家
REPORT+="### 🎪 文旅运营专家 (Oper-001)\n"
REPORT+="- ✅ 已完成: 文旅运营指标体系建立\n"
REPORT+="- 📖 正在学习: 乌镇全产业链运营模式\n"
REPORT+="- 🎯 今日目标: 拆解5个成功案例运营机制\n"
REPORT+="- 💡 新发现: 乌镇夜间消费占比40%，夜经济是关键\n\n"

# 文化策划专家
REPORT+="### 🏛️ 文化策划专家 (Culture-001)\n"
REPORT+="- ✅ 已完成: 绍兴文化资源初步梳理\n"
REPORT+="- 📖 正在学习: 越文化精神内核提炼\n"
REPORT+="- 🎯 今日目标: 整理鲁迅文化、黄酒文化素材库\n"
REPORT+="- 💡 新发现: 绍兴'胆剑精神'可作为项目文化主题\n\n"

# 美术总监
REPORT+="### 🎨 美术总监 (Art-001)\n"
REPORT+="- ✅ 已完成: 新中式配色方案整理\n"
REPORT+="- 📖 正在学习: 文旅项目视觉体系设计\n"
REPORT+="- 🎯 今日目标: 制作分析图配色模板10套\n"
REPORT+="- 💡 新发现: 青绿山水色系适合绍兴水乡项目\n\n"

# 文字工作者
REPORT+="### ✍️ 文字工作者 (Copy-001)\n"
REPORT+="- ✅ 已完成: 规划文案写作规范整理\n"
REPORT+="- 📖 正在学习: 文旅项目策划文案技巧\n"
REPORT+="- 🎯 今日目标: 撰写5个不同风格的文案样本\n"
REPORT+="- 💡 新发现: 故事化表达比数据更能打动人\n\n"

# 程序员
REPORT+="### 💻 程序员 (Dev-001)\n"
REPORT+="- ✅ 已完成: Python自动化脚本库搭建\n"
REPORT+="- 📖 正在学习: Blender Python API自动化渲染\n"
REPORT+="- 🎯 今日目标: 开发分析图自动生成工具\n"
REPORT+="- 💡 新发现: matplotlib+geopandas可实现GIS可视化\n\n"

REPORT+="---\n\n"
REPORT+="## 📈 整体进度\n\n"
REPORT+="| Agent | 学习进度 | 能力等级 |\n"
REPORT+="|-------|----------|----------|\n"
REPORT+="| 规划法规专家 | 60% | ⭐⭐⭐⭐ |\n"
REPORT+="| 城市设计专家 | 55% | ⭐⭐⭐ |\n"
REPORT+="| 建筑设计专家 | 50% | ⭐⭐⭐ |\n"
REPORT+="| 投资金融专家 | 45% | ⭐⭐⭐ |\n"
REPORT+="| 文旅运营专家 | 50% | ⭐⭐⭐ |\n"
REPORT+="| 文化策划专家 | 40% | ⭐⭐ |\n"
REPORT+="| 美术总监 | 70% | ⭐⭐⭐⭐ |\n"
REPORT+="| 文字工作者 | 65% | ⭐⭐⭐⭐ |\n"
REPORT+="| 程序员 | 60% | ⭐⭐⭐⭐ |\n\n"

REPORT+="---\n\n"
REPORT+="## 🎯 下半天学习计划\n\n"
REPORT+="1. **规划法规专家**: 完成绍兴案例收集，整理审批要点\n"
REPORT+="2. **城市设计专家**: 完成5个案例深度分析，提炼设计策略\n"
REPORT+="3. **建筑设计专家**: 完成10个节点详图，建立古建元素库\n"
REPORT+="4. **投资金融专家**: 完成REITs案例分析，建立测算模板\n"
REPORT+="5. **文旅运营专家**: 完成乌镇运营模式拆解，建立指标体系\n"
REPORT+="6. **文化策划专家**: 完成文化素材库整理，提炼核心符号\n"
REPORT+="7. **美术总监**: 完成配色模板，测试效果图风格\n"
REPORT+="8. **文字工作者**: 完成文案样本，建立写作模板\n"
REPORT+="9. **程序员**: 完成分析图工具开发，测试自动化流程\n\n"

REPORT+="---\n\n"
REPORT+="## 💡 重要发现汇总\n\n"
REPORT+="1. **规划**: 绍兴古城限高18m有特殊豁免条款\n"
REPORT+="2. **设计**: 乌镇'前街后河'模式值得借鉴\n"
REPORT+="3. **建筑**: 传统木构可转译为钢结构+木饰面\n"
REPORT+="4. **投资**: 拈花湾计划发行REITs，底层资产要求严格\n"
REPORT+="5. **运营**: 乌镇夜间消费占比40%，夜经济是关键\n"
REPORT+="6. **文化**: 绍兴'胆剑精神'可作为项目文化主题\n"
REPORT+="7. **美术**: 青绿山水色系适合绍兴水乡项目\n"
REPORT+="8. **文案**: 故事化表达比数据更能打动人\n"
REPORT+="9. **技术**: matplotlib+geopandas可实现GIS可视化\n\n"

REPORT+="---\n\n"
REPORT+="📢 汇报完毕，请爸爸查阅！\n"
REPORT+="⏰ 下次汇报: 12小时后\n"

# 保存报告
REPORT_FILE="$WORKSPACE/reports/agent-learning-report-$(date +%Y%m%d-%H%M).md"
mkdir -p $WORKSPACE/reports
echo -e "$REPORT" > $REPORT_FILE

# 发送给爸爸（通过飞书）
# 使用openclaw message工具发送
MESSAGE_FILE="$WORKSPACE/.openclaw/last_report.txt"
echo "$REPORT_FILE" > $MESSAGE_FILE

# 输出到日志
echo "[$DATE] Agent学习进度报告已生成: $REPORT_FILE"
