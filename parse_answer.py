import re


def main():
    content = open('./EnglishAnswer.html').read()
    result = re.findall('答案：</span>([A-Z])</li>', content, re.S)
    section_b = re.findall(
        '答案：</span>([A-Z])、([A-Z])、([A-Z])、([A-Z])、([A-Z])、([A-Z])、([A-Z])、([A-Z])、([A-Z])、([A-Z])</li>', content, re.S)
    print(section_b)
    for item in section_b:
        for i in item:
            result.insert(-10, i)

    print(result)
    return result


def callback():
    ans = main()
    return ans


if __name__ == '__main__':
    main()
