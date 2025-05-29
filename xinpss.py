def tamiz(wowrude:str)->str:
    """
    tamiz kardan vooroodi
    :param wowrude: 
    """
    wowrude= wowrude.lower()
    if wowrude.find('@'):
        wowrude = wowrude.split('@')[0]
    wowrude.replace(" ", "") \
        .replace("https", "") \
        .replace("http", "") \
        .replace("www", "") \
        .replace("/", "") \
        .replace(":", "")
    return wowrude

pyGah=tamiz(input ("pygah:\n"))
karBar=tamiz(input("karBar:\n"))
ShSHen=tamiz(input('ShenSHomar:\n'))
testhash = str(hash(pyGah + ShSHen + karBar))
testhash = testhash[1]+testhash[1]+testhash[4]+testhash[1]+testhash[3]
test = pyGah[1:3] + '*@' + karBar[1:4] + testhash
print(test)
