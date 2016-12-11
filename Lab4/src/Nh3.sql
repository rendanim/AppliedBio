SELECT species.name,
        familymembers.family,
        familymembers.protein

FROM familymembers
    INNER JOIN protein ON (familymembers.protein=protein.accession)
    INNER JOIN species ON (protein.species=species.abbrev)
WHERE familymembers.family='NHR3';    
