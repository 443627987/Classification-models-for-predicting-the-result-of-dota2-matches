import urllib,re

html=urllib.urlopen('https://api.steampowered.com/IDOTA2Match_570/GetMatchDetails/V001/?key=176013BFF606C62BEDCD4982B9332A9C&match_id=1367469919').read()
reg1 = '"hero_id":(-?\d+\.?\d*),'
reg2 = '"match_id1":(-?\d+\.?\d*),'
reg3 = '"radiant_win":(.*?),'
heros = re.findall(reg1,html)
match = re.findall(reg2,html)
outcome = re.findall(reg3,html)
#create title
f = open("C:\Users\jiewei feng\Desktop\data1.txt",'wb')
f.write('Match_ID')
for j in range(1,114+1):
    f.write('\t'+'hero'+str(j))
f.write('\t'+'outcome')
f.close()
f = open("C:\Users\jiewei feng\Desktop\data1.txt",'a')

for i in range(1,3000 + 1):
    print i
    url=urllib.urlopen('https://api.steampowered.com/IDOTA2Match_570/GetMatchDetails/V001/?key=176013BFF606C62BEDCD4982B9332A9C&match_id='+ str(3080204814+1-i)).read()
    reg1 = '"hero_id":(-?\d+\.?\d*),'
    reg2 = '"match_id":(-?\d+\.?\d*),'
    reg3 = '"radiant_win":(.*?),'
    heros = re.findall(reg1,url)
    match = re.findall(reg2,url)
    outcome = re.findall(reg3,url)
    r=[0]
    r=r*115#114 heros, the first column will not be used(which is r[0])
    if len(heros)== 10 and len(match)==1 and len(outcome)==1:
        for n  in range(1,5+1):
            k=heros[n-1]
            k=int(k)
            r[k]=1
        for n  in range(6,10+1):
            k=heros[n-1]
            k=int(k)
            r[k]=-1
        out=[0]
        if outcome[0] =='true':
            out[0] = 1
        else:
            out[0] = 0
        f.write("\n"+match[0])
        for j in range(1,114+1):
            f.write('\t'+str(r[j]))
        f.write('\t'+str(out[0]))
    else:
        continue
f.close()
