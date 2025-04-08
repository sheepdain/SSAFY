PRAGMA table_info(invoices);

SELECT BillingCountry, sum(total) FROM invoices GROUP BY "BillingCountry";

SELECT strftime('%Y', "InvoiceDate"), sum("Total") FROM invoices
GROUP BY strftime('%Y', "InvoiceDate");

SELECT BillingState, sum(Total) FROM invoices
WHERE "BillingCountry"='USA' and "InvoiceDate">'2010-01-01'
GROUP BY "BillingState"

SELECT BillingCountry, max(Total) FROM invoices
WHERE "BillingCountry" IN ('Germany', 'France')
GROUP BY "BillingCountry"