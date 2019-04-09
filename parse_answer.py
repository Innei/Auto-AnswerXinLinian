import re
from random import randint, choice


def main(w=0):
    content = open('./EnglishAnswer.html').read()
    result = re.findall('答案：</span>([A-Z])</li>', content, re.S)
    section_b = re.findall(
        '答案：</span>([A-Z])、([A-Z])、([A-Z])、([A-Z])、([A-Z])、([A-Z])、([A-Z])、([A-Z])、([A-Z])、([A-Z])</li>', content, re.S)
    print(section_b)
    for item in section_b:
        for i in item:
            result.insert(-10, i)

    print(result)
    for w in range(0, w):
        r = randint(1, 20)
        result[r] = choice('ABCD')
        print(str(r) + '题答案被更换为' + result[r])
    return result


def callback(w):
    ans = main(w)
    return ans


if __name__ == '__main__':
    main()
