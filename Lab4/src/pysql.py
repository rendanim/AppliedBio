#!/usr/bin/env python3
import sqlite3 as sql


def main():
    conn = sql.connect('final2.db')
    c = conn.cursor()
    print('---------QUERY 1-----------')
    q1 = 'SELECT COUNT(DISTINCT abbrev) FROM species;'
    result1=c.execute(q1)
    for row in result1:
        print(row[0])
    '''print('---------QUERY 2-----------')    
    q2="INSERT INTO species(abbrev,name,common) VALUES ('Ss','Sus scrofa','Feral Pig');"
    result2=c.execute(q2)
    for row in result2:
        print(row) '''
    print('---------QUERY 3-----------')
    q3="SELECT  accession, species FROM protein WHERE length(sequence)>1000;"
    result3=c.execute(q3)
    for row in result3:
         print(str(row[0]).ljust(5)+'\t'+str(row[1]).ljust(5))    

    print('---------QUERY 4-----------')
    q4 = """SELECT species.name, 
                familymembers.family,
                familymembers.protein
        FROM familymembers
        INNER JOIN protein ON (familymembers.protein=protein.accession)
        INNER JOIN species ON (protein.species=species.abbrev)
        WHERE familymembers.family='NHR3';""" 
        
    result4=c.execute(q4)
    for row in result4:
        print(str(row[0]).ljust(5)+'\t'+str(row[1]).ljust(5)+'\t'+str(row[2]).ljust(5)) 
    print('---------QUERY 5-----------')  
    q5 = """SELECT species.name,
         COUNT(DISTINCT protein.accession)

        FROM species
        INNER JOIN protein ON (protein.species=species.abbrev)
        GROUP BY species.name;"""
    result5=c.execute(q5)
    for row in result5:
        print(str(row[0]).ljust(5)+'\t'+str(row[1]).ljust(5))           
    c.close() 
if __name__=='__main__':
    main()