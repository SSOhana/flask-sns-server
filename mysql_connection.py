import mysql.connector

def get_connection() :
    connection = mysql.connector.connect(
        host = 'yh-db.caohoyy07jik.ap-northeast-2.rds.amazonaws.com',
        database = 'sns_db', 
        user = 'sns_user1',
        password = '06sns24' 
    )
    return connection   


