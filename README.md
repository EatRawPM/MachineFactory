# MachineFactory
使用PyGame制作的自动化游戏。

## 前
这是我第一个发布的作品，也是我第一个制作的游戏，如果有什么不好，欢迎评论。

## 介绍

* ### 更新内容

* GameScene新增地图
* 新增可操控的玩家
* 新增动画Class

* ### 操作

* 使用WASD移动
* 使用鼠标滚轮缩放

## 库

### 使用的Python库
* PyGame
* PyGetWindow

### 安装指令
```
pip install pygame
```
```
pip install pygetwindow
```
#### 快速安装

在指令后加上
```
-i https://mirrors.aliyun.com/pypi/simple/
```

## 打包

### 使用pyinstaller打包。

* 先要安装requests

```
pip install requests
```

* 获得requirements.txt

```
pip freeze > requirements.txt
```

* 安装pyinstaller

```
pip install pyinstaller
```

### 打包

#### 测试打包

```
pyinstaller -F run.py -n MachineFactory -i .\assets\images\icons\icon.ico
```

#### 正式打包

```
pyinstaller -F run.py -n MachineFactory -w -i .\assets\images\icons\icon.ico
```
