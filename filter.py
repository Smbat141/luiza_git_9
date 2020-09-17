import re

keyword = input('Find: ')

with open('sample_data.csv') as f:
    data = f.read().split(',')
    data = ''.join(data)
    
    result = re.findall(keyword + r'[ a-zA-Z]{0,}"', data)
    
    if result:
        for name in result:
            print(name[0:-1])
    else:
        print('Not Found')
        
    
    
    
    