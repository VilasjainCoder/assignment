# First product
product_price1 = int(input("Enter the price of the first product: "))
product_gst1 = (product_price1 / 100) * 20
mrp1 = product_price1 + product_gst1
print("\nFor the first product:")
print("Product Price:", product_price1)
print("Product GST:", product_gst1)
print("MRP of product:", mrp1)

# Second product
product_price2 = int(input("Enter the price of the second product: "))
product_gst2 = (product_price2 / 100) * 20
mrp2 = product_price2 + product_gst2
print("\nFor the second product:")
print("Product Price:", product_price2)
print("Product GST:", product_gst2)
print("MRP of product:", mrp2)
