import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="xxxxxxx",
    database="xxxxxxxx"
)

cursor = connection.cursor()

class Filter():

    def filter_purchases(self):

        query = """
            select * from purchases where date(time_of_purchase) between %s and %s
        """

        x = input("Enter the start date: ")
        y = input("Enter the end date: ")

        values = (x, y)

        cursor.execute(query, values)
        Purchases = cursor.fetchall()

        for items in Purchases:
            print(items)

    def filter_sales(self):

        query = """
            select * from sales where date(time_of_sale) between %s and %s

        """

        x = input("Enter the start date: ")
        y = input("Enter the end date: ")

        values = (x, y)

        cursor.execute(query, values)
        Sales = cursor.fetchall()

        for items in Sales:
            print(items)


# if __name__ == "__main__":

#     f = Filter()
#     f.filter_purchases()
#     f.filter_sales()

        
