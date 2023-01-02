filepath='test.log'
mesage='\nline\rline\rline.'
file=open(filepath,'a')
file.write(mesage)
file.close()
#
# file=open(filepath,'r')
# for line in file.readlines():
#     print(line)
# print(file)
# file.close()

file=open(filepath,'w')
file.write('...')
file.close()

file=open(filepath,'r')
for line in file.readlines():
    print(line)
file.close()