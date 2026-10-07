import mysql.connector
from course_project.Stock import stock
from datetime import datetime


connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="xxxxxx",
    database="xxxxxx"
)

cursor = connection.cursor()


class Sales:

    def insert_sale(self):

        a = []
        p = "True"
        while p == "True":
            x = int(input("Enter the procuct_id: "))
            quantity = int(input("Enter the quantity of the product you sold: "))
            a.append((x, quantity))
            y = input("If you dont want to continue type 'no': ").lower()
            if y == "no":
                p = False
                break

        for item in a:
            x = int(item[0])
            quantity = item[1]

            query = """
                select product_name, product_value from products where product_id = 
                %s
            """
            
            value = (x,)
            cursor.execute(query, value)

            sales = cursor.fetchall()

            for item in sales:

                product_name = item[0]
                product_value = item[1]


            current_date = datetime.now()


            query = """
                insert into Sales (product_id,product_name, product_value,
                product_quantity, total_value, time_of_sale) 
                values(%s, %s, %s, %s, %s, %s)
            """



            total_value = product_value * quantity

            values = (x, product_name, product_value,quantity, total_value, 
                        current_date)

            cursor.execute(query, values)
            connection.commit()

            s = stock()
            s.sell_prod(x, quantity)


    def delete_sale(self):
        cursor = connection.cursor()

        query = """
            delete from Sales where sale_id = %s
        """

        x = int(input("Enter the sales id you want to remove: "))
        values = (x,)

        cursor.execute(query, values)
        connection.commit()

        sales = cursor.execute("select * from Sales")
        sales = cursor.fetchall()
        print(sales)

    def update_sale(self):
        cursor = connection.cursor()

        x = int(input("enter the sales id that has to be updated: "))
        # y = input("Enter the name of the updated product: ")
        z = int(input("Enter the updated quantity: "))

        query = """
        select product_id, product_quantity from sales where sale_id = %s
        """

        value = (x, )

        cursor.execute(query, values)
        j = cursor.fetchall()

        for item in j:
            p_id = item[0]
            p_quantity = item[1]


        query = """
        update product_stock set product_quantity = product_quantity + %s where product_id = %s
        """

        values = (p_quantity, p_id)

        cursor.execute(query, values)
        connection.commit()


        query = """
            update Sales set product_quantity = %s where 
            sale_id = %s
        """

        values = (z, x)

        cursor.execute(query, values)
        connection.commit()

        query = """
        update product_stock set product_quantity = product_quantity - %s where product_id = %s
        """

        values = (z, p_id)

        cursor.execute(query, values)
        connection.commit()

        cursor.execute("Select * from Sales where sale_id = %s", (x, ))

        sales = cursor.fetchall()
        print(sales)


    def view_sale(self):

        cursor = connection.cursor()
        query = """
        select * from Sales
        """
        
        x = cursor.execute(query)
        h = cursor.fetchall()

        for item in h:
            print(item)
        



# p = Sales()
# if __name__ == "__main__":
#     x = True
#     while x == True:
#         print("Select the operation you to want to do: ")
#         print("1. Insert Sale")
#         print("2. Delete Sale")
#         print("3. Show Sale")
#         print("4. Update Sale")

#         choice = int(input("Enter your choice: "))

#         if choice == 1:
#             p.insert_sale()
#         elif choice == 2:
#             p.delete_sale()
#         elif choice == 3:
#             p.view_sale()
#         elif choice == 4:
#             p.update_sale()
#         else:
#             print("Invalid choice")

#         h = input("If you dont want to continue type 'no': ").lower()
#         if h == "no":
#             x = False
#             break


#     print("\nYour data is updated")
