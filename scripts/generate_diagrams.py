import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import Rectangle, FancyBboxPatch
import numpy as np

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

fig, axes = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle('Alila Wuzhen - Spatial Analysis Diagrams', fontsize=16, fontweight='bold')

# 1. 总平面示意
ax1 = axes[0, 0]
ax1.set_xlim(0, 100)
ax1.set_ylim(0, 100)
ax1.set_aspect('equal')

# 绘制建筑体块
for i in range(3):
    for j in range(4):
        rect = Rectangle((10+i*25, 10+j*20), 15, 12, 
                         facecolor='#f5f5f5', edgecolor='#333', linewidth=1)
        ax1.add_patch(rect)

# 绘制水院
water = patches.Circle((50, 50), 15, facecolor='#e8f4f8', edgecolor='#4682b4', linewidth=2)
ax1.add_patch(water)

# 绘制流线
ax1.plot([5, 50], [50, 50], 'k--', alpha=0.5, linewidth=1)
ax1.annotate('Entry', xy=(5, 50), fontsize=8)
ax1.annotate('Water Court', xy=(45, 65), fontsize=8)

ax1.set_title('Site Plan Concept', fontsize=11, fontweight='bold')
ax1.axis('off')

# 2. 空间序列分析
ax2 = axes[0, 1]
ax2.set_xlim(0, 10)
ax2.set_ylim(0, 10)

# 序列节点
sequence = ['Entry\n(Narrow)', 'Transition', 'Water Court\n(Open)']
colors_seq = ['#d3d3d3', '#e8e8e8', '#87ceeb']
y_pos = [8, 5, 2]

for i, (label, color, y) in enumerate(zip(sequence, colors_seq, y_pos)):
    rect = FancyBboxPatch((2, y-0.8), 6, 1.5, 
                          boxstyle="round,pad=0.1",
                          facecolor=color, edgecolor='#333', linewidth=1)
    ax2.add_patch(rect)
    ax2.text(5, y, label, ha='center', va='center', fontsize=9, fontweight='bold')
    
    if i < len(sequence) - 1:
        ax2.annotate('', xy=(5, y_pos[i+1]+0.8), xytext=(5, y-0.8),
                    arrowprops=dict(arrowstyle='->', color='#333', lw=1.5))

ax2.set_title('Spatial Sequence Analysis', fontsize=11, fontweight='bold')
ax2.axis('off')

# 3. 色彩分析
ax3 = axes[1, 0]
ax3.set_xlim(0, 10)
ax3.set_ylim(0, 10)

colors_analysis = [
    ('#f5f5f5', 'White Wall\n70%', 8),
    ('#4a4a4a', 'Dark Grey Roof\n20%', 5),
    ('#8b4513', 'Wood Accent\n7%', 3),
    ('#228b22', 'Green Plant\n3%', 1),
]

for color, label, y in colors_analysis:
    rect = Rectangle((2, y-0.8), 6, 1.5, facecolor=color, edgecolor='#333', linewidth=1)
    ax3.add_patch(rect)
    ax3.text(5, y, label, ha='center', va='center', fontsize=9, 
             color='white' if color in ['#4a4a4a', '#8b4513', '#228b22'] else 'black',
             fontweight='bold')

ax3.set_title('Color Palette Analysis', fontsize=11, fontweight='bold')
ax3.axis('off')

# 4. 功能布局
ax4 = axes[1, 1]
ax4.set_xlim(0, 100)
ax4.set_ylim(0, 100)

# 功能分区
zones = [
    ('Guest Rooms', 10, 70, 35, 25, '#e8f4f8'),
    ('Public Area', 50, 70, 40, 25, '#f0f8e8'),
    ('Water Court', 45, 35, 30, 30, '#d4e8f0'),
    ('Back of House', 10, 10, 80, 20, '#f5f5f5'),
]

for name, x, y, w, h, color in zones:
    rect = Rectangle((x, y), w, h, facecolor=color, edgecolor='#666', 
                     linewidth=1, alpha=0.7)
    ax4.add_patch(rect)
    ax4.text(x+w/2, y+h/2, name, ha='center', va='center', 
             fontsize=8, fontweight='bold')

ax4.set_title('Functional Zoning', fontsize=11, fontweight='bold')
ax4.axis('off')

plt.tight_layout()
plt.savefig('/home/codespace/.openclaw/workspace/images/alila_wuzhen_analysis.png', 
            dpi=150, bbox_inches='tight', facecolor='white')
plt.close()

print("✅ 分析图生成成功: images/alila_wuzhen_analysis.png")
