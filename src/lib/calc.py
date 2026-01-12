class Calc:

    def calc(self, number_of_items, price_per_item, state_code):

        order_value = number_of_items * price_per_item

        discount = self.sales_discount(order_value)

        sub_total = order_value - discount

        tax = self.sales_tax(sub_total, state_code)

        total = sub_total + tax

        return [total, number_of_items, price_per_item, state_code, order_value, discount, tax]

    def sales_discount(self, order_value):
        if order_value >= 50000:
            return order_value * 0.15
        elif order_value >= 10000:
            return order_value * 0.1
        elif order_value >= 7000:
            return order_value * 0.07
        elif order_value >= 5000:
            return order_value * 0.05
        elif order_value >= 1000:
            return order_value * 0.03
        else:
            return 0

    def sales_tax(self, sub_total, state_code):

        taxes = {
                "UT": 0.0685,
                "NV": 0.08,
                "TX": 0.0625,
                "AL": 0.04,
                "CA": 0.0825
                }
        return sub_total * taxes[state_code]


