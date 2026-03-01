#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""生成案例分享PDF文件""

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.enums import TA_CENTER, TA_LEFT
import os

def create_pdf():
    # 尝试注册中文字体
    font_paths = [
        '/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc',
        '/usr/share/fonts/truetype/wqy/wqy-microhei.ttc',
        '/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc',
        '/usr/share/fonts/truetype/noto/NotoSansCJK-Regular.ttc',
    ]
    
    font_registered = False
    for font_path in font_paths:
        if os.path.exists(font_path):
            try:
                pdfmetrics.registerFont(TTFont('ChineseFont', font_path))
                font_registered = True
                print(f"已注册字体: {font_path}")
                break
            except:
                continue
    
    if not font_registered:
        print("警告: 未找到中文字体，将使用默认字体")
        font_name = 'Helvetica'
    else:
        font_name = 'ChineseFont'
    
    # 创建PDF文档
    doc = SimpleDocTemplate(
        "/home/codespace/.openclaw/workspace/案例分享_2026-02-28.pdf",
        pagesize=A4,
        rightMargin=2*cm,
        leftMargin=2*cm,
        topMargin=2*cm,
        bottomMargin=2*cm
    )
    
    # 样式
    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontName=font_name,
        fontSize=24,
        textColor=colors.HexColor('#2C3E50'),
        spaceAfter=30,
        alignment=TA_CENTER
    )
    
    heading1_style = ParagraphStyle(
        'CustomH1',
        parent=styles['Heading1'],
        fontName=font_name,
        fontSize=18,
        textColor=colors.HexColor('#E67E22'),
        spaceAfter=12,
        spaceBefore=12
    )
    
    heading2_style = ParagraphStyle(
        'CustomH2',
        parent=styles['Heading2'],
        fontName=font_name,
        fontSize=14,
        textColor=colors.HexColor('#3498DB'),
        spaceAfter=10,
        spaceBefore=10
    )
    
    normal_style = ParagraphStyle(
        'CustomNormal',
        parent=styles['Normal'],
        fontName=font_name,
        fontSize=11,
        leading=16,
        spaceAfter=8
    )
    
    # 构建内容
    story = []
    
    # 标题
    story.append(Paragraph("文旅规划设计案例分享", title_style))
    story.append(Paragraph("12Agent团队学习成果 2026-02-28", normal_style))
    story.append(Spacer(1, 0.5*cm))
    
    # 概览
    story.append(Paragraph("案例概览", heading1_style))
    story.append(Paragraph("本次分享精选6个国内外优秀案例，涵盖：文商综合体、文旅建筑、景观桥梁、乡村文旅、大师作品", normal_style))
    story.append(Spacer(1, 0.3*cm))
    
    # 案例表格
    data = [
        ['序号', '案例名称', '地点', '类型', '学习价值'],
        ['1', '湖州埭溪文商综合体', '浙江湖州', '文商综合体', '⭐⭐⭐⭐⭐'],
        ['2', '观山见己', '吉林长白山', '文旅建筑', '⭐⭐⭐⭐'],
        ['3', '大理万花溪3D打印桥', '云南大理', '景观桥梁', '⭐⭐⭐⭐'],
        ['4', '影像南屏', '安徽黄山', '乡村文旅', '⭐⭐⭐⭐'],
        ['5', 'MVRDV融合中心', '亚美尼亚', '地标建筑', '⭐⭐⭐⭐⭐'],
        ['6', 'DKC工程剧场', '莫斯科', '文化建筑', '⭐⭐⭐⭐'],
    ]
    
    table = Table(data, colWidths=[1.5*cm, 4*cm, 3*cm, 3*cm, 2.5*cm])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#3498DB')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, -1), font_name),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#F8F9FA')),
        ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#BDC3C7')),
        ('FONTNAME', (0, 1), (-1, -1), font_name),
        ('FONTSIZE', (0, 1), (-1, -1), 9),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#F8F9FA')])
    ]))
    story.append(table)
    story.append(Spacer(1, 0.5*cm))
    
    # 重点案例详解
    story.append(PageBreak())
    story.append(Paragraph("重点案例详解", heading1_style))
    
    # 案例1
    story.append(Paragraph("案例1：湖州埭溪文商综合体", heading2_style))
    story.append(Paragraph("<b>项目信息</b>", normal_style))
    story.append(Paragraph("• 地点：浙江湖州 | 设计：米丈建筑 | 类型：文化+商业综合体", normal_style))
    story.append(Paragraph("• 学习价值：⭐⭐⭐⭐⭐ (与迪荡湖项目高度相关)", normal_style))
    story.append(Spacer(1, 0.2*cm))
    story.append(Paragraph("<b>设计理念</b>", normal_style))
    story.append(Paragraph('"抽象山水与具象城市" —— 浙江本土项目的地域性设计', normal_style))
    story.append(Spacer(1, 0.2*cm))
    story.append(Paragraph("<b>可借鉴点</b>", normal_style))
    story.append(Paragraph("• 文商综合体的功能组织策略", normal_style))
    story.append(Paragraph("• 浙江地域文化表达方式", normal_style))
    story.append(Paragraph("• 临水建筑的处理手法", normal_style))
    story.append(Paragraph("• 现代建筑语言与传统意境结合", normal_style))
    story.append(Spacer(1, 0.3*cm))
    
    # 案例2
    story.append(Paragraph("案例2：观山见己 - 长白山文旅建筑", heading2_style))
    story.append(Paragraph("<b>项目信息</b>", normal_style))
    story.append(Paragraph("• 地点：吉林长白山 | 设计：数石space10工作室", normal_style))
    story.append(Paragraph("• 类型：文旅建筑 | 标签：建筑、艺术、设计", normal_style))
    story.append(Spacer(1, 0.2*cm))
    story.append(Paragraph("<b>设计理念</b>", normal_style))
    story.append(Paragraph('"长白山脚下的棱镜庇护所" —— 自然环境中的建筑', normal_style))
    story.append(Spacer(1, 0.2*cm))
    story.append(Paragraph("<b>学习价值</b>", normal_style))
    story.append(Paragraph("• 自然环境中的建筑设计方法", normal_style))
    story.append(Paragraph("• "庇护所"概念与酒店设计的关联", normal_style))
    story.append(Paragraph("• 文旅项目的空间体验营造", normal_style))
    story.append(Spacer(1, 0.3*cm))
    
    # 案例3
    story.append(Paragraph("案例3：大理万花溪3D打印步行桥", heading2_style))
    story.append(Paragraph("<b>项目信息</b>", normal_style))
    story.append(Paragraph("• 地点：云南大理 | 创新点：云南第一座3D打印步行桥", normal_style))
    story.append(Paragraph("• 设计：和畔皓森 + ORS Studio", normal_style))
    story.append(Spacer(1, 0.2*cm))
    story.append(Paragraph("<b>技术亮点</b>", normal_style))
    story.append(Paragraph("• 新技术应用（3D打印）", normal_style))
    story.append(Paragraph("• 景观桥设计与文旅小镇配套", normal_style))
    story.append(Paragraph("• 传统工艺与数字制造的结合", normal_style))
    story.append(Spacer(1, 0.3*cm))
    
    # 大师案例
    story.append(PageBreak())
    story.append(Paragraph("大师作品学习", heading1_style))
    
    story.append(Paragraph("案例5：MVRDV融合中心概念方案", heading2_style))
    story.append(Paragraph("<b>项目信息</b>", normal_style))
    story.append(Paragraph("• 地点：亚美尼亚 | 设计：MVRDV（国际大师）", normal_style))
    story.append(Paragraph("• 概念：一座可眺望远景的"方舟", normal_style))
    story.append(Spacer(1, 0.2*cm))
    story.append(Paragraph("<b>大师手法学习</b>", normal_style))
    story.append(Paragraph("• 地标性建筑的塑造方法", normal_style))
    story.append(Paragraph("• 概念方案的表达技巧", normal_style))
    story.append(Paragraph("• 国际前沿设计理念", normal_style))
    story.append(Spacer(1, 0.3*cm))
    
    # 学习总结
    story.append(Paragraph("学习总结与计划", heading1_style))
    
    story.append(Paragraph("<b>今日学习数据</b>", heading2_style))
    data2 = [
        ['指标', '数值'],
        ['学习时间', '30分钟'],
        ['收集案例', '6个'],
        ['重点研究', '1个（湖州埭溪）'],
        ['学习团队', '城市设计+建筑设计'],
    ]
    table2 = Table(data2, colWidths=[6*cm, 8*cm])
    table2.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#7A9B76')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, -1), font_name),
        ('FONTSIZE', (0, 0), (-1, 0), 11),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
        ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#F8F9FA')),
        ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#BDC3C7')),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#F8F9FA')])
    ]))
    story.append(table2)
    story.append(Spacer(1, 0.3*cm))
    
    story.append(Paragraph("<b>关键发现</b>", heading2_style))
    story.append(Paragraph("1. 浙江本土项目价值高 —— 与迪荡湖项目有直接参考价值", normal_style))
    story.append(Paragraph("2. "抽象山水"概念 —— 可作为文化表达的手法", normal_style))
    story.append(Paragraph("3. 文商综合体模式 —— 需要深入研究空间组织", normal_style))
    story.append(Spacer(1, 0.3*cm))
    
    story.append(Paragraph("<b>下一步计划</b>", heading2_style))
    story.append(Paragraph("□ 深度分析湖州埭溪项目平面图", normal_style))
    story.append(Paragraph("□ 研究米丈建筑其他作品", normal_style))
    story.append(Paragraph("□ 总结"抽象山水"设计手法", normal_style))
    story.append(Paragraph("□ 建立文商综合体设计模式库", normal_style))
    story.append(Spacer(1, 0.5*cm))
    
    # 底部信息
    story.append(Spacer(1, 1*cm))
    story.append(Paragraph("— 12Agent文旅规划设计团队 —", normal_style))
    story.append(Paragraph("数据来源: 谷德设计网 | 生成时间: 2026-02-28", normal_style))
    
    # 生成PDF
    doc.build(story)
    print("PDF生成成功: /home/codespace/.openclaw/workspace/案例分享_2026-02-28.pdf")

if __name__ == '__main__':
    create_pdf()
