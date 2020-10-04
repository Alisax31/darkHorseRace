    '''
    plt.figure(figsize=(15,5))
    plt.plot(range(len(y_test)), y_test, 'r', label='testdata')
    plt.plot(range(len(y_test)), y_pred, 'b', label='preddata')
    #for a,b in zip(x,y):
    #    plt.text(a,b,'%.0f'%b,ha = 'center',va = 'bottom',fontsize=7)
    plt.legend()    
    plt.show()
    plt.scatter(y_test, y_pred)
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'k--')
    plt.xlabel('test')
    plt.ylabel('pred')
    plt.show()
    '''