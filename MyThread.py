# -*- coding: UTF-8 -*-

import threading
from time import sleep, ctime

loops = [2, 4]

def loop(index, sec):
    hint = 'start loop ', index, ' at: ', ctime(), '\n'
    print hint
    sleep(sec)
    hint = 'end loop ', index, 'at:', ctime(), '\n'
    print hint

def main():
    print 'starting at:', ctime()
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        t = threading.Thread(target = loop, args=(i, loops[i]))
        threads.append(t)
    
    for i in nloops:
        threads[i].start()
    
    for i in nloops:
        threads[i].join()
    print 'ending at:', ctime()


if __name__ == '__main__':
        main()
