-- Active: 1744070835207@@127.0.0.1@3306
SELECT Invoiceid, InvoiceDate FROM invoices;

SELECT * FROM invoices WHERE "BillingCountry"='USA' and "Total">10;

SELECT * FROM invoices
WHERE "BillingCity" IN ('London', 'Berlin');

SELECT * FROM invoices
WHERE "Total"=(SELECT max("Total") FROM invoices);

SELECT * FROM invoices
WHERE "InvoiceDate">'2013-03-31' AND "Total">3;

SELECT * FROM invoices
WHERE "BillingCountry"='USA' AND "BillingState"='CA' AND "Total">10;

SELECT * FROM invoices
WHERE "BillingCountry"='Canada' AND "BillingState"='ON' AND "BillingCity"='Toronto';

SELECT * FROM invoices
WHERE "InvoiceDate"<'2023-01-01' AND ("Total">=50 or "BillingCountry"='Brazil')