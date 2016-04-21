#queing script
import os
import boto.emr
import time
import subprocess
import re
from urlparse import urlparse
from urllib import *
a = []; awsarray = []; x = 0; y = 1;
a.append('default')
#a.append('default')
while (1 == 1):
        req = urlopen("http://agboxml.appspot.com/file")
        content = req.read()
        content1 = content
        content2 = 'wait'
        a.append(content1)
        print set(a); awsarray = set(a); #awsarray.pop()
        if len(awsarray) > 2: #because of default
                runner = os.system("python runboto.py")
                print 'we have started Indexing!'
                awsarray = ' '
                #result = subprocess.check_output(runner, shell=True) 
                #os.system("runner >> runner.txt"
        if content1 != ' ':
                #then we have a new content
                time.sleep(3)
                print 'we await new requests!!!'
                content2  = content1
                if a[x] != a[y]:
                        x += 1; y += 1;
                        content1 = ' '
                #now content1 is nothing again
