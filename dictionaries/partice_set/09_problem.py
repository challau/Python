# friends = {
#     "uday":6281211993 ,
#     "teja sree":900529191,
#     "Dasappa":9381753377
# }
# print(friends.keys())
# print(friends.values())
# print(friends.items())





# list = [1,2,3,4,5,5]
# s = set(list)
# print(s)


# given a dictionary of products and their prices, find the products with the highest price

products = {
    "laptop":50000,
    "Phone":30000,
    "Tablet":20000,
    "Headphones":5000
}

highest_product = max(products,key = products.get)
print("Products with highest price:", highest_product)

print("price: ",products[highest_product])




# write a program that merges two dictionaries into one

dict1 = {
    "name": "uday",
    "age":20
}


dict2 = {
    "course": "B.tech CSE",
    "college":"DSU"
}


merge_dict  = {**dict1,**dict2}
print(merge_dict)