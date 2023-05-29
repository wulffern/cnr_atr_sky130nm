#!/usr/bin/env python3



cell = """
        { "name" : "{type}CH_{contacts}C{f_int}F{f_frac}",
          "inherit" : "{type}CH",
          "abstract" : 0,
          "verticalMultiplyVector" : [1.2,1,{f},1,{f},1,1.2],
          "afterNew":{
              "copyColumns": [
                  {
                      "count": {count},
                      "offset": 8,
                      "length": 3
                  }
              ]
          }
        }"""

types = ["P","N"]
contacts = [2,4,8,12]
lengths = [1.2,2,4,8,12]

#- Generate all transistors
cells = list()
for t in types:
    for c in contacts:
        for f in lengths:
            f_frac = (f % 1)*10
            print(f_frac)
            ss = cell.replace("{type}",t) \
            .replace("{contacts}",str(c)) \
            .replace("{count}",str(int(c/2-1))) \
            .replace("{f}",str(f)) \
            .replace("{f_int}",str(int(f))) \
            .replace("{f_frac}",str(round(f_frac)))
            cells.append(ss)

N = len(cells)

with open("../cic/alltran.json","w") as fo:
    fo.write("""
{
   "cells" : [
""")
    for i in range(0,N):
        st = cells[i]
        if(i <N-1):
            st += ","
        fo.write(st)
    fo.write("""
   ]
}
""")
