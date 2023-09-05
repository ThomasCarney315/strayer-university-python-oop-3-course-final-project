# Type code for classes here
class ItemToPurchase:
    def __init__(self, name = 'none', price = 0, qty = 0):
        self.item_name = name
        self.item_price = price
        self.item_quantity = qty
    def print_item_cost(self):
        total_cost = self.item_price * self.item_quantity
        print(f'{self.item_name} {self.item_quantity} @ ${self.item_price} = ${total_cost}')
    def get_total_cost(self):
        return self.item_price * self.item_quantity

if __name__ == "__main__":
    # Type main section of code here
    print('Item 1')
    name = input('Enter the item name:\n')
    price = int(input('Enter the item price:\n'))
    qty = int(input('Enter the item quantity:\n'))
    item1 = ItemToPurchase(name,price,qty)
    
    print('\nItem 2')
    name = input('Enter the item name:\n')
    price = int(input('Enter the item price:\n'))
    qty = int(input('Enter the item quantity:\n'))
    item2 = ItemToPurchase(name,price,qty)
    
    print('\nTOTAL COST')
    item1.print_item_cost()
    item2.print_item_cost()
    print(f'\nTotal: ${item1.get_total_cost() + item2.get_total_cost()}')