class Calc:

    def calc(self, number_of_items, price_per_item, state_code):

        sub_total = number_of_items * price_per_item

        discount = self.sales_discount(sub_total)

        sub_sub_total = sub_total - discount

        total = sub_sub_total + self.sales_tax(sub_sub_total, state_code)

        return [total, number_of_items, price_per_item, state_code]

    def sales_discount(self, sub_total):
        return 0.5

    def sales_tax(self, sub_total, state_code):

        taxes = {
                "UT": 0.0685,
                "NV": 0.08,
                "TX": 0.0625,
                "AL": 0.04,
                "CA": 0.0825
                }
        return sub_total * taxes[state_code]


