def calculate_sales():
    prices = {
        "popcorn": {"small": 50, "medium": 80, "large": 100},
        "coke": {"small": 30, "medium": 50, "large": 70},
        "chips": {"small": 40, "medium": 80, "large": 120}
    }
    sales = {
        "popcorn": {"small": 0, "medium": 0, "large": 0},
        "coke": {"small": 0, "medium": 0, "large": 0},
        "chips": {"small": 0, "medium": 0, "large": 0}
    }
    for item in sales:
        for size in sales[item]:
            sales[item][size] = int(input(f"Введите количество проданного {item} размера {size}: "))
    total_sales = 0
    for item in sales:
        for size in sales[item]:
            total_sales += sales[item][size] * prices[item][size]

    print(f"Общая сумма продаж: {total_sales} грн.")

if __name__ == "__main__":
    calculate_sales()
