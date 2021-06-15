#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
converts extracted annotations from text to audio using Mac's say command.
"""

import sys
import os

def main():
   narrator = sys.argv[1]
   voice = sys.argv[2]
   filepath = sys.argv[3]

   if not os.path.isfile(filepath):
       print("File path {} does not exist. Exiting...".format(filepath))
       sys.exit()
  
   with open(filepath) as fp:
       cnt = 0
       old_frame = 1
       for line in fp:
           # print("line {} contents {}".format(cnt, line))
           if ( len(line) > 1 ):
               if ( line[1] == "*" ):
                   num = int(line[8:11].strip().split(':')[0])
                   print("talk frame at ", num )
                   os.system("say"+' -v '+voice+' "'+line[11:]+'" -o frames/frame{0:03d}.aiff'.format(num))
                   for quiet_frame in range(old_frame,num):
                       print("quiet frame at ",quiet_frame)
                       if (quiet_frame == 1):
                           os.system("say"+' -v '+voice+' "'+
                               "[[slnc 1000]] This presentation is read by, "+
                               narrator+", using the voice of, "+voice+
                               "[[slnc 2000]]"+'" -o frames/frame{0:03d}.aiff'.format(quiet_frame))
                       else:
                           os.system("say"+' -v '+voice+' "'+"[[slnc 5000]]"+'" -o frames/frame{0:03d}.aiff'.format(quiet_frame))
                   old_frame=num+1
           cnt += 1
  
if __name__ == '__main__':
    main()
