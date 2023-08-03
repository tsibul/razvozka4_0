from django.db import models
from auditlog.registry import auditlog


class DriverIcons(models.Model):
    description = models.CharField(max_length=100)
    icon_url = models.CharField(max_length=255, null=True)


class Driver(models.Model):
    code = models.CharField(max_length=2)
    description = models.CharField(max_length=100)
    phone1 = models.CharField(max_length=12)
    phone2 = models.CharField(max_length=12, null=True, blank=True)
    car_no = models.CharField(max_length=9, null=True, blank=True)
    icon_code = models.CharField(max_length=255, default='icons/truck.svg', null=True, blank=True)
    deleted = models.BooleanField(default=False)

    def __repr__(self):
        return self.description

    def __str__(self):
        return self.description


class Customer(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)
    mappoint = models.CharField(max_length=255, default='', help_text="Yandex mappoint")
    subcontractor = models.BooleanField(default=False, help_text='True if subcontractor')
    deleted = models.BooleanField(default=False)

    def __repr__(self):
        return f"Customer(name={self.name!r}, contact={self.contact!r})"

    def __str__(self):
        return self.name


class Razvozka(models.Model):
    date = models.DateField(help_text='date of transportation', null=True)
    date_id = models.SmallIntegerField(default=0, help_text='order inside date')
    customer = models.ForeignKey(Customer, models.SET_NULL, null=True, blank=True, help_text='customer base if exist')
    customer_name = models.CharField(max_length=100, help_text='customer as text could differ from db')
    address = models.CharField(max_length=255, help_text='real address')
    contact = models.CharField(max_length=255, help_text='real contacts')
    to_do_deliver = models.CharField(max_length=255, help_text='things for delivery')
    to_do_take = models.CharField(max_length=255, help_text='things to take from')
    map_point = models.CharField(max_length=255, help_text='Yandex mappoint')
    fulfilled = models.BooleanField(default=False, help_text='True is fulfilled')
    deliver_to = models.BooleanField(default=False, help_text='transportation to processing')
    return_from = models.BooleanField(default=False, help_text='return products from processing')
    return_all = models.BooleanField(default=False, help_text='False if some part was not return')

    return_goods = models.ForeignKey('self', models.SET_NULL, null=True, blank=True,
                                     help_text='from which delivery return')

    date_until = models.DateField(null=True,
                                  help_text='plan (last) date of transportation')
    date_create = models.DateField(null=True, help_text='date of create razvozka')
    driver = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True, blank=True, default=None)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return str(self.date) + '| ' + str(self.customer_name) + '| ' + str(self.to_do_deliver) + '| ' + str(
            self.to_do_take)

    def __repr__(self):
        return f"razvozka_list(date={self.date!r}, customer={self.customer_name!r}, deliver={self.to_do_deliver!r}, " \
               f"take={self.to_do_take!r}) "

    def get_all_todo(self):
        to_do_take = ''
        to_do_deliver = ''
        if self.to_do_take != '':
            to_do_take = ' ЗАБРАТЬ: ' + str(self.to_do_take)
        if self.to_do_deliver != '':
            to_do_deliver = ' СДАТЬ: ' + str(self.to_do_deliver)
        return f"{to_do_take} {to_do_deliver}"


class Razvozka_returns(models.Model):
    take = models.ForeignKey(Razvozka, on_delete=models.CASCADE, related_name='take')
    deliver = models.ForeignKey(Razvozka, on_delete=models.CASCADE, related_name='deliver')
    returned = models.BooleanField(default=False)


auditlog.register(Customer)
auditlog.register(Razvozka)
auditlog.register(Razvozka_returns)
auditlog.register(Driver)
