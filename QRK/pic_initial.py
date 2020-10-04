import matplotlib.pyplot as plt

def create_pic(df, n):
    i = 0
    while(i < n):
        tor_value = df.iloc[i,2].split(',')
        ang_value = df.iloc[i+1,2].split(',')
        for j in range(len(tor_value)):
            try:
                tor_value[j] = float(tor_value[j])
            except:
                tor_value[j] = tor_value[j-1]
        # tor_value = list(map(safe_float, tor_value))
        # ang_value = list(map(safe_float, ang_value))
        for k in range(len(ang_value)):
            try:
                ang_value[k] = float(ang_value[k])
            except:
                ang_value[k] = ang_value[k-1]       
        print('the',i,'次')
        i += 2
        print(str(i)+' line: '+str(len(tor_value)))
        print(str(i+1)+' line: '+str(len(ang_value)))
        if len(tor_value) != len(ang_value):
            print('错误数据',i,'-----------------------------------------------')
        plt.plot(ang_value, tor_value, '-r')
        plt.savefig(r'QRK/pic/pic'+df.iloc[i,0]+'.png')
        plt.close()