#!/bin/bash
# OpenClaw 配置备份脚本
# 每天自动备份配置文件

BACKUP_DIR="$HOME/.openclaw/backups"
mkdir -p "$BACKUP_DIR"

TIMESTAMP=$(date '+%Y%m%d_%H%M%S')

# 备份主配置
cp "$HOME/.openclaw/openclaw.json" "$BACKUP_DIR/openclaw.json.$TIMESTAMP"

# 备份工作空间
tar -czf "$BACKUP_DIR/workspace-$TIMESTAMP.tar.gz" -C "$HOME/.openclaw" workspace/

# 只保留最近30个备份
cd "$BACKUP_DIR"
ls -t openclaw.json.* | tail -n +31 | xargs -r rm
ls -t workspace-*.tar.gz | tail -n +31 | xargs -r rm

echo "Backup completed: $TIMESTAMP"
echo "Backup files in: $BACKUP_DIR"
