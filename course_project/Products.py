import mysql.connector
from course_project import Stock

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Nikhilesh.2004",
    database="project"
)


class products:

    
    def insert_products(self):
        cursor = connection.cursor()

        
        x = int(input("Enter the product id: "))
        y = input("Enter the product name: ")
        z = int(input("Enter the product value: "))


        cursor.execute("select * from products")

        products = cursor.fetchall()

        for i in products:
            if i[1] == y:
                print("Product is already existed!!!")
                return


        query = """
            insert into products(product_id,product_name,product_value) 
            values(%s, %s, %s)
        """
        values = (x, y, z)
        cursor.execute(query, values)
        connection.commit()

        cursor.execute("select * from products")

        products = cursor.fetchall()
        print(products)

        


    def show_products(self):
        cursor = connection.cursor()
        cursor.execute("select * from products")
        products = cursor.fetchall()
        for item in products:
            print(item)


    def delete_products(self):
        cursor = connection.cursor()

        x = int(input("Enter the product id to delete: "))

        query = """
            delete from products where product_id = %s
        """

        values = (x,)

        cursor.execute(query, values)
        connection.commit()

        cursor.execute("select * from products")
        products = cursor.fetchall()
        print(products)

    
    def update_value(self):
        cursor = connection.cursor()

        x = int(input("enter the product id that has to be updated: "))
        y = int(input("Enter the updated value:"))

        query = """
            update products set product_value = %s where product_id = %s
        """

        values = (y, x)

        cursor.execute(query, values)
        connection.commit()

        cursor.execute("Select * from products where product_id = %s", (x, ))

        products = cursor.fetchall()
        print(products)

    def update_name(self):

        cursor = connection.cursor()

        x = int(input("enter the product id that has to be updated: "))
        y = input("Enter the updated name:")

        query = """
            update products set product_name = %s where product_id = %s
        """

        values = (y, x)

        cursor.execute(query, values)
        connection.commit()

        cursor.execute("Select * from products where product_id = %s", (x, ))

        products = cursor.fetchall()
        print(products)




# p = products()
# if __name__ == "__main__":
#     x = True
#     while x == True:
#         print("Select the operation you to want to do: ")
#         print("1. Insert Products")
#         print("2. Delete Products")
#         print("3. Show Products")
#         print("4. Update Products Value")
#         print("5. Update Products Name")

#         choice = int(input("Enter your choice: "))

#         if choice == 1:
#             p.insert_products()
#         elif choice == 2:
#             p.delete_products()
#         elif choice == 3:
#             p.show_products()
#         elif choice == 4:
#             p.update_value()
#         elif choice == 5:
#             p.update_name()
#         else:
#             print("Invalid choice")

#         h = input("If you dont want to continue type 'no': ").lower()
#         if h == "no":
#             x = False
#             break


#     print("\nYour data is updated")

