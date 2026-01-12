from lib.calc import Calc

class InputValidator:
    def validate(self, input):
        try:
            return int(input)
        except ValueError:
            print(f"{input} is not a number")
            exit(1)

if __name__ == "__main__":
    validator = InputValidator()
    number_of_items = validator.validate(input("How many? "))
    price_per_item = validator.validate(input("What is the price? "))
    state_code = input("What is the state code? ")

    total = Calc().calc(number_of_items, price_per_item, state_code)
    print(total)
