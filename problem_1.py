from collections import Counter

myfile = open("/home/dalgarno/Documents/GAW/data-sets/bed/lamina.bed", 'r')
mybed = [line.split('\t') for line in myfile]

mychroms = [i[0] for i in mybed[2:]]

mychroms = (Counter(mychroms))
mymaxkey = (max(mychroms.keys(), key=(lambda key: mychroms[key])))


print(mymaxkey, mychroms[mymaxkey])
