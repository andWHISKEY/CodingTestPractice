with A as (
    SELECT APNT_NO,A.MCDP_CD,DR_NAME,APNT_YMD,PT_NO
    FROM APPOINTMENT A join DOCTOR D on A.MDDR_ID=D.DR_ID
    WHERE APNT_YMD like '2022-04-13%' and A.MCDP_CD='CS' and APNT_CNCL_YN='N'
),

B as (
    SELECT APNT_NO,PT_NAME,A.PT_NO,A.MCDP_CD,DR_NAME,APNT_YMD
    FROM A join PATIENT P on A.PT_NO=P.PT_NO
    ORDER BY APNT_YMD asc
)

-- 코드를 입력하세요
SELECT *
FROM B
