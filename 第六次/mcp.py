#!/usr/bin/env python3
import json,sys,random

TOOLS=[
{"name":"hello","description":"返回欢迎信息"},
{"name":"get_random_number","description":"生成随机整数"}
]

def send(x):
    print(json.dumps(x,ensure_ascii=False),flush=True)

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
        send({"jsonrpc":"2.0","id":rid,"result":{"serverInfo":{"name":"student-server","version":"1.0"}}})
    elif method=="tools/list":
        send({"jsonrpc":"2.0","id":rid,"result":{"tools":TOOLS}})
    elif method=="tools/call":
        name=req.get("params",{}).get("name")
        if name=="hello":
            txt="Hello, MCP!"
        elif name=="get_random_number":
            txt=str(random.randint(1,100))
        else:
            send({"jsonrpc":"2.0","id":rid,"error":{"code":-1,"message":"unknown tool"}})
            continue
        send({"jsonrpc":"2.0","id":rid,"result":{"content":[{"type":"text","text":txt}]}})
    else:
        send({"jsonrpc":"2.0","id":rid,"error":{"code":-32601,"message":"method not found"}})
