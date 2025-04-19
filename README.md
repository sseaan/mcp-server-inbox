# Inbox MCP Server

一个基于[MCP(Model Context Protocol)](https://modelcontextprotocol.io)的服务器，用于将笔记发送到Inbox API。

## 功能

这个MCP服务器提供了一个工具，可以将笔记内容发送到指定的Inbox API端点。

- 支持发送最多3000字符的笔记内容
- 通过环境变量配置用户令牌
- 简单易用的API接口

## 安装

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

## API

### 发送笔记

```
工具名称: send_note
参数:
  - content: 笔记内容 (最多3000字符)
返回: API响应
```

## 许可证

MIT