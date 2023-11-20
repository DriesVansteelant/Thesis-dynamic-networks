from tqdm import tqdm
import time
import numpy as np

inPath = 'tgbl-review_edgelist_v2.csv'
outPath = 'tgbl-review_edgelist_final.txt'
outp = open(outPath, 'w')
outp.write('')
outp.close()

outPath2 = 'tgbl-review_edgelist_final_with_intervals.txt'

outp2 = open(outPath2, 'w')
outp2.write('')
outp2.close()

outp2 = open(outPath2, 'a')
outp = open(outPath, 'a')
inp = open(inPath, 'r')


print(inp.readline())
line = inp.readline()
start = time.time()

outp.write("s d ts\n")
outp2.write("s d ts\n")

while line:
    s = line.strip().split(',')

    # brol = s.pop()
    source = s[1]
    target = s[2]
    # ts2 = float(ts)+50
    ts = str(int(float(s[0])))
    ts2 = str(int(np.floor(float(ts)+1000)))
    # print(source, target, ts)
    newline = source + " " + target + " " + ts + "\n"
    newline2 = source + " " + target + " " + ts + " " + ts2 + "\n"

    # print(newline)
    outp.write(newline)
    outp2.write(newline2)
    line = inp.readline()

inp.close()
outp.close()
outp2.close()

end = time.time()
print(f"Time taken to format graph {end-start} seconds")