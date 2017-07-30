# w = open('bbb.txt','w')
# with open('aaa.txt','r',encoding='gbk') as f:
#     #for line in f.readline():
#     w.write(f.read().strip('\r\n'))
#
# w.flush()
# w.close()


def delblankline(infile, outfile):
    infopen = open(infile, 'r')
    outfopen = open(outfile, 'w')
    lines = infopen.readlines()
    for line in lines:
        if line.split():
            outfopen.writelines(line)
        else:
            outfopen.writelines("")
    infopen.close()
    outfopen.close()


delblankline("aaa.txt", "bbb.txt")