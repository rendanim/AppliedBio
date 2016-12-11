SELECT  accession,
        species
FROM protein
WHERE length("sequence")>1000;