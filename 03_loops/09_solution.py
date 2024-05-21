# List Uniqueness Checker
# Check if all elements in a list are unique. If a duplicate is found,exit the loop and print the duplicate.

fruits_list = ['apple','banana','orange','apple','mango']
unique_items = set()
dupilcate_fruit = ''

for fruit in fruits_list:
    if fruit in unique_items:
        dupilcate_fruit = fruit
        break
    unique_items.add(fruit)        
    
if dupilcate_fruit:
    print(f'duplicate fruit is {dupilcate_fruit}')
else:
    print('all fruits are unique')
            