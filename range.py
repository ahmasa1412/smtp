def scan(site):
    ur = site.rstrip()
    ch = site.split('\n')[0].split('.')
    ip1 = ch[0]
    ip2 = ch[1]
    ip3 = ch[2]
    taz = str(ip1) + '.' + str(ip2) + '.'
    i = 0
    while i <= 255:
        i += 1
        c = 0
        while c <= 255:
            c += 1
            print "Ranging ==>" + str(taz) + str(c) + '.' + str(i)
            open('Result-iprange.txt', 'a').write(str(taz) + str(c) + '.' + str(i) + '\n')
            
if __name__ == '__main__':
	print('''KONTOL IP RANGE\n''')

nam = raw_input('List Ips  :')
with open(nam) as f:
    for site in f:
        scan(site)
