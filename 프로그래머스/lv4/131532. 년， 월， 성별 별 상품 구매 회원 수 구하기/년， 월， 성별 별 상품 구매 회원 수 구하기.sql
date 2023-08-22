-- 코드를 입력하세요
SELECT DATE_FORMAT(o.sales_date, '%Y') AS year
        , DATE_FORMAT(o.sales_date, '%m') AS month
        , u.gender
        , COUNT(DISTINCT u.user_id) AS users
    FROM 
        USER_INFO u
    INNER JOIN 
        ONLINE_SALE o
    ON 
        u.USER_ID = o.USER_ID
    WHERE 
        u.GENDER IS NOT NULL
    GROUP BY 
        YEAR, MONTH, u.GENDER
        # s.SALES_DATE
    ORDER BY 
        YEAR, MONTH, u.GENDER
        # YEAR(s.SALES_DATE) ASC, 
        # MONTH(s.SALES_DATE) ASC, 
        # u.GENDER ASC
