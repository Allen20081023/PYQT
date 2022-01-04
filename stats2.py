import os
import PySide2
import json

dirname = os.path.dirname(PySide2.__file__)
plugin_path = os.path.join(dirname, 'plugins', 'platforms')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path

from PySide2.QtWidgets import QApplication, QMessageBox, QPlainTextEdit,QLineEdit
from PySide2.QtUiTools import QUiLoader


class Stats:

    def __init__(self):
        # 从文件中加载UI定义

        # 从 UI 定义中动态 创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了
        # 比如 self.ui.button , self.ui.textEdit
        self.ui = QUiLoader().load('ui/bot_json.ui')

        self.ui.pushButton_req.clicked.connect(self.get_req())
        print(1)

    def get_req(self):
        n = self.ui.data1_req.text()
        d = self.ui.data2_req.text()
        print(2)

        REQ_ADR = {
            1: "version",  # 版本号
            2: "curMold",  # 当前模号(主机网口版本暂时不支持)
            3: "counterList",  # 计数器ID 列表：[“0”,“2”,“5”]
            4: "counter-",  # 计数器信息：[“id”, “目标”, “当前”]
            5: "curMode",  # 当前模式# (0#无,1#手动模式, 2#自动模式, 3#停止模式, 7#自动运行中, 8#单步,9#单循环)
            6: "boardIONum",  # IO 板总数
            7: "input-",  # 32 位输入状态# (n 从0 开始, 0#第1-32 个输入, 1#第33-64 个输入…)
            8: "output-",  # 32 位输出状态# (n 从0 开始, 0#第1-32 个输出, 1#第33-64 个输出…)
            9: "axisNum",  # 轴总数
            10: "axis-",  # 轴位置# (n 从0 开始, 0#J1, 1#J2, 2#J3, 3#J4, 4#J5, 5#J6, 6#J7, 7#J8)
            11: "world-",  # 世界坐标轴位置# (n 从0 开始, 0#X, 1#Y, 2#Z, 3#U, 4#V, 5#W, 6#M7, 7#M8)
            12: "curAlarm",  # 当前报警代号
            13: "curCycle",  # 当前周期(s)
            14: "lastCycle",  # 上模周期(s)
            15: "machineName",  # 机器名称
            16: "curTorque-",
            # 当前扭矩# (网口在主板的版本才有, 2580 代表一倍转矩, n 从0 开始, 0#J1,1#J2, 2#J3, 3#J4, 4#J5, 5#J6, 6#J7, 7#J8)
            17: "curSpeed-",  # 当前速度(RPM)# (网口在主板的版本才有, n 从0 开始, 0#J1, 1#J2, 2#J3, 3#J4,4#J5, 5#J6, 6#J7, 7#J8)
            18: "curAccount",  # 当前用户(主机网口版本暂时不支持)
            19: "origin",  # 原点状态
            20: "moldList",  # 模号列表：[“A1”,“A2”,“A5”]
            21: "isMoving",  # 是否处于移动状态#(1 为移动,0 为静止)
            22: "M-n"  # 32 位M 状态# (n 从0 开始, 0#第1-32 个M, 1#第33-64 个M…)
        }

        if not n:
            n = "0"

        n = ord(n) - 47
        cmd_data = REQ_ADR[n]
        if d:
            cmd_data = cmd_data + str(d)

        REQ = {
            "dsID": "www.hc-system.com.RemoteMonitor",
            "reqType": "command",
            "cmdData": cmd_data
            }
        if REQ:
            self.ui.textBrowser.textCursor(json.dumps(REQ,indent=True))

    # def handleCalc(self):
    #     info = self.ui.TextEdit.toPlainText()
    #
    #     salary_above_20k = ''
    #     salary_below_20k = ''
    #     for line in info.splitlines():
    #         if not line.strip():
    #             continue
    #         parts = line.split(' ')
    #
    #         parts = [p for p in parts if p]
    #         name, salary, age = parts
    #         if int(salary) >= 20000:
    #             salary_above_20k += name + '\n'
    #         else:
    #             salary_below_20k += name + '\n'
    #
    #     QMessageBox.about(self.ui,
    #                       '统计结果',
    #                       f'''薪资20000 以上的有：\n{salary_above_20k}
    #                 \n薪资20000 以下的有：\n{salary_below_20k}'''
    #                       )
    #

app = QApplication([])
stats = Stats()
stats.ui.show()
app.exec_()
