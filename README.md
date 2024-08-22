# Python 学习记录

## Introduction
每个单元作为一个章节，包含了详细的 .md 说明文件讲述当前单元的基础知识,并且由其中细分的 .py 文件实现代码运行

学习方式包括但不限于课程,文档,项目,结合 github copilot 完成的这一项储存库

预计后面会加入小项目和一些更贴近工作的知识

## Unit
- unit 1 初识Python
- unit 2 变量和基础数据类型
- unit 3 运算符
- unit 4 条件判断
- unit 5 循环
- unit 6 组合数据类型
- unit 7 异常处理
- unit 8 函数
- unit 9 模块
- unit 10 文件及IO操作
- unit 11 面向对象程序设计
- unit 12 界面开发

## Exercises(./exercises)

- unit 1 1.1 个人名片(Personal business card)
  > 在控制台提示用户依次输入：姓名、公司、职位、电话、邮箱
  > 按照以下格式输出：
  ```
        ********************************
        name:
        company:
        title:
        phone:
        email
        ********************************`
  ```
- unit 2 2.1 几个苹果(A few apples)
  > 有10个苹果，A 拿走2个，B 拿走 4 个，C 拿走剩下的
  > 问：C 拿走几个苹果, A 和 B 一共拿走几个苹果
- unit 2 2.2 支付宝余额(Alipay balance)
  > 支付宝有 100 元，经过以下操作
  > 存 10 元
  > 取 20 元
  > 全部转出
  > 请在每次操作后输出余额
- unit 3 3.1 分苹果(Divide the apples)
  > 有 14 个苹果，分给 4 个小朋友,分不掉的苹果留下来
  > 请问每个小朋友分几个苹果，还剩几个苹果,分出去的苹果总数
- unit 4 4.1 年龄判断(Age judgment)
  > 输入一个人的年龄，判断这个人年龄是否在 1 - 120 之间
- unit 4 4.2 成绩判断(Performance judgment)
  > 输入两门成绩，有一门大于 60 分就算及格
- unit 4 4.3 闰年判断(Leap year determination)
  > 输入一个年份，判断这个年份是否是闰年
  > 闰年条件：能被4整除但不能被 100 整除，或者能被 400 整除
  > 例如：2000 年是闰年，1900 年不是闰年
- unit 5 5.1 打印星号(Print the star)
  > 打印 m*n 个星号
  > 打印 n 行的字符三角形
- unit 5 5.2 猴子吃桃子(Monkeys eat peaches)
  > 猴子第一天摘下若干个桃子，当即吃了一半，还不过瘾，又多吃了一个
  > 第二天早上又将剩下的桃子吃掉一半，又多吃了一个
  > 以后每天早上都吃了前一天剩下的一半零一个
  > 到第 10 天早上想再吃时，见只剩下一个桃子了
  > 请问猴子第一天共摘了多少个桃子
- unit 5 5.3 九九乘法表(Nine times nine multiplication table)
  > 输出九九乘法表
  > 
  > 1 * 1 = 1
  > 
  > 1 * 2 = 2 2 * 2 = 4
  > ...

## In action(./In action)

### 用户登录系统(User Login System)
- 用户输入用户名和密码，根据用户是否已注册,是否在黑名单中,提示用户登录成功或失败
1. 登录功能实现 
   1. 输入用户名和密码 
   2. 登陆验证 
      1. 用户是否已注册
      2. 密码是否正确
      3. 是否在黑名单中
   3. 验证次数限制 --> 3 次
- 数据结构设计
1. 保存用户名,密码,黑名单
   1. 列表
   2. 字典

### 计算天数(Counting days)
- 输入年月日,计算这一天是这一年的第几天  

      e.g:输入2024-12-31,输出2024年的第366天

### 简单计算器(Simple calculator)
1. 需求分析
   1. 支持加减乘除
   2. 输入不合法时提示用户
2. 任务拆解
   1. 加法运算
   2. 减法运算
   3. 乘法运算
   4. 除法运算
   5. 异常情况处理
3. 数据结构设计
   1. 储存运算结果
4. 代码流程 ( 循环进行 )
   1. 输入两个数
   2. 输入 C 退出程序
   3. 输入运算符
      1. 加法
      2. 减法
      3. 乘法
      4. 除法
      5. 异常
   4. 进行运算
   5. 输出结果

### 名片管理系统(Business card management system)
1. 需求分析
   1. 启动欢迎界面,并显示功能菜单
   2. 用户选择功能
      1. 新建名片
      2. 显示全部
      3. 查询名片
      4. 退出系统
   3. 执行用户选择的功能
   4. 用户名片需要记录
      1. 姓名
      2. 电话
      3. QQ
      4. 邮箱
   5. 如果查询到名片,可以选择修改或删除
2. 任务拆解
   1. 增: 新建名片,姓名,电话,QQ,邮箱
   2. 删: 删除名片
   3. 改: 修改名片
   4. 查
      1. 显示全部
      2. 查询名片:根据什么查询
3. 数据结构设计
    1. 字典
    2. 列表

### 日记本(Journal book)
- unit 10 代码练习,见 unit 10 File and IO operations/code 10.4 Journal book
- 日记存储在 .py 文件同级目录(./journal.txt)

### 学生管理系统(Student management system)
- 学生
  - 姓名,年龄,性别,学号,参与课程
  - 显示学生信息
- 老师
  - 姓名,年龄,性别,工号,是否是导员,班级列表
  - 显示老师信息
- 课程
  - 课名,课程号,学分,老师,性质,课程容量
  - 显示课程信息
- 班级
  - 班级名称,班级号,辅导员,学生列表
  - 显示班级信息
- ...

### 抽奖器(Prize drawing apparatus)
- 见 unit 12 Interface development/code 12.3 Prize drawing apparatus

### 简单计算器(Simple calculator)
- 见 unit 12 Interface development/code 12.4 Simple calculator

## 项目实战(见./Project Practice文件夹)

### 多人聊天室(Multi-person chat rooms)
- 客户端
  - Client 类
    - 父类:wx.Frame
    - 初始化方法
      - 实例属性
        - 客户名: name
        - 连接状态: isConnected
        - 套接字: client_socket
      - 界面
        - wxPython
          - 界面设计
          - 调用父类初始化模板  个人信息  用户名
          - 创建面板
          - 创建按钮
            - 加入聊天室
            - 离开聊天室
            - 发送消息
            - 清空消息
          - 创建文本框
            - 聊天窗口: chat_text
            - 文本编辑器: input_text
          - 绑定事件
            - 加入聊天室: connect
            - 离开聊天室: disconnect
            - 发送消息: send
            - 清空消息: reset
    - 事件响应方法
      - connect
        - 创建 socket 对象
        - 连接服务器
        - 发送客户信息
        - 创建线程接收消息: receive
      - disconnect
        - 发送断开连接信息
        - 设置连接状态: self.isConnected = False
      - send
        - 获取输入内容
        - 发送内容
        - 清空输入内容
      - reset
        - self.input_text.Clear()
      - receive
        - 接收消息
        - 显示消息
        
   
- 服务器
  - Server 类
    - 父类:wx.Frame
    - 初始化方法
    - 事件响应方法
  - SessionThread 类:父类 threading.Thread