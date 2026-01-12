from lib.calc import Calc

if __name__ == "__main__":
    number_of_items = int(input("How many? "))
    price_per_item = int(input("What is the price? "))
    state_code = input("What is the state code? ")

    total = Calc().calc(number_of_items, price_per_item, state_code)
    print(total)
