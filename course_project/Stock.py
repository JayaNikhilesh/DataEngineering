import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Nikhilesh.2004",
    database="project"
)

cursor = connection.cursor()

class stock:
    def add_prod(self, x, quantity):
        query = """
            select product_name, product_value from products where product_id = %s
        """
        # x = int(input("Enter the procuct_id: "))
        value = (x,)
        cursor.execute(query, value)

        purchases = cursor.fetchall()

        for item in purchases:

            product_name = item[0]
            product_value = item[1]

        query = """
        select product_id from product_stock where product_id = %s
        """
        values = (x,)
        cursor.execute(query, values)
        n = cursor.fetchall()
        
        for item in n:
            item = 1
        
        if item == 1:
            query = """
            update product_stock set product_quantity = product_quantity + %s where product_id = %s
            """

            values = (quantity, x)
            cursor.execute(query, values)
            connection.commit()
        
        else:
            query = """
                insert into product_stock values (%s, %s, %s, %s)
            """

            # y = input("Enter the quantity of the product you purchased: ")
            values = (x, product_name, product_value, quantity)

            cursor.execute(query, values)
            connection.commit()
        
        cursor.execute("select * from product_stock")
        products = cursor.fetchall()
        print(products)



    def sell_prod(self, x, quantity):
        
        query = """
            select product_value from products where product_id = %s
        """
        # x = int(input("Enter the procuct_id: "))
        value = (x,)
        cursor.execute(query, value)

        purchases = cursor.fetchall()

        for item in purchases:

            product_value = item[0]

            
        query = """
            update product_stock set product_quantity = product_quantity - %s 
            where product_id = %s 
        """


        products_stock = cursor.execute("select product_quantity from product_stock where product_id = %s", (x,))
        products_stock = cursor.fetchall()
        m = products_stock[0][0]

        print(m)

        # y = int(input("Enter the quantity of the product you sold: "))
        values = (quantity, x)

        if m < quantity:
            print("Unable to sell as product is out of stock!")
            return

        else:
            cursor.execute(query, values)
            connection.commit()


        cursor.execute("select * from product_stock")
        products = cursor.fetchall()
        print(products)
        
        products_stock = cursor.execute("select product_quantity from product_stock where product_id = %s", (x,))
        products_stock = cursor.fetchall()
        m = products_stock[0][0]
        print(m)

        if m <= 10:
            print("Low stock, need to refill")

if __name__ == "__main__":
    p = stock()
    p.add_prod()
    p.sell_prod()