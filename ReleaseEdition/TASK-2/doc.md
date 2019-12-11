## Doc for TASK-2
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
# python3 Client.py 127.0.0.1 8000 9000 test.mp4
```

### Client使用说明
#### Button功能
- `[Setup]` 点击初始化，播放前先点击此按钮
- `[Play]` 点击开始播放视频，暂停后再次开始也点击该按钮
- `[Pause]` 点击暂停视频播放
- `[Teardown]` 点击终止传输并关闭客户端
- `[Fullscreen]` 点击开启全屏模式
- `[0.5]` 点击开始以`0.5`倍速播放
- `[2.0]` 点击开始以`2.0`倍速播放

#### Slider功能
- 显示当前播放进度
- ***拖动***进度条可改变播放进度

#### 全屏时
- 按`[ESC]`键可退出全屏
- 全屏状态下按`[SPACE]`键可播放或暂停

#### 其他
- 在点击`[Teardown]`结束后重新以相同的`[client_port]`连接即可从上次中断位置继续播放

### 注意事项

#### Client端
1. 请勿在全屏时快速连续地按下`[SPACE]`键
2. 播放前请先按`[Setup]`按钮初始化
3. 多用户端连接时请在`[client_port]`处设置不同的值，如`client1`的`port`为`9000`，`client2`的`port`为`9001`