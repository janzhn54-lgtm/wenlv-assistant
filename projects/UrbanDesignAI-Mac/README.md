# UrbanDesignAI Mac App

## 🚀 快速开始

### 1. 创建Xcode项目

1. 打开 **Xcode** (需要macOS和Xcode installed)
2. 选择 **File → New → Project**
3. 选择 **macOS → App**
4. 填写项目信息：
   - **Product Name**: UrbanDesignAI
   - **Team**: 你的Apple ID
   - **Organization Identifier**: com.yourname (例如：com.zhengjian)
   - **Interface**: SwiftUI
   - **Language**: Swift

### 2. 添加文件

将本文件夹中的所有 `.swift` 文件拖入Xcode项目中：
- `UrbanDesignAIApp.swift`
- `Models.swift`
- `ContentView.swift`
- `InputMethodView.swift`
- `ParametersEditor.swift`
- `StyleSelector.swift`
- `OutputGallery.swift`
- `ImportView.swift`

### 3. 运行项目

按 **Cmd+R** 运行，或点击运行按钮。

---

## 📱 功能说明

### ✅ 已实现功能

1. **多种输入方式**
   - CAD文件 (.dwg, .dxf)
   - 图片 (.png, .jpg, .tiff)
   - GIS数据 (.shp, .geojson, .kml)
   - 拖放或文件选择器导入

2. **功能类型选择**
   - 文旅小镇
   - 住宅社区
   - 商业综合体
   - 办公园区
   - 混合开发
   - 产业园区

3. **规划参数调整**
   - 容积率 (0.5-5.0)
   - 建筑密度 (10-60%)
   - 绿化率 (10-50%)
   - 限高 (6-150m)
   - 停车标准

4. **设计风格选择**
   - 新中式、极简现代、地中海
   - 欧式古典、东南亚、工业风
   - 生态自然、科技未来

5. **顶尖设计团队**
   - 国内：MAD、GOA、蓝城、万科
   - 国际：BIG、Sasaki、SOM、Zaha Hadid、Kengo Kuma、WOHA、Snøhetta

6. **输出成果**
   - CAD平面图 (.dwg/.dxf)
   - 彩色平面图
   - 鸟瞰效果图
   - 人视效果图
   - 设计分析图
   - 设计说明文档

---

## 🏗️ 项目结构

```
UrbanDesignAI/
├── UrbanDesignAIApp.swift      # App入口
├── Models.swift                # 数据模型
├── ContentView.swift           # 主界面
├── InputMethodView.swift       # 输入模块
├── ParametersEditor.swift      # 参数编辑
├── StyleSelector.swift         # 风格选择
├── OutputGallery.swift         # 成果展示
├── ImportView.swift            # 导入对话框
└── Resources/                  # 资源文件
    └── CaseStudies/            # 案例库
```

---

## 🔧 系统要求

- macOS 12.0+
- Xcode 14.0+
- Swift 5.7+

---

## 💡 使用流程

1. **新建项目** → 输入项目名称
2. **导入文件** → 拖放CAD/图片/GIS文件
3. **选择功能** → 文旅/住宅/商业等
4. **调整参数** → 容积率/密度/绿化率等
5. **选择风格** → 新中式/现代/欧式等
6. **选择团队** → 学习顶尖设计理念
7. **生成方案** → AI自动生成设计
8. **查看成果** → 平面图/效果图/文档
9. **导出文件** → 保存到本地

---

## 📋 下一步开发计划

### Phase 1: AI集成 (2周后API配置完成)
- [ ] 接入GPT-4o/Claude生成设计理念
- [ ] Stable Diffusion渲染高质量效果图
- [ ] 案例库向量检索

### Phase 2: CAD引擎 (1个月)
- [ ] 完整CAD读写功能
- [ ] 精确的建筑布局算法
- [ ] 自动生成CAD图纸

### Phase 3: 3D渲染 (2个月)
- [ ] 3D模型自动生成
- [ ] 实时渲染预览
- [ ] VR/AR查看

### Phase 4: 学习系统 (持续)
- [ ] 案例库持续扩充
- [ ] 用户反馈学习
- [ ] 设计优化建议

---

## 🎨 设计团队数据库

App内置了12个国内外顶尖设计团队的核心设计理念：

### 中国团队
- **MAD建筑事务所**: 山水城市理念
- **GOA大象设计**: 和而不同，场所精神
- **蓝城集团**: 比城市更温暖，比乡村更文明
- **万科设计**: 建筑赞美生命

### 国际团队
- **BIG**: Yes is More，实用主义乌托邦
- **Sasaki**: 设计源于对场所的深刻理解
- **SOM**: 整体设计，技术与艺术融合
- **Zaha Hadid**: 建筑作为动态的力量场
- **Kengo Kuma**: 让建筑消失，与自然对话
- **WOHA**: 花园中的城市，垂直村落
- **Snøhetta**: 社会参与，环境共生

---

## 🔒 注意事项

1. **CAD文件**: 需要完整的解析库（当前为简化演示）
2. **AI生成**: 需要配置API Key后启用完整功能
3. **渲染效果**: 当前为简化版，后续接入专业渲染引擎

---

Made with ❤️ for 爸爸
