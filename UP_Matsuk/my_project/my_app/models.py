from django.db import models

class Motosalon(models.Model):
    motosalon_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, verbose_name="Название мотосалона")
    
    class Meta:
        db_table = 'Мотосалон'
        verbose_name = 'Мотосалон'
        verbose_name_plural = 'Мотосалоны'
    
    def __str__(self):
        return self.name

class MotorTransport(models.Model):
    MOTORCYCLE_TYPES = [
        ('sport', 'Спортивный'),
        ('cruiser', 'Круизер'),
        ('enduro', 'Эндуро'),
        ('tourist', 'Туристический'),
        ('naked', 'Нейкед'),
        ('cross', 'Кроссовый'),
        ('scooter', 'Скутер'),
        ('classic', 'Классический'),
    ]
    
    motortransport_id = models.AutoField(primary_key=True)
    motosalon = models.ForeignKey(Motosalon, on_delete=models.CASCADE, verbose_name="Мотосалон")
    type = models.CharField(max_length=255, choices=MOTORCYCLE_TYPES, verbose_name="Тип")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Стоимость")
    year = models.IntegerField(verbose_name="Год выпуска")
    brand = models.CharField(max_length=255, verbose_name="Марка")
    model = models.CharField(max_length=255, verbose_name="Модель")
    color = models.CharField(max_length=255, verbose_name="Цвет")
    
    class Meta:
        db_table = 'Мототранспорт'
        verbose_name = 'Мототранспорт'
        verbose_name_plural = 'Мототранспорт'
    
    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"

class Dealer(models.Model):
    dealer_id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=255, verbose_name="ФИО")
    phone_number = models.BigIntegerField(verbose_name="Номер телефона")
    
    class Meta:
        db_table = 'Дилер'
        verbose_name = 'Дилер'
        verbose_name_plural = 'Дилеры'
    
    def __str__(self):
        return self.full_name

class Client(models.Model):
    client_id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=255, verbose_name="ФИО")
    phone_number = models.BigIntegerField(verbose_name="Номер телефона")
    
    class Meta:
        db_table = 'Клиент'
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
    
    def __str__(self):
        return self.full_name

class Accessory(models.Model):
    ACCESSORY_TYPES = [
        ('helmet', 'Шлем'),
        ('jacket', 'Куртка'),
        ('gloves', 'Перчатки'),
        ('boots', 'Ботинки'),
        ('cover', 'Чехол'),
        ('protection', 'Защита'),
        ('intercom', 'Интерком'),
        ('navigator', 'Навигатор'),
        ('case', 'Кофр'),
        ('antitheft', 'Антикража'),
        ('oil', 'Масло'),
        ('chain', 'Цепь'),
        ('mirrors', 'Зеркала'),
        ('exhaust', 'Выхлоп'),
        ('footpegs', 'Подножки'),
    ]
    
    accessory_id = models.AutoField(primary_key=True)
    motosalon = models.ForeignKey(Motosalon, on_delete=models.CASCADE, verbose_name="Мотосалон")
    type = models.CharField(max_length=255, choices=ACCESSORY_TYPES, verbose_name="Тип")
    brand = models.CharField(max_length=255, verbose_name="Бренд")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Стоимость")
    
    class Meta:
        db_table = 'Аксессуары'
        verbose_name = 'Аксессуар'
        verbose_name_plural = 'Аксессуары'
    
    def __str__(self):
        return f"{self.brand} {self.type}"

class Service(models.Model):
    SERVICE_TYPES = [
        ('maintenance', 'Техническое обслуживание'),
        ('oil_change', 'Замена масла'),
        ('engine_repair', 'Ремонт двигателя'),
        ('chain_replacement', 'Замена цепи'),
        ('suspension_setup', 'Настройка подвески'),
        ('wheel_balancing', 'Балансировка колес'),
        ('chip_tuning', 'Чип-тюнинг'),
        ('accessory_installation', 'Установка аксессуаров'),
        ('diagnostics', 'Диагностика'),
        ('brake_replacement', 'Замена тормозов'),
        ('painting', 'Покраска'),
        ('polishing', 'Полировка'),
        ('seasonal_storage', 'Сезонное хранение'),
        ('tire_service', 'Шиномонтаж'),
        ('field_repair', 'Выездной ремонт'),
    ]
    
    service_id = models.AutoField(primary_key=True)
    motosalon = models.ForeignKey(Motosalon, on_delete=models.CASCADE, verbose_name="Мотосалон")
    service_type = models.CharField(max_length=255, choices=SERVICE_TYPES, verbose_name="Вид услуги")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Стоимость")
    
    class Meta:
        db_table = 'Услуги'
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
    
    def __str__(self):
        return self.service_type

class Deal(models.Model):
    deal_id = models.AutoField(primary_key=True)
    dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE, verbose_name="Дилер")
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name="Клиент")
    deal_date = models.DateField(verbose_name="Дата сделки")
    total_amount = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Общая сумма")
    
    class Meta:
        db_table = 'Сделка'
        verbose_name = 'Сделка'
        verbose_name_plural = 'Сделки'
        ordering = ['-deal_date']
    
    def __str__(self):
        return f"Сделка #{self.deal_id} от {self.deal_date}"

class DealMotorTransport(models.Model):
    deal_motor_transport_id = models.AutoField(primary_key=True)
    deal = models.ForeignKey(Deal, on_delete=models.CASCADE, verbose_name="Сделка")
    motor_transport = models.ForeignKey(MotorTransport, on_delete=models.CASCADE, verbose_name="Мототранспорт")
    quantity = models.IntegerField(default=1, verbose_name="Количество")
    
    class Meta:
        db_table = 'Сделка_Мототранспорт'
        verbose_name = 'Сделка - Мототранспорт'
        verbose_name_plural = 'Сделки - Мототранспорт'
        unique_together = ['deal', 'motor_transport']
    
    def __str__(self):
        return f"{self.deal} - {self.motor_transport}"

class DealService(models.Model):
    deal_service_id = models.AutoField(primary_key=True)
    deal = models.ForeignKey(Deal, on_delete=models.CASCADE, verbose_name="Сделка")
    service = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name="Услуга")
    quantity = models.IntegerField(default=1, verbose_name="Количество")
    
    class Meta:
        db_table = 'Сделка_Услуги'
        verbose_name = 'Сделка - Услуга'
        verbose_name_plural = 'Сделки - Услуги'
        unique_together = ['deal', 'service']
    
    def __str__(self):
        return f"{self.deal} - {self.service}"

class DealAccessory(models.Model):
    deal_accessory_id = models.AutoField(primary_key=True)
    deal = models.ForeignKey(Deal, on_delete=models.CASCADE, verbose_name="Сделка")
    accessory = models.ForeignKey(Accessory, on_delete=models.CASCADE, verbose_name="Аксессуар")
    quantity = models.IntegerField(default=1, verbose_name="Количество")
    
    class Meta:
        db_table = 'Сделка_Аксессуары'
        verbose_name = 'Сделка - Аксессуар'
        verbose_name_plural = 'Сделки - Аксессуары'
        unique_together = ['deal', 'accessory']
    
    def __str__(self):
        return f"{self.deal} - {self.accessory}"