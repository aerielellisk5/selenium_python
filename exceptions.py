# ItemsInCart = 0
# # 2 items will be added to cart

# if ItemsInCart != 2:
#     # raise Exception("Products Cart count incorrect")
#     pass

# assert(ItemsInCart == 2)


try:
    with open('text.txt', 'r') as reader:
        reader.read()
except Exception as e:
    print(e)

    # the finally keyword will ALWAYS run 
finally:
    print("cleaning up resources")