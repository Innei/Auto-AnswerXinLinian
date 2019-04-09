#!python3
import random
import requests
from prase_dig import *

root = "http://192.168.9.12/npels/"
answerurl = root + "/Student/viewTestTask.aspx"
ctoken = None
s = requests.session()


def randomnocache():
    return str(random.random())


def getanswer(part, ttid, sheetid, sttid):
    data = "action=getPart&partnum=" + str(part) + "&ttid=" + str(ttid) + "&sheetid=" + str(sheetid) + "&sttid=" + str(
        sttid) + "&nocache=" + randomnocache()
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Referer": "http://192.168.9.12/npels/student/viewTestTask.aspx",
        "Content-Type": "application/x-www-form-urlencoded",
    }
    ans = s.post(url=answerurl, data=data, headers=headers)
    if ans.text.find("服务器错误") == -1:
        return ans.text


def answer(ttid, sheetid, sttid):
    fo = open("EnglishAnswer.html", "w+")
    try:
        fo.write(getanswer(1, ttid, sheetid, sttid))
        fo.write(getanswer(2, ttid, sheetid, sttid))
        fo.write(getanswer(3, ttid, sheetid, sttid))
        fo.write(getanswer(4, ttid, sheetid, sttid))
    except:
        pass;
    finally:
        fo.close()

def prase_result():
    dig = callback_dig()
    answer(dig[0], dig[1], dig[2])
    print('解析成功')

