from address import Address
from mailing import Mailing

#адрес для отправки
to_address = Address("12345","Тюмень", "Мира", "10", "22")
#адрес отправителя
from_address = Address("67890","Тюмень1", "Пушкина", "11", "12")

mailing = Mailing(to_address,from_address,100, "track12345")