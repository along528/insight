def categorize(rpsi):
    if rpsi >=0 and rpsi <=1.3:
        return 0
    elif rpsi > 1.3 and rpsi < 2.5:
        return 1
    else: return 2