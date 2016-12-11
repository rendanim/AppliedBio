SELECT description
FROM gene
WHERE biotype LIKE "%_pseudogene"
AND description IS NOT NULL
AND description NOT LIKE "similar to%";