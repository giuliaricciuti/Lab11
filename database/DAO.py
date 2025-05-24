from database.DB_connect import DBConnect
from model.daily_sales import DailySale
from model.go_products import Product


class DAO():
    @staticmethod
    def getAllColours():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor()
        query = """SELECT DISTINCT gp.Product_color 
                FROM go_products gp """
        cursor.execute(query)

        for row in cursor:
            result.append(row[0])
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getProductsByColor(color):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary = True)
        query = """SELECT DISTINCT *
                    FROM go_products gp 
                    WHERE gp.Product_color = %s"""
        cursor.execute(query, (color,))

        for row in cursor:
            result.append(Product(**row))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getDailySales(year):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary = True)
        query = """SELECT *
                    from go_daily_sales gds 
                    WHERE YEAR (gds.`Date`)=%s"""
        cursor.execute(query, (year,))

        for row in cursor:
            result.append(DailySale(row["Retailer_code"], row["Product_number"], row["Date"]))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getSameDaySales(p1, p2, year):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor()
        query = """SELECT COUNT(DISTINCT gds2.`Date`) as N
                    from go_daily_sales gds , go_daily_sales gds2 
                    WHERE YEAR (gds.`Date`)= %s
                    AND gds.Product_number = %s
                    AND gds2.Product_number = %s
                    AND gds2.Retailer_code = gds.Retailer_code
                    AND gds2.`Date` = gds.`Date` """
        cursor.execute(query, (year, p1, p2))

        for row in cursor:
            result.append(DailySale(row["N"]))

        cursor.close()
        conn.close()
        return result