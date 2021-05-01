use ringer;

select * from User;

-- ALTER TABLE User
-- MODIFY password
-- varchar(300);


SET FOREIGN_KEY_CHECKS = 0; 
TRUNCATE TABLE User;
TRUNCATE TABLE address;
SET FOREIGN_KEY_CHECKS = 1;


select * from bank order by user_id;
