SELECT species.name,
        COUNT(DISTINCT protein.accession)

FROM species
   INNER JOIN protein ON (protein.species=species.abbrev)
GROUP BY species.name;
    
