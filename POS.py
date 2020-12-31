item_dictionary = {
    1: {'name': 'Potato', 'price': 50},
    2: {'name': 'Apple', 'price': 35},
    3: {'name': 'Orange', 'price': 40},
    4: {'name': 'Banana', 'price': 25},
    5: {'name': 'Popcorn', 'price': 120},
    6: {'name': 'Bottled Water', 'price': 20},
    7: {'name': 'Cola', 'price': 45}
}
cart = {
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0,
}
loop = True
current_tab = 0
current_pointer = 0


def add_or_remove_from_cart(item_no, quantity=1, add_or_remove=1):  # add_or_remove | 1: add | 0: remove
    if quantity > cart[item_no] and add_or_remove == 0:
        cart[item_no] = 0
    else:
        cart[item_no] = cart[item_no] + quantity if add_or_remove == 1 else cart[item_no] - quantity


def ask_for_answer(display_msg='', data_type=0):  # data_type STRING = 1 number = 0 maybe???
    repeat: bool = True
    while repeat:
        if data_type == 0:
            try:
                rcv_msg = int(input(f"{display_msg} "))
                return rcv_msg
            except ValueError:
                print("please input Number")
        elif data_type == 1:
            return input(display_msg).lower()


def display(tab, pointer=0):  # what to display arg: display type | 0: main | 1: items | 2: cart | 3: exit=
    if tab == 0:
        print("Hi, welcome to the Cash Register!")
        print("Select an option below:")
        print("    [1] | Items")
        print("    [2] | Cart/Check-out")
        print("    [0] | Exit")
        return ask_for_answer("Type:", 0)

    elif tab == 1:
        print("Items")
        for item_no, item_info in item_dictionary.items():
            print(
                f"    [{item_no}] | {item_info['name']}{' ' * (20 - len(item_info['name']))} | {item_info['price']} Php")
        print("    [0] | Cancel")
        return ask_for_answer("select item number", 0)

    elif tab == 11:
        return ask_for_answer(f"no. of {item_dictionary[pointer]['name']} you want to add to the cart:", 0)

    elif tab == 2:
        print("Cart")
        count = 0
        for item_no, quantity, item_info in zip(cart.keys(), cart.values(), item_dictionary.values()):
            if quantity > 0:
                count += 1
                print(f"    {item_info['name']}{' ' * (20 - len(item_info['name']))} |"
                      f" {quantity} | {quantity*item_info['price']} Php")
        if count == 0:
            print("    The cart is empty")
            return 0
        else:
            print(
                f"    TOTAL | {sum([item['price'] * quantity for item, quantity in zip(item_dictionary.values(), cart.values())])} Php")
        print("----------------------------------------------------")
        print("    [1] | Remove from the cart")
        print("    [2] | Proceed to Check-out")
        print("    [0] | Exit")
        return ask_for_answer("type: ")

    elif tab == 21:
        print("Remove from Cart")
        for item_no, quantity, item_info in zip(cart.keys(), cart.values(), item_dictionary.values()):
            if quantity > 0:
                print(f"    [{item_no}] | {item_info['name']}{' ' * (20 - len(item_info['name']))} |"
                      f" {quantity} | {quantity*item_info['price']} Php")
        print("    [0] | Cancel")
        return ask_for_answer("type item_no: ")
    elif tab == 211:
        print(f"There are {cart[pointer]} {item_dictionary[pointer]['name']} in your cart")
        print("    [0] | Cancel")
        return ask_for_answer(f"No of {item_dictionary[pointer]['name']} you want to remove: ")
    elif tab == 22:
        print(f"CURRENT TOTAL: {sum([item['price']*quantity for item, quantity in zip(item_dictionary.values(), cart.values())])}")
        input_amount = ask_for_answer("Input the amount you will be paying:")
        PWD = ask_for_answer("Are you a PWD(y/n):",1)
        Birth_year = ask_for_answer("What is your birth year:")
        print("This will serve as your official receipt")
        price_list = []
        for item_no, quantity, item_info in zip(cart.keys(), cart.values(), item_dictionary.values()):
            if quantity > 0:
                price = quantity*item_info['price']
                print(f"{item_info['name']}{' ' * (20 - len(item_info['name']))} | P{item_info['price']} X {quantity} = {quantity*item_info['price']}")
                price_list.append(price)
        print("----------------------------------------------------")
        total = sum(price_list)
        print(f"TOTAL                | {total}")
        discount = (0.05 * total if PWD == "y" else 0) + (0.1 * total if 2020 - Birth_year >= 60 else 0)
        print(f"PWD/SENIOR           | {discount}")
        final_total = total-discount
        print(f"DISCOUNTED TOTAL     | {final_total}")
        print(f"CASH TENDERED        | {input_amount}")
        print(f"CHANGE               | {input_amount - final_total}")
        print("----------------------------------------------------")
        print("THANK YOU !")
        return 0


while loop:
    rcv = display(current_tab, current_pointer)
    if rcv == 0:
        if current_tab == 0:
            loop = False
        else:
            current_tab = 0
    else:
        if current_tab == 0:
            current_tab = rcv

        elif current_tab == 1:
            current_tab = 11
            current_pointer = rcv

        elif current_tab == 11:
            current_tab = 0
            add_or_remove_from_cart(current_pointer, rcv)
            print("Successfully  added to the cart")
            current_pointer = 0
        elif current_tab == 2:
            if rcv == 1:
                current_tab = 21
            if rcv == 2:
                current_tab = 22
        elif current_tab == 21:
            current_pointer = rcv
            current_tab = 211
        elif current_tab == 211:
            current_tab = 2
            add_or_remove_from_cart(current_pointer, rcv, 0)
            print("Successfully  removed from the cart")
            current_pointer = 0
    print("----------------------------------------------------")
