import re


def main():
    content = open('./EnglishAnswer.html').read()
    result = re.findall('答案：</span>([A-Z])</li>', content, re.S)
    print(result)
    return result


def callback():
    ans = main()
    return  ans

if __name__ == '__main__':
    main()
