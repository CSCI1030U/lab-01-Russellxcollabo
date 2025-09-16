def main():
    cost_per_item = 19.99
    quantity = 5 
  
    # PART 1
    subtotal_cost = cost_per_item * quantity
    tax = subtotal_cost * 0.13
    total_cost = subtotal_cost + tax

    # PART 2
    print(f'cost_per_item = ${cost_per_item:0.2f}')
    print(f'quantity = {quantity}')
    print(f'subtotal_cost = ${subtotal_cost:0.2f}')
    print(f'tax = ${tax:0.2f}')
    print(f'total_cost = ${total_cost:0.2f}')

    # PART 3
    initial_investment = 1000
    interest_rate = 0.035
    investment = initial_investment

    for _ in range(5):  # repeat 5 times for 5 years
        investment += investment * interest_rate

    print(f'After 5 years, your investment will be worth {investment} dollars.')

main()

