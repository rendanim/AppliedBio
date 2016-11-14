

out=list()
fp=open('../data/stockholm2')
i=0
for line in fp:
    if(line[0]=='#' or line[0]=='/' or line[0]=='\n'):
        i+=0;
    else:
        i+=1
        out.append(line.split(" ")[0])
print(i)
for k in out:
    print(k)

