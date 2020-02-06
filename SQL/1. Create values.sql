--Create values for Vendor--

INSERT INTO Vendor (id, vendor_name, vendor_city, vendor_country)
VALUES (10, "Biedronka", "Warsaw", "Poland"),
(11, "Carrefour", "Warsaw", "Poland"),
(12, "Netflix", "Los Gatos", "USA"),
(13, "Spotify", "Stockholm", "Sweden"),
(14, "PSN", "San Mateo", "USA"),
(15, "Bar", NULL, NULL),
(16, "Discoclub", NULL, NULL),
(17, "Cinema", NULL, NULL),
(18, "Landlord garage", "Warsaw", "Poland"),
(19, "Landlord house", "Warsaw", "Poland"),
(20, "Train company", NULL, NULL),
(21, "Bus company", NULL, NULL),
(22, "Airline company", NULL, NULL),
(23, "BP", NULL, "Poland"),
(24, "Lotos", NULL, "Poland"),
(25, "Other", NULL, NULL);

--Create values for Sender--

INSERT INTO Sender (id, sender_name, sender_city, sender_country)
VALUES (10, "Work", "Warsaw", "Poland"),
(11, "Refund", NULL, NULL),
(12, "Family", NULL, NULL),
(13, "Friend", NULL, "Poland"),
(14, "Other", NULL, NULL);

--Create values for Category--

INSERT INTO Category (id, category_name)
VALUES (10, "Other"),
(11, "Salary"),
(12, "University"),
(13, "Netflix"),
(14, "Spotify"),
(22, "Food"),
(23, "Parties"),
(24, "Petrol"),
(25, "Rent"),
(26, "Multimedia services"),
(27, "University"),
(28, "Travels"),
(29, "Transport");

--Create values for User--

INSERT INTO User (id, username, first_name, second_name, email, user_city, prof_status, password)
VALUES (10, "jorge10", "Jorge", "Bueno", "jorge@gmail.com", "Warsaw", "Student", "jorbuepe123"),
(11, "alex11", "Alex", NULL, "alex@gmail.com", "Warsaw", "Worker", "alex123"),
(12, "robert12", "Robert", NULL, "robert@gmail.com", "Warsaw", "Student", "robert123"),
(13, "joanna13", "Joanna", NULL, "joanna@gmail.com", "Warsaw", "Worker", "joanna123");