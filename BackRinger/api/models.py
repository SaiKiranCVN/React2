# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Address(models.Model):
    add_id = models.CharField(primary_key=True, max_length=10)
    type = models.CharField(max_length=10)
    street_address = models.CharField(max_length=60)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=2)
    zipcode = models.IntegerField()
    user = models.ForeignKey('UserData', models.DO_NOTHING)
    updated_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'address'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class AuthtokenToken(models.Model):
    key = models.CharField(primary_key=True, max_length=40)
    created = models.DateTimeField()
    user = models.OneToOneField(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'authtoken_token'


class Bank(models.Model):
    bank_id = models.CharField(primary_key=True, max_length=10)
    card_no = models.BigIntegerField()
    exp_date = models.DateTimeField()
    cvv = models.SmallIntegerField()
    name = models.CharField(max_length=60)
    defa = models.CharField(max_length=1)
    user = models.ForeignKey('UserData', models.DO_NOTHING)
    updated_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bank'


class Currencies(models.Model):
    code = models.CharField(primary_key=True, max_length=10)
    name = models.CharField(max_length=30)
    is_active = models.CharField(max_length=1)
    is_base_currency = models.CharField(max_length=1)
    updated_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'currencies'


class Divident(models.Model):
    yr2004 = models.DecimalField(max_digits=10, decimal_places=3)
    yr2005 = models.DecimalField(max_digits=10, decimal_places=3)
    yr2006 = models.DecimalField(max_digits=10, decimal_places=3)
    yr2007 = models.DecimalField(max_digits=10, decimal_places=3)
    yr2008 = models.DecimalField(max_digits=10, decimal_places=3)
    yr2009 = models.DecimalField(max_digits=10, decimal_places=3)
    yr2010 = models.DecimalField(max_digits=10, decimal_places=3)
    yr2011 = models.DecimalField(max_digits=10, decimal_places=3)
    yr2012 = models.DecimalField(max_digits=10, decimal_places=3)
    yr2013 = models.DecimalField(max_digits=10, decimal_places=3)
    yr2014 = models.DecimalField(max_digits=10, decimal_places=3)
    yr2015 = models.DecimalField(max_digits=10, decimal_places=3)
    yr2016 = models.DecimalField(max_digits=10, decimal_places=3)
    yr2017 = models.DecimalField(max_digits=10, decimal_places=3)
    yr2018 = models.DecimalField(max_digits=10, decimal_places=3)
    yr2019 = models.DecimalField(max_digits=10, decimal_places=3)
    yr2020 = models.DecimalField(max_digits=10, decimal_places=3)
    yr2021 = models.DecimalField(max_digits=10, decimal_places=3)
    item = models.OneToOneField('Item', models.DO_NOTHING, primary_key=True)

    class Meta:
        managed = False
        db_table = 'divident'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Inventory(models.Model):
    inven_id = models.CharField(primary_key=True, max_length=10)
    item_id = models.CharField(max_length=10)
    bought_price = models.DecimalField(max_digits=10, decimal_places=3)
    quantity = models.DecimalField(max_digits=10, decimal_places=3)
    user = models.ForeignKey('UserData', models.DO_NOTHING)
    updated_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'inventory'


class Item(models.Model):
    item_id = models.CharField(primary_key=True, max_length=10)
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=30)
    price = models.ForeignKey('Price', models.DO_NOTHING)
    sector = models.CharField(max_length=45)
    homepage = models.CharField(max_length=100)
    investorpage = models.CharField(max_length=100)
    pe = models.DecimalField(max_digits=10, decimal_places=3)
    updated_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'item'


class ItemResearch(models.Model):
    item = models.ForeignKey(Item, models.DO_NOTHING, blank=True, null=True)
    ids = models.ForeignKey('Research', models.DO_NOTHING, db_column='ids', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'item_research'


class Offer(models.Model):
    offer_id = models.CharField(primary_key=True, max_length=10)
    quantity = models.DecimalField(max_digits=10, decimal_places=4)
    buy_sell = models.CharField(max_length=1)
    price = models.DecimalField(max_digits=10, decimal_places=3)
    ts = models.DateTimeField()
    updated_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'offer'


class Payment(models.Model):
    pay_id = models.CharField(primary_key=True, max_length=10)
    amount = models.DecimalField(max_digits=10, decimal_places=3)
    updated_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'payment'


class Price(models.Model):
    price_id = models.CharField(primary_key=True, max_length=10)
    buy = models.DecimalField(max_digits=10, decimal_places=3)
    sell = models.DecimalField(max_digits=10, decimal_places=3)
    ts = models.DateTimeField()
    changeper = models.DecimalField(max_digits=10, decimal_places=4)
    updated_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'price'


class Research(models.Model):
    ids = models.CharField(primary_key=True, max_length=10)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    link = models.CharField(max_length=50)
    author_name = models.CharField(max_length=50)
    authorid = models.CharField(max_length=10)
    updated_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'research'


class Trade(models.Model):
    trade_id = models.CharField(primary_key=True, max_length=10)
    quantity = models.DecimalField(max_digits=10, decimal_places=3)
    unit_price = models.DecimalField(max_digits=10, decimal_places=3)
    item = models.ForeignKey(Item, models.DO_NOTHING)
    buyer = models.ForeignKey('UserData', models.DO_NOTHING,related_name='buyer_id')
    seller = models.ForeignKey('UserData', models.DO_NOTHING,related_name='seller_id')
    pay = models.ForeignKey(Payment, models.DO_NOTHING)
    updated_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'trade'


class TradeOffer(models.Model):
    pri = models.CharField(primary_key=True, max_length=10)
    offer = models.ForeignKey(Offer, models.DO_NOTHING)
    trade = models.ForeignKey(Trade, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'trade_offer'


class UserData(models.Model):
    user_id = models.CharField(primary_key=True, max_length=10)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    username = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    email = models.CharField(max_length=60)
    time_registered = models.DateTimeField(blank=True, null=True)
    wallet = models.DecimalField(max_digits=10, decimal_places=3)
    dob = models.DateTimeField()
    gender = models.CharField(max_length=1)
    updated_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_data'
