import re,math

def getNetworkAddress(ip, mask):
    separator = "."
    networkAddress = ""
    ipSplit = ip.split(separator)
    maskSplit = mask.split(separator)
    for i in range(len(ipSplit)):
        ipSplitInt = int(ipSplit[i])
        maskSplitInt = int(maskSplit[i])
        if(i == 0):
            networkAddress = str(ipSplitInt & maskSplitInt)
        else:
            networkAddress = networkAddress + separator + str(ipSplitInt & maskSplitInt)
    return networkAddress
 
def isMultipleof16(n):
    while (n > 0):
        n = n-16
    if (n == 0):
        return 1
    return 0 

def toBin(x):
    return toBin(x//2) + [x%2] if x > 1 else [x]   
        
def getHostPartIndex(ip):
    if(getClass(ip) == 'A'):
        return 1
    if(getClass(ip) == 'B'):
        return 2
    if(getClass(ip) == 'C'):
        return 3

def getClass(ip):    
    ipSplit = ip.split(".")
    ipSplitToInt = int(ipSplit[0])
    if  1 <= ipSplitToInt <= 126:
        return "A"
    if 128 <= ipSplitToInt <= 191:
        return "B"
    if 192 <= ipSplitToInt <= 223:
        return "C"
    else:
        raise Exception("Invalid Ip")    

def checkIpv4Format(ip, maskOrIp):
    ipSplit = ip.split(".")
    count = len(ipSplit)
    errorMessage = "Invalid Ip Address"
    if(maskOrIp == "masque"):
        errorMessage = "Invalid Mask Address"
    if(count != 4):
        raise Exception(errorMessage)
    for i in range(len(ipSplit)):
        try:
            ipSplitToInt = int(ipSplit[i])
        except:
            raise Exception(errorMessage)
        finally:
            if ipSplitToInt < 0 or ipSplitToInt > 255:
                raise Exception(errorMessage) 

def intToHexWith0(n):
    binTemp = bin(int(n, 16))
    binTemp = int(binTemp,2)
    binTemp =  format(binTemp, '#016b')
    binTemp = binTemp[2:]     
    return binTemp

def getMask(ip):
    if(getClass(ip) == "A"):
        return "255.0.0.0"
    if(getClass(ip) == "B"):
        return "255.255.0.0"
    if(getClass(ip) == "C"):
        return "255.255.255.0"        

def onesComplement(n):
    if(n == 0):
        return 255
    number_of_bits = (int)(math.floor(math.log(n) / math.log(2)))+1;
    return ((1 << number_of_bits) - 1) ^ n;

def getBroadcatAddress(ip, mask):
    broadcast = ""
    ipSplit = ip.split(".")
    maskSplit = mask.split(".")
    for i in range(len(ipSplit)):
        if i == 0:
            broadcast = str(onesComplement(int(maskSplit[i])) |  int(ipSplit[i]))
        else:
            broadcast = broadcast + "." + str(onesComplement(int(maskSplit[i])) |  int(ipSplit[i]))
    return broadcast

def binaryStringToHex(hexa):  
    binary_string = hexa
    return '%0*X' % ((len(binary_string)+3) // 4, int(binary_string, 2))

def getLastOrder(ip, mask):
    separator = "."
    lastOrder = str(int(getBroadcatAddress(ip, mask).split(separator)[0])) + separator + str(int(getBroadcatAddress(ip, mask).split(separator)[1])) + separator + str(int(getBroadcatAddress(ip, mask).split(separator)[2])) + separator + str(int(getBroadcatAddress(ip, mask).split(separator)[3])-1)
    return lastOrder

def getFirstOrder(ip, mask):
    separator = "."
    firstOrder = str(int(getNetworkAddress(ip, mask).split(separator)[0])) + separator + str(int(getNetworkAddress(ip, mask).split(separator)[1])) + separator + str(int(getNetworkAddress(ip, mask).split(separator)[2])) + separator + str(int(getNetworkAddress(ip, mask).split(separator)[3]) + 1)
    return firstOrder

def decimalToSubnet(n):
    if n == 1:
        return 128 
    if n == 2:
        return 192
    if n == 3:
        return 224
    if n == 4:
        return 240
    if n == 5:
        return 248
    if n == 6:
        return 252
    if n == 7:
        return 254
    if n == 8:
        return 255                      

def hostBit(ip):
    return (4-getHostPartIndex(ip))*8

def getAddressNumber(ip):    
    numberOf = pow(2,hostBit(ip))-2
    return numberOf