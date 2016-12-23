CREATE TABLE Tasks (
  tid INT AUTO_INCREMENT,
  title VARCHAR(100),
  due_date DATE,
  status VARCHAR(1),
  PRIMARY KEY(tid)
)
engine=innodb;

CREATE TABLE Completed (
  tid INT,
  title VARCHAR(100),
  due_date DATE,
  comp_date DATE,
  status VARCHAR(1),
  PRIMARY KEY (tid)
)
engine=innodb;

INSERT INTO Tasks(title, due_date, status)
VALUES ('Test 1', '2016-12-31', '0'),
  ('Test 2', '2016-12-15', '0'),
  ('Test 3', '2016-12-31', '1');
