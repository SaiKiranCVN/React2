-- SQLINES DEMO *** le SQL Developer Data Modeler 20.2.0.167.1538
-- SQLINES DEMO *** -04-22 19:56:36 EDT
-- SQLINES DEMO *** le Database 11g
-- SQLINES DEMO *** le Database 11g



-- SQLINES DEMO *** no DDL - MDSYS.SDO_GEOMETRY

-- SQLINES DEMO *** no DDL - XMLTYPE

CREATE TABLE address (
    add_id          VARCHAR(10) NOT NULL,
    type            VARCHAR(10) NOT NULL,
    street_address  VARCHAR(60) NOT NULL,
    city            VARCHAR(30) NOT NULL,
    state           VARCHAR(2) NOT NULL,
    zipcode         INT NOT NULL,
    updated_date    DATETIME NOT NULL,
    user_id         VARCHAR(10) NOT NULL
);

ALTER TABLE address ADD CONSTRAINT address_pk PRIMARY KEY ( add_id );

CREATE TABLE bank (
    bank_id       VARCHAR(10) NOT NULL,
    card_no       BIGINT NOT NULL,
    exp_date      DATETIME NOT NULL,
    cvv           SMALLINT NOT NULL,
    name          VARCHAR(60) NOT NULL,
    defa          CHAR(1) NOT NULL,
    updated_date  DATETIME NOT NULL,
    user_id       VARCHAR(10) NOT NULL
);

ALTER TABLE bank ADD CONSTRAINT bank_pk PRIMARY KEY ( bank_id );

CREATE TABLE currencies (
    code              VARCHAR(10) NOT NULL,
    name              VARCHAR(30) NOT NULL,
    is_active         CHAR(1) NOT NULL,
    is_base_currency  CHAR(1) NOT NULL,
    updated_date      DATETIME NOT NULL
);

ALTER TABLE currencies ADD CONSTRAINT currencies_pk PRIMARY KEY ( code );

CREATE TABLE inventory (
    inven_id      VARCHAR(10) NOT NULL,
    item_id       VARCHAR(10) NOT NULL,
    bought_price  DECIMAL(10, 3) NOT NULL,
    quantity      DECIMAL(10, 3) NOT NULL,
    updated_date  DATETIME NOT NULL,
    user_id       VARCHAR(10) NOT NULL
);

CREATE INDEX inventory__idx ON
    inventory (
        user_id
    ASC );

ALTER TABLE inventory ADD CONSTRAINT inventory_pk PRIMARY KEY ( inven_id );

CREATE TABLE item (
    item_id       VARCHAR(10) NOT NULL,
    code          VARCHAR(10) NOT NULL,
    name          VARCHAR(30) NOT NULL,
    updated_date  DATETIME NOT NULL,
    price_id      VARCHAR(10) NOT NULL
);

CREATE UNIQUE INDEX item__idx ON
    item (
        price_id
    ASC );

ALTER TABLE item ADD CONSTRAINT item_pk PRIMARY KEY ( item_id );

CREATE TABLE offer (
    offer_id      VARCHAR(10) NOT NULL,
    quantity      DECIMAL(10, 4) NOT NULL,
    buy_sell      CHAR(1) NOT NULL COMMENT 'True for Buy and False for Sell.',
    price         DECIMAL(10, 3) NOT NULL,
    ts            DATETIME NOT NULL,
    updated_date  DATETIME NOT NULL
);

/* Moved to CREATE TABLE
COMMENT ON COLUMN offer.buy_sell IS
    'True for Buy and False for Sell.'; */

ALTER TABLE offer ADD CONSTRAINT offer_pk PRIMARY KEY ( offer_id );

CREATE TABLE payment (
    pay_id        VARCHAR(10) NOT NULL,
    amount        DECIMAL(10, 3) NOT NULL,
    updated_date  DATETIME NOT NULL
);

ALTER TABLE payment ADD CONSTRAINT payment_pk PRIMARY KEY ( pay_id );

CREATE TABLE price (
    price_id      VARCHAR(10) NOT NULL,
    buy           DECIMAL(10, 3) NOT NULL,
    sell          DECIMAL(10, 3) NOT NULL,
    ts            DATETIME NOT NULL,
    updated_date  DATETIME NOT NULL
);

ALTER TABLE price ADD CONSTRAINT price_pk PRIMARY KEY ( price_id );

CREATE TABLE trade (
    trade_id      VARCHAR(10) NOT NULL,
    quantity      DECIMAL(10, 3) NOT NULL,
    unit_price    DECIMAL(10, 3) NOT NULL,
    updated_date  DATETIME NOT NULL,
    item_id       VARCHAR(10) NOT NULL,
    pay_id        VARCHAR(10) NOT NULL,
    buyer_id      VARCHAR(10) NOT NULL,
    seller_id     VARCHAR(10) NOT NULL
);

ALTER TABLE trade ADD CONSTRAINT trade_pk PRIMARY KEY ( trade_id );

CREATE TABLE trade_offer (
    pri       VARCHAR(10) NOT NULL,
    trade_id  VARCHAR(10) NOT NULL,
    offer_id  VARCHAR(10) NOT NULL
);

ALTER TABLE trade_offer ADD CONSTRAINT trade_offer_pk PRIMARY KEY ( pri );

CREATE TABLE user_data (
    user_id          VARCHAR(10) NOT NULL,
    first_name       VARCHAR(45) NOT NULL,
    last_name        VARCHAR(45) NOT NULL,
    username         VARCHAR(45) NOT NULL,
    password         VARCHAR(45) NOT NULL,
    email            VARCHAR(60) NOT NULL,
    time_registered  DATETIME,
    wallet           DECIMAL(10, 3) NOT NULL,
    dob              DATETIME NOT NULL,
    gender           VARCHAR(1) NOT NULL,
    updated_date     DATETIME NOT NULL
);

ALTER TABLE user_data ADD CONSTRAINT user_data_pk PRIMARY KEY ( user_id );

ALTER TABLE trade
    ADD CONSTRAINT item_fkv2 FOREIGN KEY ( item_id )
        REFERENCES item ( item_id );

ALTER TABLE trade_offer
    ADD CONSTRAINT offer_fk FOREIGN KEY ( offer_id )
        REFERENCES offer ( offer_id );

ALTER TABLE trade
    ADD CONSTRAINT payment_fk FOREIGN KEY ( pay_id )
        REFERENCES payment ( pay_id );

ALTER TABLE item
    ADD CONSTRAINT price_fk FOREIGN KEY ( price_id )
        REFERENCES price ( price_id );

ALTER TABLE trade_offer
    ADD CONSTRAINT trade_fk FOREIGN KEY ( trade_id )
        REFERENCES trade ( trade_id );

ALTER TABLE trade
    ADD CONSTRAINT user_data_fk FOREIGN KEY ( buyer_id )
        REFERENCES user_data ( user_id );

ALTER TABLE trade
    ADD CONSTRAINT user_data_fkv2 FOREIGN KEY ( seller_id )
        REFERENCES user_data ( user_id );

ALTER TABLE address
    ADD CONSTRAINT user_data_fkv3 FOREIGN KEY ( user_id )
        REFERENCES user_data ( user_id );

ALTER TABLE bank
    ADD CONSTRAINT user_data_fkv4 FOREIGN KEY ( user_id )
        REFERENCES user_data ( user_id );

ALTER TABLE inventory
    ADD CONSTRAINT user_data_fkv5 FOREIGN KEY ( user_id )
        REFERENCES user_data ( user_id );



-- SQLINES DEMO *** per Data Modeler Summary Report: 
-- 
-- SQLINES DEMO ***                        11
-- SQLINES DEMO ***                         2
-- SQLINES DEMO ***                        21
-- SQLINES DEMO ***                         0
-- SQLINES DEMO ***                         0
-- SQLINES DEMO ***                         0
-- SQLINES DEMO *** DY                      0
-- SQLINES DEMO ***                         0
-- SQLINES DEMO ***                         0
-- SQLINES DEMO ***                         0
-- SQLINES DEMO ***                         0
-- SQLINES DEMO ***  TYPE                   0
-- SQLINES DEMO ***  TYPE                   0
-- SQLINES DEMO ***  TYPE BODY              0
-- SQLINES DEMO ***                         0
-- SQLINES DEMO ***                         0
-- SQLINES DEMO ***                         0
-- SQLINES DEMO ***                         0
-- SQLINES DEMO ***                         0
-- SQLINES DEMO ***                         0
-- SQLINES DEMO ***                         0
-- SQLINES DEMO *** EGMENT                  0
-- SQLINES DEMO ***                         0
-- SQLINES DEMO *** ED VIEW                 0
-- SQLINES DEMO *** ED VIEW LOG             0
-- SQLINES DEMO ***                         0
-- SQLINES DEMO ***                         0
-- SQLINES DEMO ***                         0
-- 
-- SQLINES DEMO ***                         0
-- SQLINES DEMO ***                         0
-- 
-- SQLINES DEMO ***                         0
-- 
-- SQLINES DEMO ***                         0
-- SQLINES DEMO *** A                       0
-- SQLINES DEMO *** T                       0
-- 
-- SQLINES DEMO ***                         0
-- SQLINES DEMO ***                         0
