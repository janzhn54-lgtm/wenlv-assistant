# 多模型配置说明

**配置时间：** 2026-02-28 08:13 UTC

---

## 已配置的API

| 模型 | 状态 | 用途 |
|------|------|------|
| DeepSeek | ✅ 已配置 | 主力模型，长文本、代码 |
| Gemini 1.5 Flash | ✅ 已配置 | 快速响应、多模态 |

---

## API Key 存储位置

**文件：** `.env.local`

```bash
# DeepSeek
DEEPSEEK_API_KEY=sk-...
DEEPSEEK_BASE_URL=https://api.deepseek.com

# Gemini
GEMINI_API_KEY=AIzaSy...
GEMINI_BASE_URL=https://generativelanguage.googleapis.com
GEMINI_MODEL=gemini-1.5-flash
```

---

## 模型特性对比

| 特性 | DeepSeek | Gemini |
|------|----------|--------|
| 上下文长度 | 128K | 1M |
| 速度 | 中等 | 快 |
| 代码能力 | 强 | 中等 |
| 多模态 | ❌ | ✅ |
| 中文 | 优秀 | 良好 |
| 免费额度 | 有限 | 60 req/min |

---

## 使用建议

- **日常对话** → Gemini（快）
- **长文本分析** → DeepSeek（上下文长）
- **代码编写** → DeepSeek（代码能力强）
- **图片分析** → Gemini（多模态）

---

## 安全说明

- `.env.local` 已加入 `.gitignore`，不会上传到代码仓库
- API Key 仅本地使用
- 如需撤销，可在 Google AI Studio 删除 key

---

**配置完成！** 可同时使用 DeepSeek + Gemini 双模型
