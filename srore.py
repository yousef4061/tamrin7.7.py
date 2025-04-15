PRODUCTS = []

def read_from_database():
    try:
        with open('database.txt', 'r') as f:
             for line in f:
                if line.strip():
                    result = line.split(",")
                    if len(result) == 4:
                        my_dict ={"code": result[0], "name": result[1], "price": result[2], "count": result[3]}
                        PRODUCTS.append(my_dict)
    except FileExistsError:

        with open('database.txt', 'w') as f:
            pass
    f.close()


def write_to_database():  
    with open('database.txt', 'w') as f:
        for product in PRODUCTS:
            line = f"{product['code']}, {product['name']}, {product['price']}, {product['count']}\n"
            f.write(line)


def show_menu():
    print("1- Add")
    print("2- Edit")
    print("3- Remove")
    print("4- search")
    print("5- show List")
    print("6- Buy")
    print("7- Discount")
    print("8- Exit")
    

def add():
    try:
        code = input("enter code: ")
        name = input("enter name: ")
        price = int(input("enter price: "))
        count = int(input("enter count: "))
        new_product = {'code': code, 'name': name, 'price': price, 'count': count}
        PRODUCTS.append(new_product)
        write_to_database()
        print("product added successfully!")
    except ValueError:
        print("Error: price and count must be numbers!")

def edit():
    code = input("enter product code to edit: ")
    for product in PRODUCTS:
        if product['code'] == code:
            try:
                product['name'] = input("enter new name: ")
                product['price'] = int(input("enter new price: "))
                product['count'] = int(input("enter new count: "))
                write_to_database()
                print("product updated successfully!")
                return
            except ValueError:
                print("Error: price and Count must be numbers!")
                return
    print("Product not found!")

def remove():
    code = input("enter product code to remove: ")
    for product in PRODUCTS:
        if product['code'] == code:
            PRODUCTS.remove(product)
            write_to_database()
            print("Product removed successfully!")
            return
        print("product not found!")

def search():
    user_input = input("type your keyword: ")
    for product in PRODUCTS:
        if product["code"] == user_input or product["name"] == user_input:
            print(product["code"], "\t\t", product["name"], "\t\t", product["price"])
            return
    else:
        print("not fount")
        
def show_list():
    if not PRODUCTS:
        print("no product available!")
    else:
        for product in PRODUCTS:
            print(product["code"], "\t\t", product["name"], "\t\t", product["price"])

def buy():
    print("DEBUG: entering buy() function")
    code = input("enter product code to buy: ").strip()
    print(f"DEBUG: code entered: {'code'}")
    if not code:
        print("DEBUG: code is empty!")
        print("error: product code cannot be empty!")
        return
    print(f"DEBUG: current PRODUCTS list: {PRODUCTS}")
    for product in PRODUCTS:
        print(f"DEBUG: checking product with code: {product['code']}")
        if product['code'] == code:
            while True:
                quantity_input = input("enter quantity to buy: ").strip()
                print(f"DEBUG: quantity input received: '{quantity_input}'")
                if not quantity_input:
                    print("DEBUG: quantity input is empty!")
                    print("error: quantity cannot be empty! please enter a number.")
                    continue
                try:
                    quantity = int(quantity_input)
                    print(f"DEBUG: quantity converted to int: {quantity}")
                    if quantity <= 0:
                        print("DEBUG: quantity is less than or equal to 0!")
                        print("quantity must be greater than 0!")
                        return
                    if quantity > product['count']:
                        print("DEBUG: quantity exceeds stock!")
                        print("not enough stock available!")
                        return
                    product['count'] -= quantity
                    write_to_database()
                    print(f"DEBUG: updated product count: {product['count']}")
                    print(f"successfully bought {quantity} of {product['name']}!")
                    return
                except ValueError:
                    print("DEBUG: ValueError occurred while converting quantity!")
                    print("error: quantity must be a number!")
                    return
        print("DEBUG: product not fount in loop!")
    print("product not found!")

def discount():
    code = input("Enter product code to apply discount: ").strip()
    if not code:
        print("Enter product code cannot be empty!")
        return
    for product in PRODUCTS:
        if product['code'] == code:
            while True:
                discount_input = input("Enter discount percentage (0-100): ").strip()
                if not discount_input:
                    print("Error: Discount percentage cannot be empty! please enter a number.")
                    continue
                try:
                    discount = float(discount_input)
                    if discount < 0 or discount > 100:
                        print("Error: Discount percentage must be between 0 and 100!")
                        return
                    original_price = int(product['price'])
                    discount_amount = original_price * (discount / 100)
                    new_price = int(original_price - discount_amount)
                    product['price'] = str(new_price)
                    write_to_database()
                    print(f"Discount applied successfully! New price of {product['name']} is {new_price}.")
                    return
                except ValueError:
                    print("Error: Discount percentage must be a number!")
                    return
    print("product not found!")

print("Welcome to Yousef Store")
print("Loading...")
read_from_database()
print("Data loaded.")

while True:
    show_menu()
    try:
        choice_input = input("enter your choice (1-8): ").strip()
        if not choice_input:
            print("error: no input! please enter a number between 1 and 8.")
            continue
        choice = int(choice_input)
        if choice < 1 or choice > 8:
            print("please enter a number between 1 and 8!")
            continue
        if choice == 1:
            add()
        elif choice == 2:
            edit()
        elif choice == 3:
            remove()
        elif choice == 4:
            search()
        elif choice == 5:
            show_list()
        elif choice == 6:
            buy()
        elif choice == 7:
            discount()
        elif choice == 8:
            write_to_database()
            exit(0)
            print("mese adam vared kon :|")
            break
        else:
            print("please enter a number between 1 and 8!")
    except ValueError:
            print(f"error: '{choice_input}' is not a valid number! please enter a number between 1 and 7.")
            continue
        # for product in PRODUCTS:
        #     print(product)

           