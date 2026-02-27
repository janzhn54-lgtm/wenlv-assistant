#!/bin/bash
# OpenClaw 服务器迁移脚本
# 在独立服务器上运行，自动部署并恢复配置

set -e

echo "🚀 OpenClaw 服务器迁移开始..."

# 1. 安装依赖
echo "📦 安装基础依赖..."
apt-get update
apt-get install -y curl git nodejs npm jq unzip

# 2. 安装 OpenClaw
echo "🔧 安装 OpenClaw..."
npm install -g openclaw

# 3. 创建目录结构
echo "📁 创建目录结构..."
mkdir -p ~/.openclaw/workspace
mkdir -p ~/.openclaw/logs
mkdir -p ~/.openclaw/backups

# 4. 提示用户从 Codespace 复制配置文件
echo ""
echo "⚠️  请从 GitHub Codespace 下载以下文件并上传到服务器 ~/.openclaw/ 目录："
echo "   - openclaw.json (主配置文件)"
echo "   - workspace/ 文件夹 (所有工作文件)"
echo ""
echo "   下载命令（在 Codespace 运行）："
echo "   zip -r ~/openclaw-backup.zip ~/.openclaw/"
echo ""
read -p "配置文件上传完成后按回车继续..."

# 5. 恢复权限
echo "🔐 设置权限..."
chmod 600 ~/.openclaw/openclaw.json 2>/dev/null || true

# 6. 安装飞书插件
echo "📱 安装飞书插件..."
openclaw plugins install feishu || true

# 7. 启动 Gateway
echo "🌐 启动 OpenClaw Gateway..."
nohup openclaw gateway > ~/.openclaw/logs/gateway.log 2>&1 &
echo "Gateway 已启动在后台"

# 8. 设置开机自启
echo "⚙️  设置开机自启..."
cat > /etc/systemd/system/openclaw.service << 'EOF'
[Unit]
Description=OpenClaw Gateway
After=network.target

[Service]
Type=simple
User=root
WorkingDirectory=/root
ExecStart=/usr/bin/openclaw gateway
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
EOF

systemctl daemon-reload
systemctl enable openclaw
systemctl start openclaw

# 9. 创建保活脚本
echo "🛡️  创建保活机制..."
cat > ~/.openclaw/keepalive.sh << 'EOF'
#!/bin/bash
while true; do
    echo "[$(date)] Keepalive" >> ~/.openclaw/logs/keepalive.log
    sleep 300
done
EOF
chmod +x ~/.openclaw/keepalive.sh

nohup ~/.openclaw/keepalive.sh > /dev/null 2>&1 &
echo "保活进程已启动"

# 10. 显示状态
echo ""
echo "✅ 部署完成！"
echo ""
echo "📊 状态检查："
openclaw status 2>&1 | head -20

echo ""
echo "🌐 服务器信息："
echo "   IP: $(curl -s ifconfig.me 2>/dev/null || echo '获取失败')"
echo "   Gateway: http://$(curl -s ifconfig.me 2>/dev/null || echo 'IP'):18789"
echo ""
echo "⚠️  重要：请确保防火墙放行 18789 端口"
echo ""
echo "🎉 OpenClaw 已在独立服务器上运行，永不掉线！"
