import requests
from bs4 import BeautifulSoup
import smtplib

##Probar con diferentes productos de Amazon
URL = 'https://www.amazon.com.mx/Mackie-CR4BT-Monitor-Bluetooth-Par/dp/B015U623GW?pf_rd_p=847e85d2-d64d-4fd4-848f-d6c56d813dec&pd_rd_wg=Lp3Bm&pf_rd_r=79318ZRY804QKZ940JWD&ref_=pd_gw_cr_wsim&pd_rd_w=27gUg&pd_rd_r=fc994423-5dd7-448f-bcfc-11e48738cff0&th=1'

##TODO: Buscar User Agent: MY USER AGENT
headers = {"User-Agent": 'YOUR USER AGENT'}

def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()

    ##Extraer primeros digitos del precio
    convPrice = price[1:6]
    convPrice2 = convPrice.replace(',', '.')

    if(float(convPrice2) < 3.168):
        send_email()

    print(title.strip())
    print(convPrice2)

def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    ##TODO:
    server.login('YOUR E-MAIL', 'YOUR PASSWORD')

    subject = 'Precio de tu producto Bajo'
    body = 'Checa el producto: '+URL

    message = "Subject: {}\n\n{}".format(subject, body)

    server.sendmail(
        'YOUR E-MAIL',
        'YOUR E-MAIL 2',
        message
    )

    print('E-mail sent!')
    server.quit()


check_price()