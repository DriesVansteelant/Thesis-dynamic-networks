from tqdm import tqdm
import time
import numpy as np

inPath = '../Code/Data/tgbl-wiki_edgelist_v2.csv'
outPath = '../Code/Data/tgbl-wiki_edgelist_final.txt'
outPath2 = '../Code/Data/tgbl-wiki_edgelist_final_with_intervals.txt'
outPath3 = '../Code/Data/tgbl-wiki_edgelist_final_h.txt'
outPath4 = '../Code/Data/tgbl-wiki_edgelist_final_with_intervals_h.txt'

outp = open(outPath, 'w')
outp.write('')
outp.close()

outp = open(outPath, 'a')


inp = open(inPath, 'r')

outp2 = open(outPath2, 'w')
outp2.write('')
outp2.close()
outp2 = open(outPath2, 'a')

outp3 = open(outPath3, 'w')
outp3.write('')
outp3.close()
outp3 = open(outPath3, 'a')

outp4 = open(outPath4, 'w')
outp4.write('')
outp4.close()

outp4 = open(outPath4, 'a')

print(inp.readline())
line = inp.readline()
start = time.time()

outp3.write("s d ts\n")
outp4.write("s d ts ts2\n")

while line:
    s = line.strip().split(',')

    # brol = s.pop()
    source = s[0]
    target = s[1]
    # ts2 = float(ts)+50
    ts = str(int(float(s[2])))
    ts2 = str(int(np.floor(float(ts)+1000)))

    # print(source, target, ts)
    newline = source + " " + target + " " + ts + "\n"
    newline2 = source + " " + target + " " + ts + " " + ts2 + "\n"

    # print(newline)
    # print(newline2)

    outp.write(newline)
    outp2.write(newline2)
    outp3.write(newline)
    outp4.write(newline2)
    line = inp.readline()

inp.close()
outp.close()
outp2.close()
outp3.close()
outp4.close()

end = time.time()
print(f"Time taken to format graph {end-start} seconds")