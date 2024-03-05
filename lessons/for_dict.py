in_stock: dict[str, bool] = {"carrots": True, "beets": False, "apples": True}

for key in in_stock:
    print(in_stock[key])
    #print(key)

for key in in_stock:
    if in_stock[key]: # when in_stock key is true
        print(key)
