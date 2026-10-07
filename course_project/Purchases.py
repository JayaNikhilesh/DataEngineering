import mysql.connector
from course_project.Stock import stock
from datetime import datetime


connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="xxxxx",
    database="xxxxx"
)

cursor = connection.cursor()


class Purchases:

    def insert_purchases(self):

        a = []
        p = "True"
        while p == "True":
            x = int(input("Enter the procuct_id: "))
            quantity = int(input("Enter the quantity of the product you purchased: "))
            a.append((x, quantity))
            y = input("If you dont want to continue type 'no': ").lower()
            if y == "no":
                p = False
                break

        for item in a:
            x = int(item[0])
            quantity = item[1]
            query = """
                select product_name, product_value from products where product_id = %s
            """
            
            value = (x,)
            cursor.execute(query, value)

            purchases = cursor.fetchall()

            for item in purchases:

                product_name = item[0]
                product_value = item[1]


            current_date = datetime.now()


            query = """
                insert into Purchases (product_id,product_name, product_value,
                product_quantity, total_value, time_of_purchase) 
                values(%s, %s, %s, %s, %s, %s)
            """


            total_value = product_value * quantity

            values = (x, product_name, product_value,quantity, total_value, 
                        current_date)

            cursor.execute(query, values)
            connection.commit()

            s = stock()
            s.add_prod(x, quantity)

        # return x, quantity



    def delete_purchase(self):
        cursor = connection.cursor()

        query = """
            delete from Purchases where purchase_id = %s
        """

        x = int(input("Enter the Purchase_id you want to remove: "))
        values = (x,)

        cursor.execute(query, values)
        connection.commit()

        purchases = cursor.execute("select * from Purchases")
        purchases = cursor.fetchall()
        print(purchases)

    def update_purchase(self):

        cursor = connection.cursor()


        a = []
        p = "True"
        while p == "True":
         x = int(input("enter the purchase id that has to be updated: "))
        # y = input("Enter the name of the updated product: ")
        z = int(input("Enter the updated quantity: "))
        a.append((x, quantity))
        y = input("If you dont want to continue type 'no': ").lower()
        if y == "no":
            p = False
            break

        for item in a:
            x = int(item[0])
            z = item[1]
            query = """
            select product_id, product_quantity from purchases where purchase_id = %s
            """

            value = (x, )

            cursor.execute(query, value)
            j = cursor.fetchall()

            for item in j:
                p_id = item[0]
                p_quantity = item[1]


            query = """
            update product_stock set product_quantity = product_quantity - %s where product_id = %s
            """

            values = (p_quantity, p_id)

            cursor.execute(query, values)
            connection.commit()

            query = """
                update purchases set product_quantity = %s where purchase_id = %s
            """

            values = (z, x)

            cursor.execute(query, values)
            connection.commit()

            query = """
            update product_stock set product_quantity = product_quantity + %s where product_id = %s
            """

            values = (z, x)

            cursor.execute(query, values)
            connection.commit()

            cursor.execute("Select * from purchases where purchase_id = %s", (x, ))

            products = cursor.fetchall()
            print(products)

    def view_purchases(self):

        cursor = connection.cursor()
        query = """
        select * from purchases
        """
        
        x = cursor.execute(query)
        h = cursor.fetchall()

        for item in h:
            print(item)


# p = Purchases()
# if __name__ == "__main__":
#     x = True
#     while x == True:
#         print("Select the operation you to want to do: ")
#         print("1. Insert Purchases")
#         print("2. Delete Purchases")
#         print("3. Show Purchases")
#         print("4. Update Purchases")

#         choice = int(input("Enter your choice: "))

#         if choice == 1:
#             p.insert_purchases()
#         elif choice == 2:
#             p.delete_purchase()
#         elif choice == 3:
#             p.view_purchases()
#         elif choice == 4:
#             p.update_purchase()
#         else:
#             print("Invalid choice")

#         h = input("If you dont want to continue type 'no': ").lower()
#         if h == "no":
#             x = False
#             break


#     print("\nYour data is updated")
