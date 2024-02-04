import timeit

def time_search_algorithm(algorithm, amount):
    return timeit.timeit(lambda: algorithm(amount), number=1)

def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]
    result = {}

    for coin in coins:
        # Визначення кількості монет даного номіналу
        count = amount // coin
        if count > 0:
            result[coin] = count
            # Зменшення залишку суми
            amount -= count * coin

    return result

def find_min_coins(amount):
    coins = [1, 2, 5, 10, 25, 50]
    
    # Ініціалізація таблиці для зберігання мінімальної кількості монет
    dp_table = [float('inf')] * (amount + 1)
    dp_table[0] = 0
    
    # Заповнення таблиці
    for coin in coins:
        for sub_amount in range(coin, amount + 1):
            dp_table[sub_amount] = min(dp_table[sub_amount], dp_table[sub_amount - coin] + 1)

    # Відновлення розв'язку з таблиці
    result = {}
    remaining_amount = amount

    for coin in reversed(coins):
        while remaining_amount >= coin and dp_table[remaining_amount] == dp_table[remaining_amount - coin] + 1:
            if coin in result:
                result[coin] += 1
            else:
                result[coin] = 1
            remaining_amount -= coin

    return result

def main():    
    # Приклад використання:
    amount = 42054

    for amount in [1000, 10000, 100000, 1000000]:
        find_coins_greedy_time = time_search_algorithm(find_coins_greedy, amount)
        print(f"find_coins_greedy | For the sum {amount}, the search time was: {find_coins_greedy_time} seconds")

    for amount in [1000, 10000, 100000, 1000000]:
        find_min_coins_time = time_search_algorithm(find_min_coins, amount)
        print(f"find_min_coins | For the sum {amount}, the search time was: {find_min_coins_time} seconds")


if __name__ == "__main__":
    main()