num = int(input("Enter a number: "))
Num = int(input("Enter a number: "))
print('-----------------------------------------------------------------------------')
for x in range(1, num + 1):
    print('')
    for y in range(1, Num + 1):
        print(f"{y} x {x} = {x * y:<20}", end="\t")


print(" ")