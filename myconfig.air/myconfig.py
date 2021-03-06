#coding = utf-8

"模版全局参数配置与测试用例自定义参数配置模块"

__author__ = "LT"

#---------------------------------全局参数----------------start------------------------------
# 数据库连接配置信息
mysql_config = {
    'host': '127.0.0.1',
    'port': 3306,
     # 数据库
    'database': 'uitest',
     # 用户名和密码
    'user': 'root',
    'password': '123456',
     # 数据库编码
    'charset': 'utf8'
}

#---------------------------------全局参数----------------end------------------------------
# 运行日志目录，自定义 
logDir='G:/ui-log'
# 是否自动生成报告 True / False
auto_report_Flag = True
# 启动模式  dev：指调试模式，启动时候从所有用例窗口启动 / prod: 指启动时候从start_run启动
start_model="dev"
#---------------------------------全局参数----------------start------------------------------

#---------------------------------用例业务参数------------start------------------------------
# 启动应用classify标识及环境选择
CLASSIFY = 'my_app'
# 商户侧ID 已开户可转账的用户
case_01_params = {'phone':'13975616542'}
#---------------------------------用例业务参数------------start------------------------------