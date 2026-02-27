# OpenClaw Chrome 扩展安装指南

## 方式一：Chrome 商店安装（推荐）

### 步骤：

1. **打开 Chrome 浏览器**
   地址栏输入：chrome://extensions/

2. **开启开发者模式**
   - 右上角开关打开 "开发者模式"

3. **访问 Chrome 商店**
   - 去 https://chrome.google.com/webstore
   - 搜索 "OpenClaw" 或 "OpenClaw Browser Relay"

4. **安装扩展**
   - 找到 OpenClaw 扩展
   - 点击 "添加至 Chrome"
   - 确认权限

---

## 方式二：手动安装（如果商店没有）

### 步骤：

1. **下载扩展文件**
   ```bash
   # 在 Codespace 里打包扩展
   cd /usr/local/share/nvm/versions/node/v24.11.1/lib/node_modules/openclaw/extensions
   zip -r openclaw-extension.zip browser-relay/
   ```

2. **在 Chrome 中加载**
   - 打开 chrome://extensions/
   - 开启 "开发者模式"
   - 点击 "加载已解压的扩展程序"
   - 选择扩展文件夹

---

## 方式三：GitHub 直接下载

1. 访问 https://github.com/openclaw/openclaw/releases
2. 下载 `openclaw-browser-extension.zip`
3. 解压后按方式二加载

---

## 🔧 配置扩展

安装后需要配置：

1. **点击扩展图标**（在 Chrome 右上角）
2. **输入 Gateway 地址**：
   ```
   ws://10.0.1.20:18789
   ```
3. **输入 Token**：`mysecret`（或更新后的 token）
4. **点击 Connect**

---

## ✅ 验证连接

连接成功后：
- 扩展图标会显示绿色 ✓
- 我能通过浏览器工具控制你的浏览器
- 你可以实时看到我的操作

---

## ⚠️ 注意事项

由于你在 Codespace 外网，我在内网，直接连可能有问题。

### 解决方案：

**方案 A：端口转发**
在 Codespace 终端运行：
```bash
github codespace ports visibility 18789:public
```
然后使用公网地址连接。

**方案 B：Tailscale（推荐）**
安装 Tailscale 组网，直接内网互通。

**方案 C：直接用飞书推送**
不用 Chrome 扩展，我的操作直接推送到飞书。

---

**爸爸，你先试试能不能找到 Chrome 商店的 OpenClaw 扩展？**

找不到的话，我推荐用 **方案 C（飞书推送）**，更简单！
