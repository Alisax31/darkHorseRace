import re
import pandas as pd
import file_dispose as fd
import matplotlib.pyplot as plt
import pic_initial as pi

if __name__ == '__main__':
    fpath = r'QRK/GetTightenDataList.txt'
    data = fd.import_file(fpath)
    tor_data = fd.torqueArray_extract(data)
    ang_data = fd.angleArray_extract(data)
    record_id_data = fd.record_id_extract(data)
    df = fd.create_dataframe(tor_data, ang_data, record_id_data)
    df = df.reset_index()
    # print(df)
    n = len(tor_data)
    print(n)
    # p;pi.create_pic(df,n)    