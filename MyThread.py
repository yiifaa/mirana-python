# -*- coding: UTF-8 -*-

import threading
from time import sleep, ctime
from datetime import datetime

loops = [36, 37]

def fabic(n):
    result = [0, 1, 1]
    if(n < 2):
        return 1
    while(n > 2):
        result.pop(0)
        result.append(result[0] + result[1])
        n = n - 1
    else:
        return result[2]
    #return result.pop()


def fobi(n):
    if(n < 1):
        raise Exception('the argument can not less than 0')
    if(n == 1 or n ==2):
        return 1
    return fobi(n - 1) + fobi(n - 2)

def loop(index, sec):
    #hint = 'start loop ', index, ' at: ', ctime(), '\n'
    #print hint
    #sleep(sec)
    #hint = 'end loop ', index, 'at:', ctime(), '\n'
    #print hint
    print datetime.now()
    startTime = datetime.now()
    fobi(sec)
    expand = datetime.now() - startTime
    print datetime.now()
    print 'My name is {username}, age is {age}!\n'.format(**{'username':index, 'age':expand})

def main():
    #print 'starting at:', ctime()
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        t = threading.Thread(target = loop, args=(i, loops[i]))
        threads.append(t)
    
    for i in nloops:
        threads[i].start()
    
    for i in nloops:
        #threads[i].join()
        pass
    #print 'ending at:', ctime()


if __name__ == '__main__':
        startTime = datetime.now()
        #print 'starting at:', datetime.now()
        print fabic(50)
        #main()
        print datetime.now() -startTime
        #print 'expend times:'
