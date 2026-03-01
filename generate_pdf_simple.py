#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生成案例分享PDF文件 - 简化版"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
import os

def create_pdf():
    doc = SimpleDocTemplate(
        "/home/codespace/.openclaw/workspace/案例分享_2026-02-28.pdf",
        pagesize=A4,
        rightMargin=2*cm,
        leftMargin=2*cm,
        topMargin=2*cm,
        bottomMargin=2*cm
    )
    
    styles = getSampleStyleSheet()
    font_name = 'Helvetica'
    
    title_style = ParagraphStyle(
        'Title', parent=styles['Heading1'], fontName=font_name,
        fontSize=24, textColor=colors.HexColor('#2C3E50'),
        spaceAfter=30, alignment=TA_CENTER
    )
    
    h1_style = ParagraphStyle(
        'H1', parent=styles['Heading1'], fontName=font_name,
        fontSize=18, textColor=colors.HexColor('#E67E22'),
        spaceAfter=12, spaceBefore=12
    )
    
    h2_style = ParagraphStyle(
        'H2', parent=styles['Heading2'], fontName=font_name,
        fontSize=14, textColor=colors.HexColor('#3498DB'),
        spaceAfter=10, spaceBefore=10
    )
    
    normal_style = ParagraphStyle(
        'Normal', parent=styles['Normal'], fontName=font_name,
        fontSize=11, leading=16, spaceAfter=8
    )
    
    story = []
    
    # 标题
    story.append(Paragraph("Case Study Sharing - Tourism & Cultural Planning", title_style))
    story.append(Paragraph("12Agent Team Learning Report 2026-02-28", normal_style))
    story.append(Spacer(1, 0.5*cm))
    
    # 概览
    story.append(Paragraph("Overview", h1_style))
    story.append(Paragraph("6 selected cases covering: Mixed-use Complex, Tourism Architecture, Landscape Bridge, Rural Tourism, Master Works", normal_style))
    story.append(Spacer(1, 0.3*cm))
    
    # 案例表格
    data = [
        ['No.', 'Case Name', 'Location', 'Type', 'Value'],
        ['1', 'Huzhou Daixi Mixed-use', 'Zhejiang', 'Mixed-use', '5 stars'],
        ['2', 'Guan Shan Jian Ji', 'Changbai Mt.', 'Tourism', '4 stars'],
        ['3', 'Dali 3D Printed Bridge', 'Yunnan', 'Landscape', '4 stars'],
        ['4', 'Ying Xiang Nan Ping', 'Huangshan', 'Rural', '4 stars'],
        ['5', 'MVRDV Fusion Center', 'Armenia', 'Landmark', '5 stars'],
        ['6', 'DKC Theater', 'Moscow', 'Culture', '4 stars'],
    ]
    
    table = Table(data, colWidths=[1.2*cm, 4.5*cm, 3*cm, 3*cm, 2*cm])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#3498DB')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, -1), font_name),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
        ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#F8F9FA')),
        ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#BDC3C7')),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#F8F9FA')])
    ]))
    story.append(table)
    story.append(Spacer(1, 0.5*cm))
    
    # 重点案例
    story.append(Paragraph("Featured Case Details", h1_style))
    
    story.append(Paragraph("Case 1: Huzhou Daixi Mixed-use Complex", h2_style))
    story.append(Paragraph("Location: Zhejiang Huzhou | Designer: Mi Zhang Architecture", normal_style))
    story.append(Paragraph("Type: Cultural + Commercial Mixed-use | Value: 5 stars", normal_style))
    story.append(Spacer(1, 0.2*cm))
    story.append(Paragraph("Concept: Abstract Landscape and Concrete City", normal_style))
    story.append(Paragraph("Key Learnings:", normal_style))
    story.append(Paragraph("- Mixed-use functional organization strategy", normal_style))
    story.append(Paragraph("- Zhejiang regional cultural expression", normal_style))
    story.append(Paragraph("- Waterfront architecture handling", normal_style))
    story.append(Paragraph("- Modern language with traditional spirit", normal_style))
    story.append(Spacer(1, 0.3*cm))
    
    story.append(Paragraph("Case 2: Guan Shan Jian Ji - Changbai Mountain", h2_style))
    story.append(Paragraph("Location: Jilin Changbai Mountain | Type: Tourism Architecture", normal_style))
    story.append(Paragraph("Concept: Prism Shelter at the foot of Changbai Mountain", normal_style))
    story.append(Paragraph("Key Learnings:", normal_style))
    story.append(Paragraph("- Architecture in natural environment", normal_style))
    story.append(Paragraph("- Shelter concept and hotel design", normal_style))
    story.append(Paragraph("- Tourism project spatial experience", normal_style))
    story.append(Spacer(1, 0.3*cm))
    
    story.append(Paragraph("Case 3: Dali Wanhua Creek 3D Printed Bridge", h2_style))
    story.append(Paragraph("Location: Yunnan Dali | Innovation: First 3D printed bridge in Yunnan", normal_style))
    story.append(Paragraph("Key Learnings:", normal_style))
    story.append(Paragraph("- New technology application (3D printing)", normal_style))
    story.append(Paragraph("- Landscape bridge design", normal_style))
    story.append(Paragraph("- Tradition meets digital manufacturing", normal_style))
    story.append(Spacer(1, 0.3*cm))
    
    # Master work
    story.append(Paragraph("Master Works Study", h1_style))
    story.append(Paragraph("Case 5: MVRDV Fusion Center Concept", h2_style))
    story.append(Paragraph("Location: Armenia | Designer: MVRDV (International Master)", normal_style))
    story.append(Paragraph("Concept: An Ark overlooking the distant view", normal_style))
    story.append(Paragraph("Master Techniques:", normal_style))
    story.append(Paragraph("- Landmark building shaping methods", normal_style))
    story.append(Paragraph("- Concept presentation skills", normal_style))
    story.append(Paragraph("- International cutting-edge design ideas", normal_style))
    story.append(Spacer(1, 0.3*cm))
    
    # 学习总结
    story.append(Paragraph("Summary and Plan", h1_style))
    
    story.append(Paragraph("Today's Learning Data:", h2_style))
    data2 = [
        ['Metric', 'Value'],
        ['Study Time', '30 minutes'],
        ['Cases Collected', '6'],
        ['Deep Study', '1 (Huzhou Daixi)'],
        ['Team', 'Urban + Architecture'],
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
    ]))
    story.append(table2)
    story.append(Spacer(1, 0.3*cm))
    
    story.append(Paragraph("Key Findings:", h2_style))
    story.append(Paragraph("1. Zhejiang local projects have high value - directly relevant to Di Dang Lake project", normal_style))
    story.append(Paragraph("2. Abstract Landscape concept - can be used as cultural expression technique", normal_style))
    story.append(Paragraph("3. Mixed-use model - need deep study of spatial organization", normal_style))
    story.append(Spacer(1, 0.3*cm))
    
    story.append(Paragraph("Next Steps:", h2_style))
    story.append(Paragraph("□ Deep analysis of Huzhou Daixi floor plans", normal_style))
    story.append(Paragraph("□ Study other works by Mi Zhang Architecture", normal_style))
    story.append(Paragraph("□ Summarize Abstract Landscape design techniques", normal_style))
    story.append(Paragraph("□ Build mixed-use design pattern library", normal_style))
    story.append(Spacer(1, 0.5*cm))
    
    # 底部信息
    story.append(Spacer(1, 1*cm))
    story.append(Paragraph("- 12Agent Tourism & Cultural Planning Design Team -", normal_style))
    story.append(Paragraph("Data Source: Gooood.cn | Generated: 2026-02-28", normal_style))
    
    doc.build(story)
    print("PDF generated successfully: /home/codespace/.openclaw/workspace/案例分享_2026-02-28.pdf")

if __name__ == '__main__':
    create_pdf()
