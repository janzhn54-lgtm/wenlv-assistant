import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Circle, Rectangle, Polygon
import numpy as np

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

# 创建图纸
fig = plt.figure(figsize=(16, 12))

# 1. 用地分析图
ax1 = plt.subplot(2, 2, 1)
ax1.set_xlim(0, 100)
ax1.set_ylim(0, 80)

# 绘制用地边界（示意）
land = Polygon([(20, 20), (80, 20), (85, 60), (60, 70), (20, 60)], 
               closed=True, fill=True, facecolor='lightblue', edgecolor='blue', linewidth=2)
ax1.add_patch(land)

# 标注
ax1.text(50, 45, '一期用地\n(已获取)', ha='center', va='center', fontsize=12, fontweight='bold')
ax1.text(50, 10, '迪荡湖', ha='center', va='center', fontsize=10, color='blue')
ax1.text(90, 45, '云江路', ha='center', va='center', fontsize=10, rotation=90)
ax1.text(50, 75, '北', ha='center', va='center', fontsize=10)

# 指北针
ax1.annotate('N', xy=(85, 75), fontsize=14, ha='center', 
            bbox=dict(boxstyle='circle', facecolor='white', edgecolor='black'))

ax1.set_title('Project Location\n(项目位置示意图)', fontsize=14, fontweight='bold')
ax1.set_aspect('equal')
ax1.axis('off')

# 2. 限制因素分析图
ax2 = plt.subplot(2, 2, 2)
ax2.set_xlim(0, 10)
ax2.set_ylim(0, 10)

# 绘制限制因素
factors = [
    ('Waterfront Height\nLimit: 24m', 5, 8, 'red', 0.8),
    ('Metro Line 5\nProtection Zone', 5, 6, 'orange', 0.6),
    ('Mixed Land Use\nComplexity', 5, 4, 'yellow', 0.5),
    ('Environmental\nAssessment', 5, 2, 'orange', 0.6),
]

for text, x, y, color, risk in factors:
    box = FancyBboxPatch((x-2, y-0.8), 4, 1.6, 
                         boxstyle="round,pad=0.1", 
                         facecolor=color, alpha=risk,
                         edgecolor='black', linewidth=1)
    ax2.add_patch(box)
    ax2.text(x, y, text, ha='center', va='center', fontsize=9, fontweight='bold')

ax2.set_title('Risk Analysis\n(限制因素分析)', fontsize=14, fontweight='bold')
ax2.set_xlim(0, 10)
ax2.set_ylim(0, 10)
ax2.axis('off')

# 3. 布局策略建议图
ax3 = plt.subplot(2, 2, 3)
ax3.set_xlim(0, 100)
ax3.set_ylim(0, 80)

# 用地边界
land = Polygon([(20, 20), (80, 20), (85, 60), (60, 70), (20, 60)], 
               closed=True, fill=True, facecolor='lightgray', edgecolor='black', linewidth=1)
ax3.add_patch(land)

# 酒店（临湖低层）
hotel = Rectangle((25, 25), 30, 15, facecolor='lightcoral', edgecolor='red', linewidth=2)
ax3.add_patch(hotel)
ax3.text(40, 32, 'Hotel\n(≤4F, ≤24m)', ha='center', va='center', fontsize=9, color='white', fontweight='bold')

# 住宅（内部高层）
residential = Rectangle((60, 35), 20, 25, facecolor='lightgreen', edgecolor='green', linewidth=2)
ax3.add_patch(residential)
ax3.text(70, 47, 'Residential\n(≤18F, ≤60m)', ha='center', va='center', fontsize=9, color='darkgreen', fontweight='bold')

# 绿地
park1 = Circle((35, 55), 8, facecolor='lightgreen', edgecolor='green', alpha=0.5)
ax3.add_patch(park1)
ax3.text(35, 55, 'Park', ha='center', va='center', fontsize=8)

# 标注
ax3.text(50, 10, 'Lake', ha='center', va='center', fontsize=10, color='blue')
ax3.annotate('', xy=(50, 18), xytext=(50, 12),
            arrowprops=dict(arrowstyle='->', color='blue', lw=2))

ax3.set_title('Layout Strategy\n(布局策略建议)', fontsize=14, fontweight='bold')
ax3.set_aspect('equal')
ax3.axis('off')

# 4. 指标对比图
ax4 = plt.subplot(2, 2, 4)

categories = ['Plot\nRatio', 'Building\nDensity', 'Green\nRate', 'Height\nLimit']
standard = [2.5, 40, 25, 60]  # 标准值
proposed = [2.0, 32, 30, 60]  # 建议值

x = np.arange(len(categories))
width = 0.35

bars1 = ax4.bar(x - width/2, standard, width, label='Standard Max', color='lightblue', alpha=0.7)
bars2 = ax4.bar(x + width/2, proposed, width, label='Proposed', color='darkblue', alpha=0.8)

ax4.set_ylabel('Value')
ax4.set_title('Planning Indicators\n(规划指标对比)', fontsize=14, fontweight='bold')
ax4.set_xticks(x)
ax4.set_xticklabels(categories)
ax4.legend()
ax4.grid(axis='y', alpha=0.3)

# 添加数值标签
for bar in bars1:
    height = bar.get_height()
    ax4.annotate(f'{height}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),
                textcoords="offset points",
                ha='center', va='bottom', fontsize=9)

for bar in bars2:
    height = bar.get_height()
    ax4.annotate(f'{height}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),
                textcoords="offset points",
                ha='center', va='bottom', fontsize=9)

plt.tight_layout()
plt.savefig('/home/codespace/.openclaw/workspace/projects/迪荡湖酒店住宅项目/01_规划法规分析图.png', dpi=150, bbox_inches='tight', facecolor='white')
plt.close()

print("✅ 规划法规分析图已生成")
