import sys
import os
words = sys.stdin.read().split()
windowSize = 5
#fetch = 'fetch.txt'
#Convert this to a function so you can specify all this
#overlap
try:
    fetch = os.environ[source_document]
    fetch = fetch.split('/')[-1]
except KeyError:
    pass
    
for i in range(0, len(words)-windowSize): # - windowsize - overlap
        outStr = ''
        for j in (0,1,2):
                outStr += words[i+j]            
                if( j < 2): #handles space indentation
                        outStr += '_'
        print '%s_%s' % (outStr, 1) +'_'+'%s_' % i + '%s_' %  (i+windowSize) + '%s_' % fetch
        #print outStr + " [EndPosition = " + (words[0 + windowSize]) + "]"
        #need to store global variables as SP and EP that can be used later
        #
        
        outStr = ''
        for j in (0,1,3):
                outStr += words[i+j]   
                if( j < 3): #handles space indentation
                        outStr += '_'             
        print '%s_%s' % (outStr, 1) +'_'+'%s_' % i + '%s_' %  (i+windowSize) + '%s_' % fetch
        
        outStr = ''
        for j in (0,2,3):
                outStr += words[i+j]   
                if( j < 3): #handles space indentation
                        outStr += '_'             
        print '%s_%s' % (outStr, 1) +'_'+'%s_' % i + '%s_' %  (i+windowSize) + '%s_' % fetch
        
        outStr = ''
        for j in (0,2,4):
                outStr += words[i+j]   
                if( j < windowSize - 1): #handles space indentation
                        outStr += '_'             
        print '%s_%s' % (outStr, 1) +'_'+'%s_' % i + '%s_' %  (i+windowSize) + '%s_' % fetch