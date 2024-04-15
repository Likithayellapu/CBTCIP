p1_name,p1_price="Apples",10.90
p2_name,p2_price="Milk",5.5
p3_name,p3_price="Eggs",526.90
company_name="Sarvani"
company_address="Malkapuram"
company_city="Vishkhapatnam"
Message="Thank you for shopping with us today! "
print("*"*50)
print("\t\t{}".format(company_name.title()))
print("\t\t{}".format(company_address))
print("\t\t{}".format(company_city))
print("*"*50)
print("\t Product Name \t Product Price")
print("\t{}\t\t {} Rs".format(p1_name.title(),p1_price))
print("\t{}\t\t {} Rs".format(p2_name.title(),p2_price))
print("\t{}\t\t {} Rs".format(p3_name.title(),p3_price))
print("="*50)
total=p1_price+p2_price+p3_price
print("\tTotal \t\t {} Rs".format(total))
print("="*50)
print("\n\t{}\n".format(Message))
print("*"*50)
