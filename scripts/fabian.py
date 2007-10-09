#! /usr/bin/env python

from Tkinter import *
from Fabian import appWin

##########################
#   Main                 #
##########################
if __name__=='__main__':
    from Fabian import appWin
    import sys
    def start():
        import time
        t1=time.clock()
        if len(sys.argv) > 2:
            print "Only the first file will be opened"
        if len(sys.argv) >= 2:
            f=sys.argv[1]
        else:
            f=None
  
        root=Tk()
        mainwin = appWin.appWin(root,filename=f,zoomfactor=0.5,mainwin='yes')
    
        t2=time.clock()
        print "time:",t2-t1
        root.mainloop()
    start()
