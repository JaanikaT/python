# yl26

# https://www.reddit.com/r/dailyprogrammer/comments/8xzwl6/20180711_challenge_365_intermediate_sales/

# Lisatasu arvutamise ülesanne. Alusta algoritmi koostamisest. 
# Kommentaarides on kah lahendused, aga proovi ise lahendada. 
# Defineeri lisatasu arvutamise funktsioon. 
# Sisendina defineeri dictionary.

""" def commission(Frank):
    monthly_commission = 0
    tea = int(Frank["tea_revenue"]) - int(Frank["tea_expences"])
    if tea > 0:
        monthly_commission += tea*0.062
    
    coffee = int(Frank["coffee_revenue"]) - int(Frank["coffee_expences"])
    if coffee > 0:
        monthly_commission += coffee*0.062    
    print("Frank: ", monthly_commission) """     

def commission(name, tea_revenue, tea_expences, coffee_revenue, coffee_expences):
    monthly_commission = 0
    tea = int(salesperson["tea_revenue"]) - int(salesperson["tea_expences"])
    if tea > 0:
        monthly_commission += tea*0.062
    
    coffee = int(salesperson["coffee_revenue"]) - int(salesperson["coffee_expences"])
    if coffee > 0:
        monthly_commission += coffee*0.062    
    print(name, round(monthly_commission,2))  


""" salesperson = {
    "name": "Frank",
    "tea_revenue": "120",
    "coffee_revenue": "243",
    "tea_expences": "130",
    "coffee_expences": "143"
    } """

salesperson = {
    "name": "Jane",
    "tea_revenue": "145",
    "coffee_revenue": "265",
    "tea_expences": "59",
    "coffee_expences": "198"
    } 

commission(**salesperson)

"""Revenue 

        Frank   Jane
Tea       120    145
Coffee    243    265

Expenses

        Frank   Jane
Tea       130     59
Coffee    143    198"""