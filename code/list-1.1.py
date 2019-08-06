principal = 1000 # Initial amount (本金)
rate = 0.05   # Interest rate (利率)
numyears = 5  # Number of years (期数,年)
year = 1
while year <= numyears:          
    principal = principal * (1 + rate)
    print(year, principal)
    year += 1
