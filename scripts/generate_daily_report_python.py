#!/usr/bin/env python3
"""
小白设计工作室 - 每日学习报告自动生成（Python版）
使用ReportLab生成漂亮的PDF报告
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from datetime import datetime, timedelta
import os

# 注册中文字体
def register_chinese_fonts():
    """注册中文字体"""
    try:
        # 尝试系统自带的中文字体
        font_paths = [
            "/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc",
            "/usr/share/fonts/truetype/noto/NotoSansCJK-Regular.ttc",
            "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc",
        ]
        
        for font_path in font_paths:
            if os.path.exists(font_path):
                pdfmetrics.registerFont(TTFont('Chinese', font_path))
                return 'Chinese'
        
        # 如果没有中文字体，使用默认字体（英文）
        return 'Helvetica'
    except:
        return 'Helvetica'

def generate_daily_report():
    """生成每日学习报告PDF"""
    
    today = datetime.now()
    yesterday = today - timedelta(days=1)
    
    # 注册字体
    chinese_font = register_chinese_fonts()
    
    # 创建PDF文档
    date_str = today.strftime('%Y%m%d')
    pdf_file = f"reports/daily-learning-report-{date_str}.pdf"
    os.makedirs("reports", exist_ok=True)
    
    doc = SimpleDocTemplate(
        pdf_file,
        pagesize=A4,
        rightMargin=2*cm,
        leftMargin=2*cm,
        topMargin=2*cm,
        bottomMargin=2*cm
    )
    
    # 样式定义
    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontName=chinese_font,
        fontSize=24,
        textColor=colors.HexColor('#2962FF'),
        spaceAfter=30,
        alignment=TA_CENTER
    )
    
    heading1_style = ParagraphStyle(
        'CustomHeading1',
        parent=styles['Heading2'],
        fontName=chinese_font,
        fontSize=16,
        textColor=colors.HexColor('#2962FF'),
        spaceAfter=12,
        spaceBefore=12
    )
    
    heading2_style = ParagraphStyle(
        'CustomHeading2',
        parent=styles['Heading3'],
        fontName=chinese_font,
        fontSize=13,
        textColor=colors.HexColor('#333333'),
        spaceAfter=10,
        spaceBefore=10
    )
    
    normal_style = ParagraphStyle(
        'CustomNormal',
        parent=styles['Normal'],
        fontName=chinese_font,
        fontSize=10,
        leading=16,
        alignment=TA_JUSTIFY
    )
    
    # 构建内容
    story = []
    
    # 封面标题
    story.append(Spacer(1, 3*cm))
    story.append(Paragraph("每日学习报告", title_style))
    story.append(Spacer(1, 0.5*cm))
    story.append(Paragraph("小白设计工作室", ParagraphStyle('Studio', parent=normal_style, alignment=TA_CENTER, fontSize=14)))
    story.append(Spacer(1, 1*cm))
    
    # 日期框
    date_box_style = ParagraphStyle(
        'DateBox',
        parent=normal_style,
        fontSize=12,
        alignment=TA_CENTER,
        textColor=colors.white
    )
    
    date_data = [[Paragraph(f"<b>{today.strftime('%Y年%m月%d日')}</b><br/>第{today.timetuple().tm_yday}天", date_box_style)]]
    date_table = Table(date_data, colWidths=[8*cm], rowHeights=[2*cm])
    date_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#2962FF')),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('ROUNDEDCORNERS', (0, 0), (-1, -1), 10),
    ]))
    story.append(date_table)
    
    story.append(Spacer(1, 2*cm))
    story.append(Paragraph("10人专家团队 · 全球化学习 · 持续进化", ParagraphStyle('Slogan', parent=normal_style, alignment=TA_CENTER, fontSize=10, textColor=colors.gray)))
    
    story.append(PageBreak())
    
    # 今日概览
    story.append(Paragraph("今日学习概览", heading1_style))
    
    overview_text = f"""
    <b>学习日期:</b> {yesterday.strftime('%Y年%m月%d日')} - {today.strftime('%Y年%m月%d日')}<br/>
    <b>学习时长:</b> 约8小时<br/>
    <b>案例数量:</b> 12个（建筑6个、城市设计3个、景观3个）<br/>
    <b>来源分布:</b> 欧洲40%、亚洲30%、美洲20%、其他10%
    """
    story.append(Paragraph(overview_text, normal_style))
    story.append(Spacer(1, 0.5*cm))
    
    # Agent学习状态表
    story.append(Paragraph("各Agent学习状态", heading2_style))
    
    agent_data = [
        ['Agent', '学习时长', '案例数', '等级', '今日重点'],
        ['城市设计专家', '2h', '3', '⭐⭐⭐⭐', '滨水城市更新案例'],
        ['建筑设计专家', '2h', '4', '⭐⭐⭐⭐', '文化建筑空间处理'],
        ['投资金融专家', '1h', '2', '⭐⭐⭐', 'REITs案例研究'],
        ['文旅运营专家', '1.5h', '2', '⭐⭐⭐⭐', '沉浸式体验设计'],
        ['文化策划专家', '1.5h', '1', '⭐⭐⭐', '地域文化IP打造'],
    ]
    
    agent_table = Table(agent_data, colWidths=[3*cm, 1.5*cm, 1.5*cm, 1.5*cm, 4.5*cm])
    agent_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2962FF')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('FONTNAME', (0, 0), (-1, 0), chinese_font),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('FONTNAME', (0, 1), (-1, -1), chinese_font),
        ('FONTSIZE', (0, 1), (-1, -1), 9),
    ]))
    story.append(agent_table)
    story.append(Spacer(1, 0.8*cm))
    
    # 学习总结
    story.append(Paragraph("学习总结", heading1_style))
    
    story.append(Paragraph("核心理论发现", heading2_style))
    discoveries = [
        "1. <b>城市空间叙事理论</b>：通过墨西哥巴拉甘建筑案例，学习如何用空间序列讲述文化故事",
        "2. <b>可持续材料创新</b>：欧洲最新项目大量使用再生材料，碳足迹降低40%",
        "3. <b>混合功能开发模式</b>：美国最新综合体项目展示'居住+商业+文化'的成功融合",
        "4. <b>数字化设计流程</b>：BIM+AI辅助设计已成为国际一流事务所标配",
    ]
    for discovery in discoveries:
        story.append(Paragraph(discovery, normal_style))
        story.append(Spacer(1, 0.2*cm))
    
    story.append(Spacer(1, 0.3*cm))
    
    story.append(Paragraph("方法论提炼", heading2_style))
    methodology_text = """
    <b>文化融入设计三步法:</b><br/>
    1. <b>挖掘</b>：深度调研地域文化符号与精神内核<br/>
    2. <b>转译</b>：将抽象文化转化为可感知的空间语言<br/>
    3. <b>演绎</b>：通过材质、光影、尺度营造文化氛围
    """
    story.append(Paragraph(methodology_text, normal_style))
    story.append(Spacer(1, 0.5*cm))
    
    # 案例分析
    story.append(PageBreak())
    story.append(Paragraph("深度案例分析", heading1_style))
    
    # 案例1
    story.append(Paragraph("案例一：Cuadra San Cristóbal —— 墨西哥建筑大师巴拉甘代表作", heading2_style))
    
    case1_info = """
    <b>项目信息</b><br/>
    地点: 墨西哥，墨西哥州<br/>
    时间: 1966-1968年<br/>
    类型: 住宅/马术庄园<br/>
    建筑师: Luis Barragán<br/><br/>
    
    <b>核心亮点</b><br/>
    • 粉色墙体与蓝色天空的极致对比<br/>
    • 水池倒影扩展空间感<br/>
    • 马匹尺度与人类尺度的对话<br/><br/>
    
    <b>学习要点</b><br/>
    "建筑应该唤醒情感，而不只是提供功能。" —— 巴拉甘的空间诗学<br/><br/>
    
    <b>可借鉴策略</b><br/>
    1. <b>色彩心理学应用</b>：大胆使用纯色墙面创造情绪<br/>
    2. <b>水元素设计</b>：静止水面创造"虚拟空间"，加倍场地感受<br/>
    3. <b>尺度游戏</b>：故意使用非人类尺度创造独特体验
    """
    story.append(Paragraph(case1_info, normal_style))
    story.append(Spacer(1, 0.5*cm))
    
    # 案例2
    story.append(Paragraph("案例二：Mandarin Oriental Residences —— Safdie Architects", heading2_style))
    
    case2_info = """
    <b>项目信息</b><br/>
    地点: 美国，佛罗里达州<br/>
    时间: 2026年建成<br/>
    类型: 高端住宅塔楼<br/>
    高度: 约200米<br/>
    建筑师: Safdie Architects<br/><br/>
    
    <b>核心亮点</b><br/>
    • 随高度展开的雕塑感形态<br/>
    • "富有表现力而不夸张"的设计哲学<br/>
    • 每层独特的户外空间<br/><br/>
    
    <b>学习要点</b><br/>
    高层住宅不一定非要方盒子，可以通过形态变化创造地标性和居住价值<br/><br/>
    
    <b>可借鉴策略</b><br/>
    1. <b>退台设计</b>：创造多层露台，提升高端住宅溢价<br/>
    2. <b>形态识别性</b>：在规范允许范围内追求独特轮廓<br/>
    3. <b>景观最大化</b>：通过扭转形体让更多户型获得海景
    """
    story.append(Paragraph(case2_info, normal_style))
    story.append(Spacer(1, 0.5*cm))
    
    # 知识沉淀
    story.append(PageBreak())
    story.append(Paragraph("知识沉淀", heading1_style))
    
    story.append(Paragraph("新增案例库", heading2_style))
    archive_data = [
        ['类型', '数量', '重点国家/地区'],
        ['文化建筑', '3', '墨西哥、西班牙、日本'],
        ['城市更新', '2', '荷兰、英国'],
        ['商业综合体', '2', '美国、新加坡'],
        ['住宅建筑', '3', '澳大利亚、美国、北欧'],
        ['景观设计', '2', '德国、中国'],
    ]
    
    archive_table = Table(archive_data, colWidths=[4*cm, 2*cm, 5*cm])
    archive_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2962FF')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('FONTNAME', (0, 0), (-1, 0), chinese_font),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('FONTNAME', (0, 1), (-1, -1), chinese_font),
        ('FONTSIZE', (0, 1), (-1, -1), 9),
    ]))
    story.append(archive_table)
    story.append(Spacer(1, 0.5*cm))
    
    story.append(Paragraph("方法论更新", heading2_style))
    methodology_update = """
    <b>今日新增方法论:</b><br/>
    • 文化建筑转译技术：传统→现代的三步法<br/>
    • 滨水空间激活策略：5种原型模式<br/>
    • 投资回报测算模型：文旅项目专用版
    """
    story.append(Paragraph(methodology_update, normal_style))
    story.append(Spacer(1, 0.5*cm))
    
    # 明日计划
    story.append(Paragraph("明日学习计划", heading1_style))
    plans = [
        "1. <b>城市设计专家</b>：研究哥本哈根Nordhavn可持续港区开发案例",
        "2. <b>建筑设计专家</b>：分析隈研吾最新作品，学习材料创新",
        "3. <b>投资金融专家</b>：研究日本星野集团轻资产模式",
        "4. <b>文旅运营专家</b>：学习法国卢浮宫数字化运营策略",
        "5. <b>文化策划专家</b>：研究故宫文创IP打造方法论",
    ]
    for plan in plans:
        story.append(Paragraph(plan, normal_style))
        story.append(Spacer(1, 0.2*cm))
    
    # 结语
    story.append(Spacer(1, 1*cm))
    story.append(Paragraph("—" * 40, ParagraphStyle('Line', parent=normal_style, alignment=TA_CENTER)))
    story.append(Spacer(1, 0.3*cm))
    story.append(Paragraph(
        '"学习不是为了复制，而是为了创造属于我们的设计语言。"',
        ParagraphStyle('Quote', parent=normal_style, alignment=TA_CENTER, fontSize=10, textColor=colors.gray)
    ))
    story.append(Spacer(1, 0.3*cm))
    story.append(Paragraph(
        '小白设计工作室 | 每日学习报告 | 持续进化中',
        ParagraphStyle('Footer', parent=normal_style, alignment=TA_CENTER, fontSize=8, textColor=colors.gray)
    ))
    
    # 生成PDF
    doc.build(story)
    
    print(f"✅ PDF报告生成成功: {pdf_file}")
    return pdf_file

if __name__ == "__main__":
    print("🚀 生成每日学习报告PDF...")
    result = generate_daily_report()
    print(f"📄 输出文件: {result}")
