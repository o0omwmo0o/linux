#!/usr/bin/env python3
"""
Linux课程作业（模仿版）
功能：
1. 模拟Linux下的系统信息查询工具
2. 使用JSON输入输出
3. 支持initialize、tools/list、tools/call三个请求
"""

import json
import sys
import platform
import time

TOOLS=[
    {"name":"system_info","description":"查看系统信息"},
    {"name":"current_time","description":"查看当前时间"}
]

def send(data):
    print(json.dumps(data,ensure_ascii=False),flush=True)

while True:
    line=sys.stdin.readline()
    if not line:
        break
    try:
        req=json.loads(line)
    except:
        continue
    rid=req.get("id")
    method=req.get("method")
    if method=="initialize":
        send({"jsonrpc":"2.0","id":rid,
              "result":{"serverInfo":{"name":"linux-demo","version":"1.0"}}})
    elif method=="tools/list":
        send({"jsonrpc":"2.0","id":rid,"result":{"tools":TOOLS}})
    elif method=="tools/call":
        name=req["params"]["name"]
        if name=="system_info":
            text=f"系统:{platform.system()} 版本:{platform.release()}"
        elif name=="current_time":
            text=time.strftime("%Y-%m-%d %H:%M:%S")
        else:
            send({"jsonrpc":"2.0","id":rid,"error":{"code":-1,"message":"未知工具"}})
            continue
        send({"jsonrpc":"2.0","id":rid,
              "result":{"content":[{"type":"text","text":text}]}})
