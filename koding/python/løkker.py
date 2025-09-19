# tall = 1
# while tall < 15:
#   print(tall)
#    tall += 1

# while tall > 0:
#   print(tall)
#   tall -= 1


tall = 0
summen = []
while tall < 11:
    print(tall)
    summen.append(tall)
    tall = tall + 1
for items in summen:
    tall = sum(summen)
print(tall)
    