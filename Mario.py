# the function that print
def show(star):
    for i in range(1,(star+1)):
        # print ' ' + # + ' ' + #
        print(' '*(star-i) + '#'*i + ' ' + '#'*i)

def main():
    try:
        val = int(input("Insert a number: "))
    except:
        # make sure it's a valid number
        print('This is not a valid number!')
        exit()
    # check if the value is negatif
    if val < 0:
        print('Please insert a positive Integer!')
        exit()
    # call the function
    show(val)

main()