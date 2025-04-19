# Inbox MCP Server

[![smithery badge](https://smithery.ai/badge/@sseaan/mcp-server-inbox)](https://smithery.ai/server/@sseaan/mcp-server-inbox)

一个基于[MCP(Model Context Protocol)](https://modelcontextprotocol.io)的服务器，用于将笔记发送到Inbox API。

## 功能

这个MCP服务器提供了一个工具，可以将笔记内容发送到指定的Inbox API端点。

- 接入 inBox 笔记 API
- 支持通过 MCP 客户端创建笔记
- 支持设置笔记标题

## 安装

### 安装 via Smithery

要自动为 Claude Desktop 安装 MCP Server 服务器，你可以使用 [Smithery](https://smithery.ai/server/@sseaan/mcp-server-inbox):

```bash
npx -y @smithery/cli install @sseaan/mcp-server-inbox --client claude
```
### 前置要求

- inBox 笔记 API (需要PRO)
- 支持 MCP 协议的客户端（CherryStudio/Cursor等）

### 依赖

- Python 3.8+
- requests
- mcp[cli]

### 安装步骤

```bash
# 克隆仓库
git clone https://github.com/example/inbox-mcp-server.git
cd inbox-mcp-server

# 安装依赖
pip install -e .
```

## 使用方法

### 环境变量设置

在运行服务器之前，需要设置以下环境变量：

- `INBOX_TOKEN`: 用于访问Inbox API的用户令牌

```bash
# Linux/macOS
export INBOX_TOKEN=your_token_here

# Windows (CMD)
set INBOX_TOKEN=your_token_here

# Windows (PowerShell)
$env:INBOX_TOKEN="your_token_here"
```

### 运行服务器

```bash
# 直接运行
python main.py

# 或使用MCP CLI
mcp run main.py
```

### 在Claude Desktop中安装

```bash
mcp install main.py
```
## 在 MCP 客户端中配置

在Smithery输入INBOX_TOKEN
获得json配置文件如下：
```json
"mcp-server-inbox": {
  "command": "npx",
  "args": [
    "-y",
    "@smithery/cli@latest",
    "run",
    "@sseaan/mcp-server-inbox",
    "--key",
    "*******************************"
  ]
}
```

### CherryStudio

1. 打开 CherryStudio 的 MCP 服务器设置页面
2. 点击 "添加服务器"
3. 输入服务器名称（例如 "inbox-mcp-server"）
4. 类型选择 “标准输入/输出(stdio)”
5. 命令输入npx
6. 输入参数
```
-y
@smithery/cli@latest
run
@sseaan/mcp-server-inbox
--key
*******************************
```
7. 点击 "保存"

### Cursor

1. 打开 Cursor 的 MCP 服务配置文件（通常位于 `~/.cursor/mcp.json`）
2. 添加 mcp-server-inbox 的配置：

```json
{
  "mcpServers": {
    "mcp-server-inbox": {
      "command": "npx",
      "args": [
        "-y",
        "@smithery/cli@latest",
        "run",
        "@sseaan/mcp-server-inbox",
        "--key",
        "*******************************"
      ]
    }
  }
}
```

### 其他 MCP 客户端

请参考对应 MCP 客户端的配置文档，添加类似的配置信息。

## API 说明

### 发送笔记

```
工具名称: send_note
参数:
  - content: 笔记内容 (最多3000字符)
  - title: 笔记标题
```

## 许可证

MIT
