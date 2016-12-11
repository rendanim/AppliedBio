SELECT biotype,
COUNT(gene_id)
FROM gene 
GROUP BY biotype;