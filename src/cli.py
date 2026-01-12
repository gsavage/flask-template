from lib.calc import Calc

if __name__ == "__main__":
    number = input("How many?")

    total = Calc().calc(number, 0, "UT")
    print(total)
