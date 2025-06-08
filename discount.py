t = int(input())

while t > 0:
    n, x, y = map(int, input().split())
    a = list(map(int, input().split()))
    t -= 1
    # Your code goes here
    #A = calculate without coupon
    original_price = sum(a)
    #calculate with coupon
    discounted_price = 0
    for num in a:
        if num > y:
            discounted_price += (num-y)
            
    #B = sum of coupon and with coupon
    discount_total = discounted_price + x
    
    #if A > B
    if discount_total < original_price:
        print("COUPON")
    else:
        print("NO COUPON")

    
