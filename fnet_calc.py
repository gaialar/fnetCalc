import sys

#Intake of variables, split them into array of four and cast to integer.
ipv4 = sys.argv[1]
netMask = sys.argv[2]
splitIpv4 = ipv4.split('.', 3)
splitNetMask = netMask.split('.', 3)
ip = map(int, splitIpv4)
mask = map(int, splitNetMask)

offBits = 0;
outPostArr = []
broadCastAddr = []
for i in range(0, 4):
	#Calculate how many zeroes are in mask.
	offBits += (bin(mask[i])[2:].zfill(8)).count('0')
	#Find what network the host is part of
	outPostArr.append(mask[i]&ip[i])
	#Find broadcast address
	broadCastAddr.append(0xFF&(ip[i]|~mask[i]))

#Cast array to string and join with . in between
def conCat(arr):
	string = map(str, arr)
	return '.'.join(string)

#Find of what class the net is.
netClass = ip[0]&192
net = ''
if netClass == 192:
	net = 'C'
elif netClass == 172:
	net = 'B'
elif netClass < 172:
	net = 'A'

print ('This host is part of the following network : ' + conCat(outPostArr) + ', Maximum number of hosts on the network : ' + str((2**offBits) - 2) + 
', the broadcast address is: ' + conCat(broadCastAddr) + ' and the network is a class ' + net + ' net')
