SELECT i.ANIMAL_ID,i.ANIMAL_TYPE,i.NAME
FROM ANIMAL_INS AS i INNER JOIN ANIMAL_OUTS AS o
ON i.ANIMAL_ID = o.ANIMAL_ID
WHERE i.SEX_UPON_INTAKE!=o.SEX_UPON_OUTCOME