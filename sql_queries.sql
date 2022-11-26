CREATE TABLE User (
	username TEXT,
	name TEXT,
	phoneno TEXT,
	emailaddress TEXT,
	PRIMARY KEY (username)
);

CREATE TABLE Fooditem (
	id INTEGER,
	name TEXT,
	price TEXT,
	description TEXT,
	PRIMARY KEY (id)
);

INSERT INTO Fooditem VALUES (1, 'Veg Pizza', 10, 'Loaded with various vegetarian toppings, Domino’s veg pizza range is what a vegetarian would love to explore.');
INSERT INTO Fooditem VALUES (2, 'Burger Pizza', 20, 'A burger pizza combines the best flavors from both a pizza and a burger. The buns of the burger pizza are made using fresh pizza dough seasoned with secret herbs.');
INSERT INTO Fooditem VALUES (3, 'Fresh Pan Pizza', 20, 'A fresh pan pizza is more buttery, crispy on the edges, and soft on the inside. The dough is generally fluffy in a fresh pan pizza which gives it a distinct taste.');
INSERT INTO Fooditem VALUES (4, 'Detroit Pizza', 20, 'A Detroit pizza features a thick crust that is chewy and crispy. It is generally rectangular and features smaller portions of pepperoni that curl up while baking resembling a miniature cup.');
INSERT INTO Fooditem VALUES (5, 'Chicken Fiesta Pizza', 30, 'Domino’s non veg pizza is full of pizzas loaded with chicken and other non-vegetarian toppings. These pizzas seamlessly combine the best of Indian and Italian flavors, so it is a must-try.');

CREATE TABLE Orders (
	id INTEGER,
	username TEXT,
	name TEXT,
	amount INTEGER,
	PRIMARY KEY (id AUTOINCREMENT)
);

