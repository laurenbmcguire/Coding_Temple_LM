CREATE TABLE "public.salesperson" (
	"salesperson_id" serial NOT NULL,
	"first_name" varchar(255) NOT NULL,
	"last_name" varchar(255) NOT NULL,
	CONSTRAINT "salesperson_pk" PRIMARY KEY ("salesperson_id")
) WITH (
  OIDS=FALSE
);



create  TABLE "public.car" (
	"car_id" serial NOT NULL,
	"salesperson_id" int ,
	"customer_id" int ,
	"invoice_id" int,
	"make" varchar(255) NOT NULL,
	"model" varchar(255) NOT NULL,
	"year" int NOT NULL,
	CONSTRAINT "car_pk" PRIMARY KEY ("car_id")
) WITH (
  OIDS=FALSE
);

CREATE TABLE "public.customer" (
	"customer_id" serial NOT NULL,
	"first_name" varchar(255) NOT NULL,
	"last_name" varchar(255) NOT NULL,
	CONSTRAINT "customer_pk" PRIMARY KEY ("customer_id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "public.invoice" (
	"invoice_id" serial NOT NULL,
	"salesperson_id" int NOT NULL,
	"car_id" int NOT NULL,
	"customer_id" serial NOT NULL,
	"car_price" int NOT NULL,
	CONSTRAINT "invoice_pk" PRIMARY KEY ("invoice_id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "public.repair_ticket" (
	"ticket_id" serial NOT NULL,
	"car_id" int NOT NULL,
	"customer_id" int NOT NULL,
	"work_needed" varchar(255) NOT NULL,
	"total_cost" int NOT NULL,
	CONSTRAINT "repair_ticket_pk" PRIMARY KEY ("ticket_id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "public.service_history" (
	"record_id" serial NOT NULL,
	"car_id" int NOT NULL,
	"ticket_id" int NOT NULL,
	"date" DATE NOT NULL,
	CONSTRAINT "service_history_pk" PRIMARY KEY ("record_id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "public.mechanic" (
	"mechanic_id" serial NOT NULL,
	"first_name" varchar(255) NOT NULL,
	"last_name" varchar(255) NOT NULL,
	CONSTRAINT "mechanic_pk" PRIMARY KEY ("mechanic_id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "public.parts" (
	"part_id" serial NOT NULL,
	"ticket_id" int NOT NULL,
	"part" varchar NOT NULL
	CONSTRAINT "parts_pk" PRIMARY KEY ("part_id")
) WITH (
  OIDS=FALSE
);




CREATE TABLE "public.junction" (
	"junction" serial NOT NULL,
	"ticket_id" int NOT NULL,
	"mechanic_id" int NOT NULL,
	CONSTRAINT "junction_pk" PRIMARY KEY ("junction")
) WITH (
  OIDS=FALSE
);




ALTER TABLE "public.car" ADD CONSTRAINT "car_fk0" FOREIGN KEY ("salesperson_id") REFERENCES "public.salesperson"("salesperson_id");
ALTER TABLE "public.car" ADD CONSTRAINT "car_fk1" FOREIGN KEY ("customer_id") REFERENCES "public.customer"("customer_id");
ALTER TABLE "public.car" ADD CONSTRAINT "car_fk2" FOREIGN KEY ("invoice_id") REFERENCES "public.invoice"("invoice_id");


ALTER TABLE "public.invoice" ADD CONSTRAINT "invoice_fk0" FOREIGN KEY ("salesperson_id") REFERENCES "public.salesperson"("salesperson_id");
ALTER TABLE "public.invoice" ADD CONSTRAINT "invoice_fk1" FOREIGN KEY ("car_id") REFERENCES "public.car"("car_id");
ALTER TABLE "public.invoice" ADD CONSTRAINT "invoice_fk2" FOREIGN KEY ("customer_id") REFERENCES "public.customer"("customer_id");

ALTER TABLE "public.repair_ticket" ADD CONSTRAINT "repair_ticket_fk0" FOREIGN KEY ("car_id") REFERENCES "public.car"("car_id");
ALTER TABLE "public.repair_ticket" ADD CONSTRAINT "repair_ticket_fk1" FOREIGN KEY ("customer_id") REFERENCES "public.customer"("customer_id");

ALTER TABLE "public.service_history" ADD CONSTRAINT "service_history_fk0" FOREIGN KEY ("car_id") REFERENCES "public.car"("car_id");
ALTER TABLE "public.service_history" ADD CONSTRAINT "service_history_fk1" FOREIGN KEY ("ticket_id") REFERENCES "public.repair_ticket"("ticket_id");


ALTER TABLE "public.parts" ADD CONSTRAINT "parts_fk0" FOREIGN KEY ("ticket_id") REFERENCES "public.repair_ticket"("ticket_id");

ALTER TABLE "public.junction" ADD CONSTRAINT "junction_fk0" FOREIGN KEY ("ticket_id") REFERENCES "public.repair_ticket"("ticket_id");
ALTER TABLE "public.junction" ADD CONSTRAINT "junction_fk1" FOREIGN KEY ("mechanic_id") REFERENCES "public.mechanic"("mechanic_id");




