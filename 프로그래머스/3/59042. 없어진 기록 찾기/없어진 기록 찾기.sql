SELECT o.ANIMAL_ID,o.NAME
FROM ANIMAL_INS AS i RIGHT OUTER JOIN ANIMAL_OUTS AS o
ON i.ANIMAL_ID=o.ANIMAL_ID
WHERE o.ANIMAL_ID NOT IN (select ANIMAL_ID from ANIMAL_INS) # NULL #AND o.ANIMAL_ID!=NULL
#select * from ANIMAL_INS;