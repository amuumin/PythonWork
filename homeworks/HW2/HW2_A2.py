#Amina Muumin, muumi002, 008 HW2_A2
def subtractFor(total, num, times):
    for i in range(times):
        value = total - (num * times)
        print(value)

    
def main():
        total = float(input("Enter a the current total: "))
        num = float(input("What number will be subtracted? "))
        times = float(input("How many times should we subtract? "))
        newestvalue= total - (num * times)
        print("Answer: ", newestvalue)
main()
