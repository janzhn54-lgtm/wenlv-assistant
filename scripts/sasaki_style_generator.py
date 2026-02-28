#!/usr/bin/env python3
"""
Sasaki风格分析图自动生成器 V1.0
学习Sasaki设计美学，生成专业级分析图
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Circle, Rectangle, Polygon
import numpy as np

# Sasaki风格配色方案
SASAKI = {
    'bg': '#FAFAFA',
    'water': '#B8D4E3',
    'green_light': '#C8D6AF',
    'green_dark': '#7A9B76',
    'grey': '#9B9B9B',
    'dark': '#4A4A4A',
    'accent': '#E67E22',
    'text': '#2C3E50',
}

def sasaki_style_init():
    """初始化Sasaki风格配置"""
    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['axes.facecolor'] = SASAKI['bg']
    plt.rcParams['figure.facecolor'] = SASAKI['bg']
    plt.rcParams['axes.spines.top'] = False
    plt.rcParams['axes.spines.right'] = False
    plt.rcParams['axes.spines.left'] = False
    plt.rcParams['axes.spines.bottom'] = False
    plt.rcParams['axes.grid'] = False

class SasakiDiagramGenerator:
    """Sasaki风格分析图生成器"""
    
    @staticmethod
    def site_context_map():
        """区位分析图 - Sasaki风格"""
        fig, ax = plt.subplots(figsize=(10, 8))
        
        # 背景
        ax.set_facecolor(SASAKI['bg'])
        
        # 绘制基地位置（强调色）
        site = Circle((50, 50), 8, facecolor=SASAKI['accent'], edgecolor='white', linewidth=2)
        ax.add_patch(site)
        
        # 绘制周边区域（低饱和度）
        for i in range(5):
            for j in range(5):
                if abs(i-2) + abs(j-2) > 1:
                    rect = Rectangle((20+i*15, 20+j*15), 12, 12, 
                                    facecolor=SASAKI['grey'], alpha=0.3, edgecolor='white')
                    ax.add_patch(rect)
        
        # 绘制交通网络
        for i in range(3):
            ax.plot([10, 90], [30+i*20, 30+i*20], color=SASAKI['dark'], linewidth=1, alpha=0.5)
            ax.plot([30+i*20, 30+i*20], [10, 90], color=SASAKI['dark'], linewidth=1, alpha=0.5)
        
        # 标注
        ax.text(50, 50, 'SITE', ha='center', va='center', fontsize=12, fontweight='bold', color='white')
        ax.text(50, 8, 'Site Context Analysis', ha='center', fontsize=14, fontweight='bold', color=SASAKI['text'])
        
        ax.set_xlim(0, 100)
        ax.set_ylim(0, 100)
        ax.set_aspect('equal')
        ax.axis('off')
        
        plt.tight_layout()
        plt.savefig('images/sasaki_style/context_map.png', dpi=150, bbox_inches='tight', facecolor=SASAKI['bg'])
        plt.close()
        print("✅ Sasaki风格区位分析图已生成")
    
    @staticmethod
    def spatial_structure_diagram():
        """空间结构分析图"""
        fig, ax = plt.subplots(figsize=(10, 8))
        ax.set_facecolor(SASAKI['bg'])
        
        # 绘制轴线
        ax.plot([20, 80], [50, 50], color=SASAKI['accent'], linewidth=3, alpha=0.7, label='Primary Axis')
        ax.plot([50, 50], [20, 80], color=SASAKI['accent'], linewidth=2, alpha=0.5, linestyle='--', label='Secondary Axis')
        
        # 绘制节点
        nodes = [(30, 50), (50, 50), (70, 50), (50, 30), (50, 70)]
        for i, (x, y) in enumerate(nodes):
            circle = Circle((x, y), 4, facecolor=SASAKI['green_dark'], edgecolor='white', linewidth=2)
            ax.add_patch(circle)
            ax.text(x, y, f'N{i+1}', ha='center', va='center', fontsize=9, fontweight='bold', color='white')
        
        # 绘制区域
        for i, (x, y, label) in enumerate([(25, 75, 'Zone A'), (75, 75, 'Zone B'), (25, 25, 'Zone C'), (75, 25, 'Zone D')]):
            rect = FancyBboxPatch((x-8, y-8), 16, 16, boxstyle="round,pad=0.02", 
                                 facecolor=SASAKI['green_light'], edgecolor=SASAKI['green_dark'], alpha=0.5)
            ax.add_patch(rect)
            ax.text(x, y, label, ha='center', va='center', fontsize=8, color=SASAKI['dark'])
        
        ax.text(50, 5, 'Spatial Structure Diagram', ha='center', fontsize=14, fontweight='bold', color=SASAKI['text'])
        
        ax.set_xlim(0, 100)
        ax.set_ylim(0, 100)
        ax.set_aspect('equal')
        ax.axis('off')
        
        plt.tight_layout()
        plt.savefig('images/sasaki_style/spatial_structure.png', dpi=150, bbox_inches='tight', facecolor=SASAKI['bg'])
        plt.close()
        print("✅ Sasaki风格空间结构图已生成")
    
    @staticmethod
    def zoning_plan():
        """功能分区图"""
        fig, ax = plt.subplots(figsize=(10, 8))
        ax.set_facecolor(SASAKI['bg'])
        
        # 分区数据
        zones = [
            ('Residential', 20, 60, 25, 30, SASAKI['green_light']),
            ('Commercial', 55, 60, 25, 30, SASAKI['water']),
            ('Public', 20, 25, 25, 25, SASAKI['accent']),
            ('Green', 55, 25, 25, 25, SASAKI['green_dark']),
        ]
        
        for label, x, y, w, h, color in zones:
            rect = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02",
                                 facecolor=color, edgecolor='white', linewidth=2, alpha=0.7)
            ax.add_patch(rect)
            ax.text(x+w/2, y+h/2, label, ha='center', va='center', fontsize=10, fontweight='bold', color='white')
        
        # 图例
        legend_y = 8
        for i, (label, _, _, _, _, color) in enumerate(zones):
            rect = Rectangle((15+i*20, legend_y), 3, 3, facecolor=color, edgecolor='white')
            ax.add_patch(rect)
            ax.text(19+i*20, legend_y+1.5, label, ha='left', va='center', fontsize=8, color=SASAKI['text'])
        
        ax.text(50, 95, 'Functional Zoning Plan', ha='center', fontsize=14, fontweight='bold', color=SASAKI['text'])
        
        ax.set_xlim(0, 100)
        ax.set_ylim(0, 100)
        ax.set_aspect('equal')
        ax.axis('off')
        
        plt.tight_layout()
        plt.savefig('images/sasaki_style/zoning_plan.png', dpi=150, bbox_inches='tight', facecolor=SASAKI['bg'])
        plt.close()
        print("✅ Sasaki风格功能分区图已生成")

if __name__ == "__main__":
    print("🎨 Sasaki风格分析图生成器")
    print("=" * 50)
    
    # 创建目录
    import os
    os.makedirs('images/sasaki_style', exist_ok=True)
    
    # 初始化风格
    sasaki_style_init()
    
    # 生成分析图
    generator = SasakiDiagramGenerator()
    generator.site_context_map()
    generator.spatial_structure_diagram()
    generator.zoning_plan()
    
    print("=" * 50)
    print("✅ 所有Sasaki风格分析图生成完成！")
    print("📁 保存位置: images/sasaki_style/")
