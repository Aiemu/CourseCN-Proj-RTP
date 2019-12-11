## Doc for TASK-1
`2017011438 曾正`

### 运行方式
#### Server端
在终端运行下列指令：
``` bash
python3 Server.py [port] 
# e.g. 
# python3 Server.py 8000
```

### Client端
在终端运行下列指令：
``` bash
python3 Client.py [server_ip] [server_port] [client_port] [file_name]
# e.g. 
# python3 Client.py 127.0.0.1 8000 9000 img/1.png
```

### Client使用说明
#### Button功能
- `[Setup]` 点击初始化，播放前先点击此按钮
- `[Play]` 点击开始播放，暂停后再次开始也点击该按钮
- `[Pause]` 点击暂停播放
- `[Teardown]` 点击终止传输并关闭客户端

### 注意事项
#### Server端
1. 会按顺序从`img`文件夹下持续读取`.jpg`文件，由`1.jpg`到`2.jpg`并持续向后读取，读到末尾`n.jpg`则再次读取`1.jpg`
2. 图片命名应为`k.jpg`(k连续的正整数)，并统一存在`img`文件夹下

#### Client端
1. 运行指令中的`[file_name]`部分应由`img/`开头，形如`img/1.jpg`