import re

keyword = input('Find: ')
count = int(input ("count: "))
with open('sample_data.csv') as f:
    data = f.read().split(',')
    data = ''.join(data)
    result = re.findall(keyword + r'[ a-zA-Z]{0,}"', data)
    if result:
        for name in result:
            print(name[0:-1])
            count -= 1
            if not count:
                break
    else:
        print('Not Found')
