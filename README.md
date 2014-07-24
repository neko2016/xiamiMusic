xiamiMusic
==========


### 虾米音乐下载

一个简单的下载虾米音乐的客户端，目前功能比较简单，只能下载单条音乐，歌词和专题图片

#### 使用方法

安装

    pip install xiami

or
   
    easy_install xiami

下载 xiami
 
    git clone https://github.com/rsj217/xiamiMusic.git

解压
运行

    python setup.py install

使用

    # -*- coding: utf-8 -*-

    from xiami import XiaMi

    app = XiaMi(__file__)

    if __name__ == '__main__':
        app.start()

将会在当前运行的脚本下生成一个`download/歌曲id/`文件夹，里面包含下载的文件

### 0.0.3

- 分离下载回调函数
- 修复bug

#### 0.0.2

- 修复用户输入bug

#### 0.0.1

- 下载音频，专辑，歌词


#### todo

- GUI界面
- 分离配置文件
- 多线程下载
- 下载专辑