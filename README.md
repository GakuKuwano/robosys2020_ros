# robosys2020_ros

ros上でメッセージをGmailで送信するためのソフトウェア（ロボットシステム学の講義で作成）

# DEMO

https://youtu.be/-MeB0o7sv5Q

[![robosys ros](http://img.youtube.com/vi/MeB0o7sv5Q/0.jpg)](https://www.youtube.com/watch?v=-MeB0o7sv5Q "robosys ros")

# 実装内容

- メールアドレスとパスワードを入力するとメッセージを記入できるので，件名と本文を入力して送信する．（宛先はコードに記入しておく）
- Subscriberがメッセージを受け取り，その旨をターミナルに表示
- 送信先のアカウントでGmailの受信を確認

# 実装環境

| | |
|:--:|:--:|
|OS|ubuntu 20.04|
|ROS|noetic|

# インストール方法

```bash
$ cd ~/catkin/src
$ git clone https://github.com/GakuKuwano/robosys2020_ros.git
```

# プログラムの実行方法

- [googleアカウント](https://www.google.com/intl/ja/account/about/)を作成する

- パッケージをbuild
```bash
$ cd ~/catkin_ws
$ catkin_make
$ source ~/catkin_ws/devel/set_up.bash
```
- プログラム実装
```bash
$ cd ~/catkin_ws/src/robosys2020_ros/scripts
$ rosrun robosys2020_ros receiver.py
```
  別のターミナルにて
```bash
$ cd ~/catkin_ws/src/robosys2020_ros/scripts
$ rosrun robosys2020_ros sender.py
```

# 引用

- [pythonでGmailを送信する](https://qiita.com/eito_2/items/ef77e44955e43f31ba78)
