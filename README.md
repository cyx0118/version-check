# Version Check API

极简版本更新检查服务，本地 Python 应用与服务器通信获取最新版本。

## 快速开始
## API 接口
检查版本更新。

**参数：**
| 字段 | 类型 | 说明 |
|:---|:---|:---|
| current | string | 当前版本号，如 `1.0.0` |

**返回：**
```
{
    "latest": "1.2.3",
    "current": "1.0.0",
    "need_update": true,
    "url": "https://example.com/download",
    "changelog": "修复已知问题"
}
```

## 版本号规则

- 格式：`主版本.次版本.修订号`（如 `1.2.3`）
- 支持任意位数比较：`1.0` < `1.0.1` < `1.1` < `2.0`

## 开源协议
MIT
