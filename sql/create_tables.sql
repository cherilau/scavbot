
CREATE TABLE IF NOT EXISTS s_group (
    name varchar(32) not null,  
    password varchar(32) not null,
    constraint group_pk primary key (name)
);


CREATE TABLE IF NOT EXISTS user (
    username VARCHAR(32) primary key,
    user_id BIGINT not null,   
    first_name VARCHAR(64),
    group_name varchar(32),
    CONSTRAINT user_fk foreign key (group_name) references s_group(name)
);

CREATE TABLE IF NOT EXISTS riddle (
    num TINYINT primary key,   
    answer TINYTEXT not null
);

CREATE TABLE IF NOT EXISTS timestamp (
    riddle TINYINT not null,   
    user VARCHAR(32) not null,
    timestamp datetime not null,
    CONSTRAINT timestamp_pk	primary key (riddle, user),
    CONSTRAINT timestamp_fk1 foreign key (riddle) references riddle(num),
    CONSTRAINT timestamp_fk2 foreign key (user) references user (username)
);