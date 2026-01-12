class Calc:

    def calc(self, number_of_items, price_per_item, state_code):

        sub_total = number_of_items * price_per_item

        total = sub_total + self.sales_tax(sub_total, state_code)

        return [total, number_of_items, price_per_item, state_code]

    def sales_tax(self, sub_total, state_code):

        taxes = {
                "UT": 0.0685
                }
        return sub_total * taxes[state_code]


