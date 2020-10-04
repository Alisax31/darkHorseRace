import re
import pandas as pd

def import_file(file):
    BOM = b'\xef\xbb\xbf'
    existBom = lambda s: True if s == BOM else False
    f = open(file, mode='rb')
    if existBom(f.read(3)):
        fbody = f.read()
        with open(file, mode='wb') as f:
            f.write(fbody)
    f.close()
    f = open(file, encoding='utf-8', mode='r')
    data = f.read()
    return data

def error_character_clean(data):
    data = data.replace(',.', ',')
    data = re.sub(r'\",\d', '\",', data)
    data = re.sub(r'\"\d\}', r'\"\}', data)
    data = re.sub(r',\"\"', ',\"', data)
    data = re.sub(r'.\}', '}', data)
    data = re.sub(r':\}', '}', data)
    file_name = 'g.txt'
    with open(file_name, 'w') as file_object:
        file_object.write(data)
    return data

def torqueArray_extract(data):
    data = re.findall(r'\"TorqueArray\": \"\S*\",', data)
    tor_str = ""
    tor_list = []
    # n = 1
    for item in data:
        tor_str = str(item)
        tor_str = tor_str.replace(",', '", ',')
        tor_str = tor_str.replace(",'", '')
        tor_str = tor_str.replace("\",", '')
        temp = tor_str.split("\": \"")
        # print("line ",n)
        # print(temp[1])
        # n += 1
        tor_list.append(temp[1])
    return tor_list

def angleArray_extract(data):
    data = re.findall(r'\"AngleArray\": \"\S*\"', data)
    ang_str = ""
    ang_list = []
    for item in data:
        ang_str = str(item)
        #ang_str = ang_str.replace(",', '", ',')
        #ang_str = ang_str.replace(",'", '')
        #ang_str = ang_str.replace("\",", '')
        temp = ang_str.split("\": \"")
        # print(temp[1])
        temp[1] = temp[1].replace('\"', '')
        ang_list.append(temp[1])
    return ang_list

def record_id_extract(data):
    data = re.findall(r'\"RecordID\": \d*', data)
    record_id_list = []
    temp = ""
    for item in data:
        temp = item.split(': ')
        record_id_list.append(temp[1])
    return record_id_list

def create_dataframe(tor_data, ang_data, record_id_data):
    result = {}
    for i in range(len(tor_data)):
        result[record_id_data[i]] = [tor_data[i],ang_data[i]] 
    dataframe = pd.DataFrame(result, index=['Torque','Angle'])
    dataframe = dataframe.unstack()
    return dataframe

'''
def safe_float(num):
    try:
        return float(num)
    except:
        l = len(num)
        if l % 2 == 0 and num != '':
            i = int(l / 2)
            return float(num[0:i])
        elif l % 2 != 0:
            # if '-' not in num:
            #     # dot = num.index('.')
                # dot_substr = num[0:dot]
            num_split = num.split('.')
            temp1 = len(num_split[0])
            temp2 = len(num_split[1]) - temp1
            return float(num_split[1][temp2:len(num_split[1])]+'.'+num_split[2])
            # elif num.index('-') == 0:
            #     dot = num.index('.')
            #     dot_substr = num[1:dot]
            #     num_split = num.split(dot_substr)
            #     return float(num_split[0]+dot_substr+num_split[1])                            
        elif num == '':
            return None
'''