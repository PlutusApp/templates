import random

def poor_big_spender():
    data = [0,0,0,0,0,0]
    age = random.randint(16, 80)
    total_income = random.randint(6000, 40000)+random.randint(-1, 1)*random.randint(1000, 3000)
    monthly_income = total_income/12.0
    rcs = -0.6
    for i in range(0,12):
        poor_status = random.uniform(0, 0.5)
        saving_rate = random.uniform(0,3)
        spending_rate = random.uniform(7,10)
        monthly_expenditure = monthly_income/saving_rate
        account_total = total_income*(1.0-poor_status)
        rcs = (monthly_income-monthly_expenditure)/monthly_income
        data = [x + y for x, y in zip(data, [monthly_income, monthly_expenditure, total_income, rcs, age, account_total])]
    data = [x / 12 for x in data]
    return data


def saver_big_spender():
    data = [0,0,0,0,0,0]
    age = random.randint(16, 80)
    total_income = random.randint(6000, 200000)+random.randint(-1, 1)*random.randint(1000, 3000)
    monthly_income = total_income/12.0
    rcs = -0.6
    for i in range(0,12):
        poor_status = random.uniform(0, 1)
        saving_rate = random.uniform(7,10)
        spending_rate = random.uniform(7,10)
        monthly_expenditure = monthly_income/saving_rate
        account_total = total_income*(1.0-poor_status)
        rcs = (monthly_income-monthly_expenditure)/monthly_income
        data = [x + y for x, y in zip(data, [monthly_income, monthly_expenditure, total_income, rcs, age, account_total])]
    data = [x / 12 for x in data]
    return data



if __name__ == "__main__":
    for i in range(0, 100):
        print(saver_big_spender())
