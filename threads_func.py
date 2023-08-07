import re
import time
import urllib.parse

import requests
from PyQt5.QtCore import QThread, pyqtSignal

# 注释删
class Delnote(QThread):
    del_success = pyqtSignal()
    del_jdt = pyqtSignal(int)

    def __init__(self, ip, all_note, headers, *args, **kwargs):
        super(Delnote, self).__init__(*args, **kwargs)
        self.headers = headers
        self.txt = ip
        self.all_note = all_note
        self.del_num = 0
        self.del_time = 0


    def run(self):
        all_nums = 0
        for note_type in self.all_note:
            all_nums = all_nums + len(self.all_note[note_type])
        print(f"总数:{all_nums}")

        for note_type in self.all_note:
            for note in self.all_note[note_type]:
                self.del_num = self.del_num + 1
                self.del_time = int(int(self.del_num) / all_nums * 100)
                self.del_jdt.emit(self.del_time)
                requests.get(
                    f"http://{self.txt}/karel/ComSet?sComment=&sIndx={note}&sFc={note_type}",
                    headers=self.headers)
        print("ok")
        self.del_success.emit()

# 注释写
class Whilenote(QThread):
    while_success = pyqtSignal()
    while_jdt = pyqtSignal(int)

    def __init__(self, ip, all_note, headers, *args, **kwargs):
        super(Whilenote, self).__init__(*args, **kwargs)
        self.headers = headers
        self.txt = ip
        self.all_note = all_note
        self.while_num = 0
        self.while_time = 0


    def while_io_note(self, io_type, number, data):
        data = data.encode('gb2312')
        data = urllib.parse.quote(data)
        url = f"http://{self.txt}/karel/ComSet?sComment={data}&sIndx={number}&sFc={io_type}"
        requests.get(url, headers=self.headers)

    def run(self):
        all_nums = 0
        for note_type in self.all_note:
            all_nums = all_nums + len(self.all_note[note_type])
        print(f"总数:{all_nums}")

        for note_type in self.all_note:
            for note in self.all_note[note_type]:
                self.while_num = self.while_num + 1
                self.while_time = int(int(self.while_num) / all_nums * 100)
                self.while_jdt.emit(self.while_time)
                print(self.while_time)
                self.while_io_note(str(note_type), str(note[1]), str(note[0]))
        self.while_success.emit()

# 坐标获取
class GetRbJOIN(QThread):
    get_rb_join = pyqtSignal(list, list)
    sleep_time = 0.5
    quit_flag = False

    def __init__(self, ip, headers, *args, **kwargs):
        super(GetRbJOIN, self).__init__(*args, **kwargs)
        self.Joint_list = None
        self.headers = headers
        self.txt = ip
        self.world = None

    def run(self):
        print("线程启动完成")
        while True:
            print(self.quit_flag)
            if self.quit_flag:
                break
            url = f'http://{self.txt}/MD/SUMMARY.DG?_TEMPLATE=FRS:SUMMTMPC'
            r = requests.get(url, headers=self.headers).text
            self.Joint_list = re.findall(
                r"Group #:.*?1\n.*? \n.*?\n.*?Joint.*?1:(.*?)\n.*?Joint.*?2:(.*?)\n.*?Joint.*?3:(.*?)\n.*?Joint.*?4:(.*?)\n.*?Joint.*?5:(.*?)\n.*?Joint.*?6:(.*?)\n",
                r)
            print(self.Joint_list)
            if "$VERSION: V7" in r:
                self.world = re.findall(r'CURRENT USER FRAME POSITION:.*?\nX:(.*?)\nY:(.*?)\nZ:(.*?)\nW:(.*?)\nP:(.*?)\nR:(.*?)\n', r)
            else:
                self.world = re.findall(r"CURRENT USER FRAME POSITION:.*?\n.*?\nX:(.*?)\nY:(.*?)\nZ:(.*?)\nW:(.*?)\nP:(.*?)\nR:(.*?)\n", r)
            self.get_rb_join.emit(self.Joint_list, self.world)
            # 暂停0.5秒
            time.sleep(self.sleep_time)

# 下载LS程序
class DownloadLs(QThread):
    download_success = pyqtSignal()

    def __init__(self, ip, headers, path, ls_list, *args, **kwargs):
        super(DownloadLs, self).__init__(*args, **kwargs)
        self.headers = headers
        self.txt = ip
        self.path = path
        self.ls_list = ls_list

    def run(self):
        for ls in self.ls_list:
            url = f"http://{self.txt}/MD/{ls}"
            r = requests.get(url).text
            ls_text = re.findall(r'<XMP>([\d\D]*)</XMP>', r)
            with open(f"{self.path}//{ls}", "w") as f:
                f.write(ls_text[0])
        self.download_success.emit()

# 模糊搜索
class FuzzySearch(QThread):
    return_fuzzy_search = pyqtSignal(list)

    def __init__(self, ip, bl_headers, fuzzy_text, *args, **kwargs):
        super(FuzzySearch, self).__init__(*args, **kwargs)
        self.txt = ip
        self.fuzzy_text = fuzzy_text
        self.headers = bl_headers

    def run(self):
        url = f'http://{self.txt}/karel/ComSet?sComment={self.fuzzy_text}&sIndx=1&sFc=69'

        self.headers['Host'] = self.txt
        self.headers['Referer'] = f'http://{self.txt}/karel/ComSet?sComment={self.fuzzy_text}&sIndx=0&sFc=69'

        try:
            r = requests.get(url, headers=self.headers, timeout=15).text
            print(r)
            ls_list = re.findall(r'<br><a href=(.*?)</a>(.*?)\n', r)
        except Exception as e:
            print(str(e))
            ls_list = [("访问超时", "访问超时", "访问超时")]
        self.return_fuzzy_search.emit(ls_list)

# 初始获取所有VA文件
class InitVarSql(QThread):
    return_init_data = pyqtSignal()
    init_jd = pyqtSignal(str)

    def __init__(self, ip, path, *args, **kwargs):
        super(InitVarSql, self).__init__(*args, **kwargs)
        self.txt = ip
        self.jd = 0
        self.path = path

    def run(self):
        # 获取所有VA文件
        requests_code = "utf-8"

        all_data = requests.get(f"http://{self.txt}/MD/INDEX_VR.HTM")
        all_top_name = re.findall(r"</TD><TD align=center><A HREF=\"..(.*?).VA\">.*.VA</A></TD>", all_data.text)

        with open(f"{self.path}\config\\var1.txt", "w", encoding=requests_code) as f:

            for top_name in all_top_name:  # 遍历所有VA文件
                url = f"http://{self.txt}{top_name}.VA"
                data = requests.get(url).text
                self.jd = self.jd + 1
                self.init_jd.emit(f"当前状态：记录中({self.jd}/{len(all_top_name)})")
                if "$" not in data:
                    continue
                else:
                    try:
                        f.write(data)
                    except Exception as e:
                        print(url)
                        print(str(e))
                        break

        self.return_init_data.emit()

# 二次比对VA文件
class TraversalVar(QThread):
    return_traversal_data = pyqtSignal(list)
    traversal_jd = pyqtSignal(str)

    def __init__(self, ip, path, *args, **kwargs):
        super(TraversalVar, self).__init__(*args, **kwargs)
        self.txt = ip
        self.jd = 0
        self.path = path
        self.var2 = []
        self.var2_index = []

    # 下载所有VA文件
    def get_data(self):
        requests_code = "utf-8"

        # 获取所有VA文件
        all_data = requests.get(f"http://{self.txt}/MD/INDEX_VR.HTM")
        all_top_name = re.findall(r"</TD><TD align=center><A HREF=\"..(.*?).VA\">.*.VA</A></TD>", all_data.text)

        with open(f"{self.path}\config\\var2.txt", "w", encoding=requests_code) as f:

            for top_name in all_top_name:  # 遍历所有VA文件
                url = f"http://{self.txt}{top_name}.VA"
                data = requests.get(url).text
                #unicodedata.normalize('NFKC', data)
                self.jd = self.jd + 1
                self.traversal_jd.emit(f"当前状态：记录中({self.jd}/{len(all_top_name)})")
                if "$" not in data:
                    continue
                else:
                    try:
                        f.write(data)
                    except Exception as e:
                        print(url)
                        print(str(e))


    def read_file(self, path1, path2):
        self.traversal_jd.emit(f"当前状态：分析中")
        with open(path1, 'r', encoding='utf-8') as f:
            data1 = f.read()
        with open(path2, "r", encoding='utf-8') as f:
            data2 = f.read()
        data1 = data1.split("\n")
        data2 = data2.split("\n")
        self.var2 = data2
        difference1 = list(set(data1) - set(data2))
        difference2 = list(set(data2) - set(data1))

        difference1_index = sorted([data1.index(i) for i in difference1])
        difference2_index = sorted([data2.index(i) for i in difference2])
        difference_index = list(set(difference1_index + difference2_index))
        self.var2_index = difference_index

        return [self.get_father_son_together(i) for i in difference_index]

    def get_father_son_together(self, i):
        content = self.find_father_content(i)
        if content == self.var2[i]:
            return content
        else:
            return f"{content}\n{self.var2[i]}"

    def find_father_content(self, index):
        if index + 1: # 确保当前索引值为正
            if "$" in self.var2[index]:
                return self.var2[index]
            else:
                return self.find_father_content(index-1)
        else: # 检索到第一行 直接直接返回空
            return ""

    def run(self):
        self.get_data()
        data = self.read_file(f"{self.path}\config\\var1.txt", f"{self.path}\config\\var2.txt")
        self.return_traversal_data.emit(data)

# IP可用性检测
class IPColor(QThread):
    set_item_color = pyqtSignal(list)
    set_win_title = pyqtSignal(str)

    def __init__(self, ip, *args, **kwargs):
        super(IPColor, self).__init__(*args, **kwargs)
        self.ip_list = ip

    def run(self):
        for i in self.ip_list:

            # if self.isInterruptionRequested():
            #     print("IPColor线程被中断")
            #     break
            try:
                self.set_win_title.emit(f"设备列表 -- 正在测试IP可用性：{i[0]}")
                if i[0] == "local IP":
                    r = requests.get(f"http://127.0.0.1/", timeout=1)
                else:
                    r = requests.get(f"http://{i[0]}/", timeout=1)
                if r.status_code == 200:
                    self.set_item_color.emit([i[1], (0, 255, 0)])
            except:
                self.set_item_color.emit([i[1], (255, 0, 0)])

        self.set_win_title.emit("设备列表 -- IP可用性测试完成,查看右侧在线状态。")
