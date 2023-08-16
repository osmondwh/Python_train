#dictionary 練習

customer_spending = {
    "小白" : 2000,
    "小黑" : 3000,
    "小黃" : 12000,
    "小綠" : 15000,
    "小灰" : 8000
}
for customer in customer_spending:
    if customer_spending[customer] >= 10000:
        customer_spending[customer] = "VIP"
    else:
        customer_spending[customer] = "一般客人"
print(customer_spending)