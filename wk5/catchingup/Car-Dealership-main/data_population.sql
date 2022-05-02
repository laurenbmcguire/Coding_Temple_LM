insert into public."public.salesperson"  (first_name, last_name)
values
('BOb', 'Odenkirk'),
('Rhea', 'Seehorn'),
('Michael', 'Mando'),
('Jonathan', 'Banks'),
('Tony', 'Dalton')


insert into public."public.customer"  (first_name, last_name)
values
('Bryan', 'Cranston'),
('Aaron', 'Paul'),
('Anna', 'Gun'),
('Krysten', 'Ritter'),
('RJ', 'Mitte'),
('Giancarlo', 'Esposito'),
('Dean', 'Norris'),
('Jesse', 'Plemons'),
('Matt', 'Jones'),
('David', 'Costabile')

insert into public."public.car"  (salesperson_id, customer_id, invoice_id, make, model, year)
values
(null, 2, null, 'Honda', 'Fit', 2015),
(1, 2, null, 'Honda', 'Fit', 2015),
(null, 6, null, 'Nissan', 'Centra', 2019), --only here for repair
(4, 9, null, 'Chevrolet', 'Camaro', 2022), --not sold yet
(3, null, null, 'Ford', 'Focus', 2016), --not sold yet
(3, null, null, 'Tesla', 'Model Y', 2022),--not sold yet
(3, null, null, 'Apple', 'iCar', 2050),
(2, 6, null, 'Ford', 'Mustang', 2022),
(4, 1, null, 'Ford', 'Explorer', 2020),
(1, 2, null, 'Ford', 'Bronco', 2020),
(2, 3, null, 'Ford', 'GT', 2020),
(3, 4, null, 'Ford', 'Expedition', 2019),
(4, 5, null, 'Ford', 'F-150', 2022),
(5, 6, null, 'Ford', 'Explorer', 2022),
(1, 7, null, 'Ford', 'Focus', 2015),
(2, 8, null, 'Ford', 'Mustang', 2022),
(3, 9, null, 'Ford', 'Mustang', 2022), --only here for repair
(4, 1, null, 'Ford', 'Mustang', 2022),
(5, 2, null, 'Ford', 'Mustang', 2022)
(null, 6, null, 'Nissan', 'Centra', 2019), --only here for repair
(null, 9, null, 'Chevrolet', 'Camaro', 2000), --only here for repair
(null, 3, null, 'Honda', 'Civic', 2016), --only here for repair
(null, 1, null, 'Honda', 'Accord', 2022) --only here for repair

insert into public."public.invoice"  (salesperson_id, car_id, customer_id, car_price)
values
(1, 73, 2, 14000),
(4, 75, 9, 20000),
(2, 79, 6, 50000),
(4, 80, 1, 84000),
(1, 81, 2, 80000),
(2, 82, 3, 100000),
(3, 83, 4, 90000),
(4, 84, 5, 60000),
(5, 85, 6, 20000),
(1, 86, 7, 50000),
(2, 87, 8, 40000),
(3, 88, 9, 5500),
(4, 89, 1, 50000),
(5, 90, 2, 60000)


UPDATE public."public.car"
SET invoice_id  = 1
WHERE car_id = 73;
UPDATE public."public.car"
SET invoice_id  = 2
WHERE car_id = 75;
UPDATE public."public.car"
SET invoice_id  = 3
WHERE car_id = 79;
UPDATE public."public.car"
SET invoice_id  = 4
WHERE car_id = 80;
UPDATE public."public.car"
SET invoice_id  = 5
WHERE car_id = 81;
UPDATE public."public.car"
SET invoice_id  = 6
WHERE car_id = 82;
UPDATE public."public.car"
SET invoice_id  = 7
WHERE car_id = 83;
UPDATE public."public.car"
SET invoice_id  = 8
WHERE car_id = 84;
UPDATE public."public.car"
SET invoice_id  = 9
WHERE car_id = 85;
UPDATE public."public.car"
SET invoice_id  = 10
WHERE car_id = 86;
UPDATE public."public.car"
SET invoice_id  = 11
WHERE car_id = 87;
UPDATE public."public.car"
SET invoice_id  = 12
WHERE car_id = 88;
UPDATE public."public.car"
SET invoice_id  = 13
WHERE car_id = 89;
UPDATE public."public.car"
SET invoice_id  = 14
WHERE car_id = 90

insert into public."public.mechanic"  (first_name, last_name)
values
('Robert', 'Forster'),
('Charles', 'Baker'),
('Scott', 'MacArthur')

insert into public."public.repair_ticket"  (car_id, customer_id, work_needed, total_cost)
values
(91, 6, 'Oil Change', 75),
(92, 9, 'Tire Rotation', 30),
(93, 3, 'Oil Change', 75),
(94, 1, 'Tire Rotation', 30),
(74, 1, 'Tire Rotation', 30)

insert into public."public.junction"  (ticket_id, mechanic_id)
values
(1,1),
(1,2),
(1,3),
(2,3),
(3,2),
(4,1),
(5,2)

insert into public."public.parts"  (ticket_id, part)
values
(2, 'New Tires')

insert into public."public.service_history"  (car_id, ticket_id, date)
values
(91, 1, '2022/04/03'),
(92, 2, '2022/04/03'),
(93, 3, '2022/04/03'),
(94, 4, '2022/04/03'),
(74, 5, '2022/04/03')