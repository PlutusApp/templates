import random
import json

def poor_big_spender():
    data = [0,0,0,0,0,0]
    age = random.randint(16, 80)
    total_income = random.randint(6000, 40000)+random.randint(-1, 1)*random.randint(1000, 3000)
    monthly_income = total_income/12.0
    rcs = -0.6
    for i in range(1,12):
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
    for i in range(1,12):
        poor_status = random.uniform(0, 1)
        saving_rate = random.uniform(7,10)
        spending_rate = random.uniform(7,10)
        monthly_expenditure = monthly_income/saving_rate
        account_total = total_income*(1.0-poor_status)
        rcs = (monthly_income-monthly_expenditure)/monthly_income
        data = [x + y for x, y in zip(data, [monthly_income, monthly_expenditure, total_income, rcs, age, account_total])]
    data = [x / 12 for x in data]
    return data


def saver_small_spender():
    data = [0,0,0,0,0,0]
    age = random.randint(16, 80)
    total_income = random.randint(6000, 200000)+random.randint(-1, 1)*random.randint(1000, 3000)
    monthly_income = total_income/12.0
    rcs = -0.6
    for i in range(1,12):
        poor_status = random.uniform(0, 1)
        saving_rate = random.uniform(7,10)
        spending_rate = random.uniform(0,3)
        monthly_expenditure = monthly_income/spending_rate
        account_total = total_income*(1.0-poor_status)
        rcs = (monthly_income-monthly_expenditure)/monthly_income
        data = [x + y for x, y in zip(data, [monthly_income, monthly_expenditure, total_income, rcs, age, account_total])]
    data = [x / 12 for x in data]
    return data

def average_spender():
    data = [0,0,0,0,0,0]
    age = random.randint(16, 80)
    total_income = random.randint(6000, 200000)+random.randint(-1, 1)*random.randint(1000, 3000)
    monthly_income = total_income/12.0
    rcs = -0.6
    for i in range(1,12):
        poor_status = random.uniform(0, 1)
        saving_rate = random.uniform(4,7)
        spending_rate = random.uniform(4,7)
        monthly_expenditure = monthly_income/spending_rate
        account_total = total_income*(1.0-poor_status)
        rcs = (monthly_income-monthly_expenditure)/monthly_income
        data = [x + y for x, y in zip(data, [monthly_income, monthly_expenditure, total_income, rcs, age, account_total])]
    data = [x / 12 for x in data]
    return data

if __name__ == "__main__":
    data = []
    targets = []
    for i in range(0, 1000000):
        rand = random.randint(0, 3)
        targets.append(rand)
        if(rand == 0): data.append(poor_big_spender())
        elif (rand == 1): data.append(saver_big_spender())
        elif (rand == 2): data.append(saver_small_spender())
        else: data.append(average_spender())

    file = open('data.txt', 'w')
    file.write(json.dumps(data))
    file.close()

    file = open('targets.txt', 'w')
    file.write(json.dumps(targets))
    file.close()
