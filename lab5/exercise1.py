def km_to_mi(km):
    return km * 0.6214

km = float(input("enter distance in kilometers: "))
print(km, "kilometers =", km_to_mi(km), "miles")