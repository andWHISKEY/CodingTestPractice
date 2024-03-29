# -- 코드를 입력하세요
SELECT APNT_NO,	
(SELECT PT_NAME FROM PATIENT AS p WHERE p.PT_NO = ap.PT_NO) AS PT_NAME , 
PT_NO, MCDP_CD, 
(SELECT DR_NAME FROM DOCTOR AS d WHERE d.DR_ID = ap.MDDR_ID) AS DR_NAME, 
APNT_YMD
FROM APPOINTMENT AS ap
WHERE APNT_YMD LIKE '2022-04-13%' AND MCDP_CD='CS' AND APNT_CNCL_YN = 'N'
ORDER BY APNT_YMD ASC
