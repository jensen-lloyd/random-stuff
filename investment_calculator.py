while True:

    balance = float(input("Starting balance in $: "))
    percentage_profit = float(input("Percentage profit per day: "))
    time = int(input("Days: "))

    decimal_profit = (percentage_profit+100)*0.01

    for i in range(time):
        balance = balance*decimal_profit

    print("End balance: " + str(balance) + "\n")
