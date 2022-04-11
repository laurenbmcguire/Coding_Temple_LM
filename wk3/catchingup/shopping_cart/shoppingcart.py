
def show_instructions():
    print("""Type 'add' to add an item to your cart.
Type 'remove' to remove an item from your cart.
Type 'clear' to clear all items from your cart.
Type 'quit' to quit the program.""")
    print('='*60)


def add_item(shopping_cart, item):
    shopping_cart.append(item)


def remove_item(shopping_cart, item):
    shopping_cart.remove(item)


def show_items(shopping_cart):
    if shopping_cart:
        for idx, item in enumerate(set(shopping_cart)):
            print(f"{idx+1}) {item} [{shopping_cart.count(item)}]")
    else:
        print("You have no items in your cart.")
    print('='*60)


def clear_items(shopping_cart):
    shopping_cart.clear()


def shopping_cart():
    cart = []

    done = False
    while not done:

        show_instructions()
        show_items(cart)

        decision = input('What would you like to do? ').lower()
        if decision == 'quit':
            done = True
        elif decision == 'add':
            item_to_add = input("What item would you like to add? ").lower()
            add_item(cart, item_to_add)
        elif decision == 'remove':
            item_to_remove = input(
                "What item would you like to remove? ").lower()
            if item_to_remove not in cart:
                input("That item does not exist. Try again.")
                continue
            else:
                remove_item(cart, item_to_remove)
        elif decision == 'clear':
            clear_items(cart)
        else:
            input("That was an invalid command. Please try again.")


shopping_cart()
