import smtplib 
# import requests
# from bs4 import BeautifulSoup

# URL = 'https://www.youtube.com/watch?v=Bg9r_yLk7VY'
# headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'

# }

# page = requests.get(URL,headers = headers)

# soap = BeautifulSoup(page.content,"html.parser")
# title = soap.find_all("div", class_="textBox selectable ")
# print(soap.prettify())





def sendMail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()


    server.login("mail","password")

    subject = "hello"

    body = "helloooooo"

    msg = f"Subject {subject} \n \n{body}"

    server.sendmail(
        "name",
        "reciverMail",
        msg
    )
    print("Mesage sent!!")

    server.quit()
sendMail()
