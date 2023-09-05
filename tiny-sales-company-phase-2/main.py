# Type code here
class ItemToPurchase:
    def __init__(self, name = 'none', price = 0, qty = 0, item_description = 'none'):
        self.item_name = name
        self.item_price = price
        self.item_quantity = qty
        self.item_description = item_description
    def print_item_cost(self):
        total_cost = self.item_price * self.item_quantity
        print(f'{self.item_name} {self.item_quantity} @ ${self.item_price} = ${total_cost}')
    def get_total_cost(self):
        return self.item_price * self.item_quantity
    def print_item_description(self, itp):
        print(self.item_description)

class ShoppingCart:
    def __init__(self, name = 'none', date = 'January 1, 2016'):
        self.customer_name = name
        self.current_date = date
        self.cart_items = []
    def add_item(self, ItemToPurchase):
        self.cart_items.append(ItemToPurchase)
    def remove_item(self, item_name):
        isInList = False
        value = None
        for item in self.cart_items:
            if item.item_name == item_name:
                isInList = True
                value = item
        if isInList:
            self.cart_items.remove(value)
        else:
            print('Item not found in cart. Nothing removed.')
    def modify_item(self, item_name, new_qty):
        cart = self.cart_items
        isInList = False
        value = None
        for item in self.cart_items:
            if item.item_name == item_name:
                isInList = True
                value = item
        if isInList:
            idx = cart.index(value)
            cart[idx].item_quantity = new_qty
        else:
            print('Item not found in cart. Nothing modified.')
    def get_num_items_in_cart(self):
        count = 0
        for item in self.cart_items:
            count += item.item_quantity
        return count
    def get_cost_of_cart(self):
        cart_total = 0
        for item in self.cart_items:
            cart_total += item.item_price * item.item_quantity
        return cart_total
    def print_total(self):
        num_items = self.get_num_items_in_cart()
        total = self.get_cost_of_cart()
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print(f'Number of Items: {num_items}')
        print()
        if num_items < 1:
            print('SHOPPING CART IS EMPTY')
        else:
            for item in self.cart_items:
                print(f'{ item.item_name} {item.item_quantity} @ ${item.item_price} = ${item.item_quantity * item.item_price}')
        print()
        print(f'Total: ${total}')
    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print()
        print('Item Descriptions')
        for item in self.cart_items:
            print(f"{item.item_name}: {item.item_description}")

if __name__ == "__main__":
    # Type main section of code here   
    def print_menu(cart):
        cmd = 0
        while cmd != 'q':
            print()
            print("MENU")
            print("a - Add item to cart")
            print("r - Remove item from cart")
            print("c - Change item quantity")
            print("i - Output items' descriptions")
            print("o - Output shopping cart")
            print("q - Quit")
            print()
            cmd = input('Choose an option:\n').lower()
            while cmd not in ['a','r','c','i','o','q']:
                cmd = input('Choose an option:\n').lower()
            if cmd == 'o':
                print('OUTPUT SHOPPING CART')
                cart.print_total()
            elif cmd == 'i':
                print("OUTPUT ITEMS' DESCRIPTIONS")
                cart.print_descriptions()
            elif cmd == 'a':
                print("ADD ITEM TO CART")
                item_name = input('Enter the item name:\n')
                description = input('Enter the item description:\n')
                price = int(input('Enter the item price:\n'))
                qty = int(input('Enter the item quantity:\n'))
                item = ItemToPurchase(item_name, price, qty, description)
                cart.add_item(item)
            elif cmd == 'r':
                print('REMOVE ITEM FROM CART')
                item_to_rm = input('Enter name of item to remove:\n')
                cart.remove_item(item_to_rm)
            elif cmd == 'c':
                print('CHANGE ITEM QUANTITY')
                item_to_change = input('Enter the item name:\n')
                new_qty = int(input('Enter the new quantity:\n'))
                cart.modify_item(item_to_change, new_qty)
            else:
                continue

    customer_name = input("Enter customer's name:\n")
    date = input("Enter today's date:\n")
    print()
    print(f"Customer name: {customer_name}")
    print(f"Today's date: {date}")
    shopping_cart = ShoppingCart(customer_name, date)
    print_menu(shopping_cart)