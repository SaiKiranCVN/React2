-- SQLINES DEMO *** le SQL Developer Data Modeler 20.2.0.167.1538
-- SQLINES DEMO *** -04-28 18:15:32 EDT
-- SQLINES DEMO *** le Database 11g
-- SQLINES DEMO *** le Database 11g



-- SQLINES DEMO *** no DDL - MDSYS.SDO_GEOMETRY

-- SQLINES DEMO *** no DDL - XMLTYPE

CREATE TABLE curriencies (
    code              VARCHAR(10) NOT NULL,
    name              VARCHAR(30) NOT NULL,
    is_active         CHAR(1) NOT NULL,
    is_base_currency  CHAR(1) NOT NULL,
    updated_date      DATE NOT NULL
);

ALTER TABLE curriencies ADD /* CONSTRAINT curriencies_pk */ PRIMARY KEY ( code );

CREATE TABLE itemDW (
    item_id       VARCHAR(10) NOT NULL,
    code          VARCHAR(10) NOT NULL,
    name          VARCHAR(30) NOT NULL,
    price_id      VARCHAR(10) NOT NULL,
    buy           DECIMAL(10, 3) NOT NULL,
    sell          DECIMAL(10, 3) NOT NULL,
    updated_date  DATE NOT NULL
);

ALTER TABLE itemDW ADD /* CONSTRAINT itemDW_pk */ PRIMARY KEY ( item_id,
                                                      price_id );

CREATE TABLE tradeDW (
    trade_id        VARCHAR(10) NOT NULL,
    quantity        DECIMAL(10, 3) NOT NULL,
    unit_price      DECIMAL(10, 3) NOT NULL,
    updated_date    DATE NOT NULL,
    buyer_id        VARCHAR(10) NOT NULL,
    seller_id       VARCHAR(10) NOT NULL,
    pay_id          VARCHAR(10) NOT NULL,
    amount          DECIMAL(10, 3) NOT NULL,
    offer_id        VARCHAR(10) NOT NULL,
    total_quantity  DECIMAL(10, 4) NOT NULL,
    buy_sell        CHAR(1) NOT NULL,
    price           DECIMAL(10, 3) NOT NULL,
    user_id         VARCHAR(10),
    add_id          VARCHAR(10),
    bank_id         VARCHAR(10),
    inven_id        VARCHAR(10),
    item_id         VARCHAR(10),
    price_id        VARCHAR(10)
);

ALTER TABLE tradeDW
    ADD /* CONSTRAINT tradeDW_pk */ PRIMARY KEY ( trade_id,
                                          pay_id,
                                          offer_id );

CREATE TABLE user_dataDW (
    user_id         VARCHAR(10) NOT NULL,
    first_name      VARCHAR(45) NOT NULL,
    last_name       VARCHAR(45) NOT NULL,
    username        VARCHAR(45) NOT NULL,
    email           VARCHAR(60) NOT NULL,
    wallet          DECIMAL(10, 3) NOT NULL,
    dob             DATE NOT NULL,
    gender          CHAR(1) NOT NULL,
    updated_date    DATE NOT NULL,
    add_id          VARCHAR(10) NOT NULL,
    type            VARCHAR(10) NOT NULL,
    street_address  VARCHAR(60) NOT NULL,
    city            VARCHAR(30) NOT NULL,
    state           VARCHAR(2) NOT NULL,
    zipcode         INT NOT NULL,
    bank_id         VARCHAR(10) NOT NULL,
    exp_date        DATE NOT NULL,
    inven_id        VARCHAR(10) NOT NULL,
    item_id         VARCHAR(10) NOT NULL,
    bought_price    DECIMAL(10, 3) NOT NULL,
    quantity        DECIMAL(10, 3) NOT NULL
);

ALTER TABLE user_dataDW
    ADD /* CONSTRAINT user_dataDW_pk */ PRIMARY KEY ( user_id,
                                              add_id,
                                              bank_id,
                                              inven_id );

ALTER TABLE tradeDW
    ADD /* CONSTRAINT tradeDW_itemDW_fk */ FOREIGN KEY ( item_id,
                                               price_id )
        REFERENCES itemDW ( item_id,
                          price_id );

ALTER TABLE tradeDW
    ADD /* CONSTRAINT tradeDW_user_dataDW_fk */ FOREIGN KEY ( user_id,
                                                    add_id,
                                                    bank_id,
                                                    inven_id )
        REFERENCES user_dataDW ( user_id,
                               add_id,
                               bank_id,
                               inven_id );

