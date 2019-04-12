import re


def callback_dig():
    context = open('source.html', encoding='utf-8').read()
    sheetid = re.search('sheetid: (\d+)', context, re.S).group(1)
    ttid = re.search('ttid: (\d+)', context, re.S).group(1)
    sttid = re.search('sttid=(\d+)', context, re.S).group(1)
    return [ttid, sheetid, sttid]


if __name__ == '__main__':
    s = callback_dig()
    print(s)
