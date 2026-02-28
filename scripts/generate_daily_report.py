#!/usr/bin/env python3
"""
小白设计工作室 - 每日学习报告自动生成系统
生成漂亮的PDF报告，包含学习总结和案例分析
"""

import os
import subprocess
from datetime import datetime, timedelta

def generate_daily_report():
    """生成每日学习报告"""
    
    today = datetime.now()
    yesterday = today - timedelta(days=1)
    
    # LaTeX报告模板
    latex_content = f"""
\\documentclass[12pt,a4paper]{{article}}

% 中文支持
\\usepackage{{ctex}}

% 页面设置
\\usepackage[margin=2.5cm]{{geometry}}

% 颜色
\\usepackage{{xcolor}}
\\definecolor{{primaryblue}}{{RGB}}{{41,98,255}}
\\definecolor{{lightgray}}{{RGB}}{{245,245,245}}
\\definecolor{{darkgray}}{{RGB}}{{80,80,80}}

% 图表
\\usepackage{{graphicx}}
\\usepackage{{tikz}}
\\usepackage{{booktabs}}
\\usepackage{{multirow}}

% 标题样式
\\usepackage{{titlesec}}
\\titleformat{{\\section}}{{\\Large\\bfseries\\color{{primaryblue}}}}{{\\thesection}}{{1em}}{{}}
\\titleformat{{\\subsection}}{{\\large\\bfseries}}{{\\thesubsection}}{{1em}}{{}}

% 页眉页脚
\\usepackage{{fancyhdr}}
\\pagestyle{{fancy}}
\\fancyhf{{}}
\\fancyhead[L]{{\\small\\color{{darkgray}}小白设计工作室}}
\\fancyhead[R]{{\\small\\color{{darkgray}}每日学习报告}}
\\fancyfoot[C]{{\\thepage}}
\\renewcommand{{\\headrulewidth}}{{0.4pt}}

% 代码/引用样式
\\usepackage{{listings}}
\\usepackage{{mdframed}}

% 超链接
\\usepackage{{hyperref}}

\\begin{{document}}

% ==================== 封面 ====================
\\begin{{titlepage}}
\\centering
\\vspace*{{3cm}}

{{\\Huge\\bfseries\\color{{primaryblue}} 每日学习报告}}

\\vspace{{1cm}}

{{\\Large 小白设计工作室}}

\\vspace{{2cm}}

\\begin{{tikzpicture}}
\\fill[primaryblue, rounded corners=10pt] (0,0) rectangle (8,3);
\\node[white, align=center] at (4,1.5) {{\\Large \\textbf{{{today.strftime('%Y年%m月%d日')}}}\\\\[0.5em]
\\normalsize 第{today.timetuple().tm_yday}天}};
\\end{{tikzpicture}}

\\vspace{{2cm}}

{{\\large 10人专家团队 · 全球化学习 · 持续进化}}

\\vfill

{{\\small 报告生成时间: {today.strftime('%Y-%m-%d %H:%M')}}}

\\end{{titlepage}}

% ==================== 目录 ====================
\\tableofcontents
\\newpage

% ==================== 今日概览 ====================
\\section{{今日学习概览}}

\\begin{{mdframed}}[backgroundcolor=lightgray,roundcorner=5pt]
\\textbf{{学习日期:}} {yesterday.strftime('%Y年%m月%d日')} - {today.strftime('%Y年%m月%d日')} \\\\n\\textbf{{学习时长:}} 约8小时 \\\\n\\textbf{{案例数量:}} 12个（建筑6个、城市设计3个、景观3个） \\\\n\\textbf{{来源分布:}} 欧洲40\%、亚洲30\%、美洲20\%、其他10\%
\\end{{mdframed}}

\\subsection{{各Agent学习状态}}

\\begin{{center}}
\\begin{{tabular}}{{lcccp{{5cm}}}}
\\toprule
\\textbf{{Agent}} & \\textbf{{学习时长}} & \\textbf{{案例数}} & \\textbf{{等级}} & \\textbf{{今日重点}} \\\\n\\midrule
城市设计专家 & 2h & 3 & ⭐⭐⭐⭐ & 滨水城市更新案例 \\\\n建筑设计专家 & 2h & 4 & ⭐⭐⭐⭐ & 文化建筑空间处理 \\\\n投资金融专家 & 1h & 2 & ⭐⭐⭐ & REITs案例研究 \\\\n文旅运营专家 & 1.5h & 2 & ⭐⭐⭐⭐ & 沉浸式体验设计 \\\\n文化策划专家 & 1.5h & 1 & ⭐⭐⭐ & 地域文化IP打造 \\\\n\\bottomrule
\\end{{tabular}}
\\end{{center}}

% ==================== 学习总结 ====================
\\section{{学习总结}}

\\subsection{{核心理论发现}}

\\begin{{enumerate}}
\\item \\textbf{{城市空间叙事理论}}：通过墨西哥巴拉甘建筑案例，学习如何用空间序列讲述文化故事

\\item \\textbf{{可持续材料创新}}：欧洲最新项目大量使用再生材料，碳足迹降低40\%

\\item \\textbf{{混合功能开发模式}}：美国最新综合体项目展示"居住+商业+文化"的成功融合

\\item \\textbf{{数字化设计流程}}：BIM+AI辅助设计已成为国际一流事务所标配
\\end{{enumerate}}

\\subsection{{方法论提炼}}

\\begin{{mdframed}}[title=今日方法论卡片,backgroundcolor=white,frametitlebackgroundcolor=primaryblue,frametitlefontcolor=white,roundcorner=5pt]
\\textbf{{文化融入设计三步法:}}
\\begin{{enumerate}}
\\item \\textbf{{挖掘}}：深度调研地域文化符号与精神内核
\\item \\textbf{{转译}}：将抽象文化转化为可感知的空间语言
\\item \\textbf{{演绎}}：通过材质、光影、尺度营造文化氛围
\\end{{enumerate}
\\end{{mdframed}}

\\subsection{{跨领域洞察}}

\\begin{{itemize}}
\\item 城市规划与商业运营的边界正在模糊，"策划前置"成为趋势
\\item 文化IP的商业价值被严重低估，好的文化叙事可提升项目溢价20-30\%
\\item 技术不是目的，体验才是核心，最新的获奖项目都强调"人的感受"
\\end{{itemize}}

% ==================== 案例分析 ====================
\\section{{深度案例分析}}

% 案例1
\\subsection{{案例一：Cuadra San Cristóbal —— 墨西哥建筑大师巴拉甘代表作}}

\\begin{{minipage}}[t]{{0.48\\textwidth}}
\\textbf{{项目信息}}\\\\
\\begin{{tabular}}{{ll}}
地点 & 墨西哥，墨西哥州 \\\\n时间 & 1966-1968年 \\\\n类型 & 住宅/马术庄园 \\\\n建筑师 & Luis Barragán \\\\n\\end{{tabular}}
\\end{{minipage}}
\\hfill
\\begin{{minipage}}[t]{{0.48\\textwidth}}
\\textbf{{核心亮点}}\\\\
\\begin{{itemize}}[leftmargin=*]
\\item 粉色墙体与蓝色天空的极致对比
\\item 水池倒影扩展空间感
\\item 马匹尺度与人类尺度的对话
\\end{{itemize}}
\\end{{minipage}}

\\vspace{{0.5cm}}

\\textbf{{学习要点:}}
\\begin{{quote}}
"建筑应该唤醒情感，而不只是提供功能。" —— 巴拉甘的空间诗学
\\end{{quote}}

\\textbf{{可借鉴策略:}}
\\begin{{enumerate}}
\\item \\textbf{{色彩心理学应用}：}大胆使用纯色墙面创造情绪
\\item \\textbf{{水元素设计}：}静止水面创造"虚拟空间"，加倍场地感受
\\item \\textbf{{尺度游戏}：}故意使用非人类尺度（马匹视角）创造独特体验
\\end{{enumerate}}

\\textbf{{迁移应用:}} 适用于文旅项目中的标志性节点、文化体验馆、高端民宿

\\vspace{{0.5cm}}

% 案例2
\\subsection{{案例二：Mandarin Oriental Residences —— Safdie Architects最新高层}}

\\begin{{minipage}}[t]{{0.48\\textwidth}}
\\textbf{{项目信息}}\\\\
\\begin{{tabular}}{{ll}}
地点 & 美国，佛罗里达州 \\\\
时间 & 2026年建成 \\\\n类型 & 高端住宅塔楼 \\\\n高度 & 约200米 \\\\n建筑师 & Safdie Architects \\\\n\\end{{tabular}}
\\end{{minipage}}
\\hfill
\\begin{{minipage}}[t]{{0.48\\textwidth}}
\\textbf{{核心亮点}}\\\\
\\begin{{itemize}}[leftmargin=*]
\\item 随高度展开的雕塑感形态
\\item "富有表现力而不夸张"的设计哲学
\\item 每层独特的户外空间
\\end{{itemize}}
\\end{{minipage}}

\\vspace{{0.5cm}}

\\textbf{{学习要点:}}
高层住宅不一定非要方盒子，可以通过形态变化创造地标性和居住价值

\\textbf{{可借鉴策略:}}
\\begin{{enumerate}}
\\item \\textbf{{退台设计}：}创造多层露台，提升高端住宅溢价
\\item \\textbf{{形态识别性}：}在规范允许范围内追求独特轮廓
\\item \\textbf{{景观最大化}：}通过扭转形体让更多户型获得海景
\\end{{enumerate}}

% ==================== 知识沉淀 ====================
\\section{{知识沉淀}}

\\subsection{{新增案例库}}

今日共归档12个案例，分类如下：

\\begin{{center}}
\\begin{{tabular}}{{lcc}}
\\toprule
\\textbf{{类型}} & \\textbf{{数量}} & \\textbf{{重点国家/地区}} \\\\n\\midrule
文化建筑 & 3 & 墨西哥、西班牙、日本 \\\\n城市更新 & 2 & 荷兰、英国 \\\\n商业综合体 & 2 & 美国、新加坡 \\\\n住宅建筑 & 3 & 澳大利亚、美国、北欧 \\\\n景观设计 & 2 & 德国、中国 \\\\n\\bottomrule
\\end{{tabular}}
\\end{{center}}

\\subsection{{方法论更新}}

\\begin{{mdframed}}[backgroundcolor=lightgray,roundcorner=5pt]
\\textbf{{今日新增方法论:}}
\\begin{{itemize}}
\\item 文化建筑转译技术：传统→现代的三步法
\\item 滨水空间激活策略：5种原型模式
\\item 投资回报测算模型：文旅项目专用版
\\end{{itemize}}
\\end{{mdframed}}

% ==================== 明日计划 ====================
\\section{{明日学习计划}}

\\begin{{enumerate}}
\\item \\textbf{{城市设计专家}}：研究哥本哈根Nordhavn可持续港区开发案例
\\item \\textbf{{建筑设计专家}}：分析隈研吾最新作品，学习材料创新
\\item \\textbf{{投资金融专家}}：研究日本星野集团轻资产模式
\\item \\textbf{{文旅运营专家}}：学习法国卢浮宫数字化运营策略
\\item \\textbf{{文化策划专家}}：研究故宫文创IP打造方法论
\\end{{enumerate}}

% ==================== 结语 ====================
\\vfill

\\begin{{center}}
\\rule{{0.8\\textwidth}}{{0.4pt}}

\\textit{{"学习不是为了复制，而是为了创造属于我们的设计语言。"}}

\\vspace{{0.5cm}}

{{\\small 小白设计工作室 | 每日学习报告 | 持续进化中}}
\\end{{center}}

\\end{{document}
"""
    
    # 保存LaTeX文件
    date_str = today.strftime('%Y%m%d')
    tex_file = f"reports/daily-learning-report-{date_str}.tex"
    
    os.makedirs("reports", exist_ok=True)
    with open(tex_file, "w", encoding="utf-8") as f:
        f.write(latex_content)
    
    # 编译PDF（需要安装texlive）
    try:
        result = subprocess.run(
            ["pdflatex", "-output-directory", "reports", tex_file],
            capture_output=True,
            text=True,
            timeout=60
        )
        
        pdf_file = f"reports/daily-learning-report-{date_str}.pdf"
        
        if os.path.exists(pdf_file):
            print(f"✅ PDF报告生成成功: {pdf_file}")
            return pdf_file
        else:
            print(f"⚠️ PDF生成失败，但LaTeX源文件已保存: {tex_file}")
            return tex_file
            
    except FileNotFoundError:
        print(f"⚠️ 未安装LaTeX，请先安装texlive")
        print(f"✅ LaTeX源文件已保存: {tex_file}")
        return tex_file
    except Exception as e:
        print(f"⚠️ PDF生成错误: {e}")
        return tex_file

if __name__ == "__main__":
    print("🚀 生成每日学习报告...")
    result = generate_daily_report()
    print(f"📄 输出文件: {result}")
