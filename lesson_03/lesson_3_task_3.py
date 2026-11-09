from mailing import Mailing
from address import Address

to_addr = Address(index=123456, city="Москва", street="Ленина", house="10", apartment="1"),
from_addr = Address(index=654321, city="Санкт-Петербург", street="Невский пр.", house="20", apartment="2")

mailing = Mailing(
    to_address=to_addr,
    from_address=from_addr,
    cost=500.0,
    track="TRACK-123"
)

print(f"""
Отправление {mailing.track}
из {mailing.from_address.index}, {mailing.from_address.city},
{mailing.from_address.street}, д.{mailing.from_address.house} -
квартира {mailing.from_address.apartment}
в {mailing.to_address.index}, {mailing.to_address.city},
{mailing.to_address.street}, д.{mailing.to_address.house} -
квартира {mailing.to_address.apartment}.
Стоимость {mailing.cost:  .2f} рублей.
""")
