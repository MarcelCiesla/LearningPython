# Variable Length Arguments *args (Non keyword arguments)
def order_food(main_order, *args):
    print(f"You have ordered: {main_order}")
    for item in args:
        print(f"you have ordered: {item}")
    print("Your food will be delivered in 30 mins:")
    print("Enjoy the party")


order_food("Salad", "Pizza", "Macaroni")

