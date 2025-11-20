

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")
    
    
    
def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            
            items = input("enter your items:").lower()
            shopping_list.append(items)
            
            
        elif choice == '2':
            item = input("Delete an item:")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"{item} has been deleted")
            else:
                print(f"{item} is not on the shopping list" )
          
        elif choice == '3':
            for item in shopping_list:
                print(item)
            
            
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")   
            
if __name__ == "__main__":
    main()            