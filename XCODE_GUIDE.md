# 文旅日报 App - Xcode 运行指南

## 📦 第一步：解压文件

1. 找到下载的 `wenlv-assistant-main.zip`
2. 双击解压，得到 `wenlv-assistant-main` 文件夹
3. 打开文件夹，进入 `projects/WenlvDaily/`

## 🚀 第二步：Xcode 打开项目

### 方法 A：直接打开（推荐）

1. 打开 **Xcode**（确保是最新版或 iOS 15+ 支持版本）
2. 点击菜单 **File → Open...**
3. 导航到：`wenlv-assistant-main/projects/WenlvDaily/`
4. 选中 **WenlvDaily** 文件夹
5. 点击 **Open**

### 方法 B：拖拽打开

1. 打开 Xcode
2. 直接把 `WenlvDaily` 文件夹拖到 Xcode 图标上

## ⚙️ 第三步：配置项目

1. **等待索引完成** - Xcode 首次打开会索引文件（1-2分钟）
2. **选择模拟器**：顶部工具栏选择 iPhone 15 Pro（或你的设备）
3. **登录 Apple ID**：
   - Xcode → Preferences → Accounts
   - 点击 + 号，添加你的 Apple ID

## ▶️ 第四步：运行 App

1. 点击顶部 **▶️ 运行按钮**（或按 Cmd+R）
2. 等待编译（首次编译需要 1-3 分钟）
3. 模拟器会自动启动，显示 App

## 📱 界面预览

运行后会看到：
- **今日** - 每日精选新闻列表
- **分类** - 政策/市场/案例/趋势四大分类
- **收藏** - 收藏的新闻
- **我的** - 阅读统计和设置

## ⚠️ 常见问题

### 1. 编译错误 "Signing for requires a development team"
**解决**：
- 点击左侧项目导航栏最顶部的 **WenlvDaily**
- 选择 **Targets → WenlvDaily → Signing & Capabilities**
- 在 **Team** 下拉框选择你的 Apple ID
- 修改 **Bundle Identifier**（随便改个名字，比如 `com.yourname.wenlvdaily`）

### 2. 模拟器黑屏/卡住
**解决**：
- Device → Erase All Content and Settings
- 或重启模拟器：Device → Restart

### 3. 找不到文件
**解决**：
- 确保打开的是 `WenlvDaily` 文件夹，不是上级目录
- 应该能看到 `WenlvDailyApp.swift`, `Models.swift` 等文件

## 🎯 真机测试（可选）

如果想在真机上测试：

1. 用 USB 连接 iPhone
2. 顶部选择你的 iPhone
3. 点击运行
4. 首次需要在 iPhone 设置 → 通用 → 设备管理中信任开发者

## 💡 下一步开发

运行成功后，你可以：
- 修改 `NewsStore.swift` 中的 `mockNews()` 添加自己的新闻数据
- 修改配色：在 `Assets.xcassets` 中添加颜色
- 添加推送：配置 Apple Developer 账号

---
有问题随时问我！
