import requests
import json
import sqlite3


# ამოცანა 4
def connect_db(db_name):
    return sqlite3.connect(db_name)


def creat_table():
    cur.execute('''CREATE TABLE IF NOT EXISTS weather_db
                   (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   temp FLOAT,
                   pressure INTEGER,
                   sea_level INTEGER,
                   humidity FLOAT,
                   description VARCHAR (35),
                   dt_txt VARCHAR(35) )
                ''')
    conn.commit()
# მოცემულ ცხრილს ვქმნი, რათა შევინახო ინფორმაცია მომდევნო ხუთი დღის (საათების მიხედვით) ამინდის პროგნოზის შესახებ:
# პირველი ველი არის id რომელიც არის უნიკალური იდენტიფიკატორი და ავტოინკრემენტი, შემდეგი ველი temp არის ტემპერატურისთვის,
# pressure  ველში ინახება ინფორმაცია წნევის შესახებ, sea_level ველში ზღვის დონის შესახებ, humidity ტენიანობის შესახებ,
# description ამინდის მოკლე აღწერა მაგ. კრიალა ცა, მსუბუქი წვიმა და ა.შ. ხოლო რაც შეეხება dt_txt ველს, მასში ვინახავ
# ინფორმაციას თარიღთან დაკავშირებით შემდეგი ფორმატით: წელი-თვე-დღე საათი:წუთი:წამი

key = 'ac85a9566b2043b8a199e2ad01a80c44'
city = 'London'
payload = {'q': city,  'appid': key}
url = f'https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={key}'
# ამოცანა1
r = requests.get(url)
print('status code: ', r.status_code)
print('headers content-type: ', r.headers['content-type'])
print('content: ', r.content)
# ამოცანა 2
res = json.loads(r.text)  # dict
print(json.dumps(res, indent=4))

with open('data.json', 'w') as f:
    json.dump(res, f, indent=4)

a = []

# ამოცანა 4
conn = connect_db("weather.sqlite")
cur = conn.cursor()
cur.execute("DELETE FROM weather_db")
conn.commit()
# ამოცანა 3
for each in res['list']:
    b = (each['main']['temp'], each['main']['pressure'], each['main']['sea_level'], each['main']['humidity'],
         each['weather'][0]['description'], each['dt_txt'])
    print("temperature: ", b[0], "  pressure: ", b[1], "  sea level: ", b[2], "  humidity: ", b[3],
          "  description: ", b[4], "  Date: ", b[5])
    a.append(b)

# ამოცანა 4
creat_table()
cur.executemany("Insert Into weather_db (temp, pressure, sea_level, humidity, description, dt_txt) VALUES (?,?,?,?,?,?)", a)
conn.commit()

p = cur.execute("select * from weather_db").fetchall()
for each in p:
    print(each)

conn.commit()
conn.close()
# https://openweathermap.org/forecast5
