import pymysql.cursors
from django.db import models

class getData(models.Model):

    def getConnection(self):

        connection = pymysql.connect(host='localhost',
                                     user='root',
                                     password='',
                                     db='web',
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)


        return connection






