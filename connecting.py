import requests
import mysql.connector
import logging
import pandas as pd
logging.basicConfig(
     filename='app.log',
     level=logging.INFO
)

def api():
        url="YOUR-API-KEY"
        responce=requests.get(url)
        print("Status code: ",responce.status_code)
        data=responce.json()
        holidays=data['holidays']
        logging.info("API request Successfull")
        return holidays

def clean_data(holidays):
     df=pd.DataFrame(holidays)
     logging.info("Data converted into DataFrame")

     df['name']=df['name'].str.title()
     df['date']=pd.to_datetime(df['date'])
     logging.info("Converted into datetime")

     df['month'] = df['date'].dt.month_name()
     df['weekday'] = df['date'].dt.day_name()
     
     df=df.drop_duplicates()
     logging.info("Duplicates have been dropped ")
     df['date'] = df['date'].astype(str)

     cleaned_holidays = df.to_dict(orient='records')
     logging.info("Converted cleaned DataFrame back to dictionary format")
     return cleaned_holidays


def insert_data(holidays):
        query="""
        INSERT INTO HOLIDAYS 
        (name,holiday_date,public_holiday,country)
        VALUES(%s, %s, %s, %s)
        """

        count = 0
        duplicate=0
        failed=0
        for holiday in holidays:
            values=(
                holiday['name'],
                holiday['date'],
                holiday['public'],
                holiday['country']
            )
            try:

                cursor.execute(query, values)
                count += 1
                logging.info(f"Inserted holiday: {holiday['name']}")

            except mysql.connector.Error as e:

                # Duplicate entry error
                if e.errno == 1062:
                    duplicate += 1
                    logging.warning(f"Duplicate skipped: {holiday['name']} - {holiday['date']}")

                else:
                    failed += 1
                    logging.error(f"Failed inserting {holiday['name']} : {e}")

        conn.commit()
        logging.info("Data insertion completed")
        logging.info(f"Inserted rows: {count}")
        logging.info(f"Duplicate rows skipped: {duplicate}")
        logging.info(f"Failed rows: {failed}")

def main():
        holidays = api()
        cleaned_holidays=clean_data(holidays)
        insert_data(holidays)

try:
    
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Sachith@18",
        database="holiday_project"
    )
    cursor=conn.cursor()
    logging.info("Connected Successfully")
    main()
    

except Exception as e:
    logging.error(e)

finally:
    try:
        conn.close()
        logging.info("Connection close")
    except:
        pass
