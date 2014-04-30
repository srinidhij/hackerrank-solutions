#!/usr/bin/python

from collections import defaultdict
features = defaultdict(lambda : 0)
words = open('words.txt').readlines()

for word in words:
    features[word.strip('\n').lower()] += 1

def longest(s):
    l = 0
    ls = ''
    if not s:
        return
    if (len(s)) == 0:
        return 
    for i in s:
        if len(i) > l:
            ls = i
            l = len(i)
    return ls

def segment(ip):
    global features
    ip = ip.lower()
    if len(ip) == 0:
        return
    if ip[0] == '#':
        ip = ip[1:]
    t = ip.find('www.')
    if t != -1:
        ip = ip[t+4:]
    t = ip.find('.')
    if t != -1:
        try:
            int(ip[t+1:])
        except:
            ip = ip[:t]

    segs = []
    while len(ip) != 0:
        possible = []
        flag = False
        for i in range(len(ip)+1):    
            if features[ip[:i]] != 0:
                possible.append(ip[:i])
            try:
                float(ip[:i])
                possible.append(ip[:i])
                flag = True
            except:
                pass

        lw = longest(possible)
        if lw is None :
            break

        try:
            int(lw)
            if int(lw) == float(lw):
                pass
            else:
                lw = int(lw)
        except:
            pass
        segs.append(lw)
        ip = ip[len(lw):]
        
    if ip != '':
        if ip == 's':

            segs[-1] += ip
    if len(segs) == 0:
        print ip
    else:
        print (' ').join(segs)
    
if __name__ == '__main__':
    n = int(raw_input())
    for i in range(n):
        sent = raw_input()
        segment(sent)