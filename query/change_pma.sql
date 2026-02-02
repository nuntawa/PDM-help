SELECT
                            I.ITEM_ID AS ITEM_ID_OLD,
                            I.ITEM_NAME AS ITEM_NAME_OLD,
                            I.PMA_CODE AS PMA_CODE_OLD,
                            I.PMA_CATEGORY_CODE AS PMA_CATEGORY_CODE_OLD,
                            I.PMA_SUB_CATEGORY_CODE AS PMA_SUB_CATEGORY_CODE_OLD,
                            :effectiveStartDateNew AS EFFECTIVE_START_DATE_NEW,
                            TO_CHAR(I.EFFECTIVE_START_DATE, 'yyyy-MM-dd') AS EFFECTIVE_START_DATE,
                            TO_CHAR(I.EFFECTIVE_END_DATE, 'yyyy-MM-dd') AS EFFECTIVE_END_DATE,
                            I.STATUS_FLAG,
                            I.ACTION_FLAG
                        FROM
                            (
                            SELECT DISTINCT
                                      IB.ITEM_ID
                                     , IB.ITEM_NAME
                                     , IB.PMA_CODE
                                     , PC.PMA_CATEGORY_ID
                                     , IB.PMA_CATEGORY_CODE
                                     , IB.PMA_SUB_CATEGORY_CODE
                                     , IB.EFFECTIVE_START_DATE
                                     , IB.EFFECTIVE_END_DATE
                                     , CP.STATUS_FLAG
                                     , CASE
                                        WHEN CP.ITEM_ID_OLD IS NOT NULL THEN 'EDIT'
                                        ELSE 'ADD'
                                     END AS ACTION_FLAG
                            FROM
                                "USER" U
                            JOIN COMPANY C ON
                                1 = 1
                            JOIN USER_PMA UP ON
                                U.USER_ID = UP.USER_ID
                                AND UP.COMPANY_ID = C.COMPANY_ID
                            LEFT JOIN PMA P ON
                                UP.PMA_ID = P.PMA_ID
                                AND P.COMPANY_ID = UP.COMPANY_ID
                                OR UP.IS_ALL_PMA = '1'
                            LEFT JOIN PMA_CATEGORY PC
                                   ON
                                (UP.PMA_CATEGORY_ID = PC.PMA_CATEGORY_ID
                                    AND UP.IS_ALL_CATEGORY = '0'
                                    AND UP.PMA_ID IS NOT NULL
                                    AND PC.PMA_ID = P.PMA_ID)
                                OR (UP.IS_ALL_CATEGORY = '1'
                                    AND UP.PMA_ID IS NOT NULL
                                    AND PC.PMA_ID = P.PMA_ID)
                                OR (UP.IS_ALL_PMA = '1'
                                    AND PC.PMA_ID = P.PMA_ID)
                            JOIN ITEM IB ON
                                IB.EFFECTIVE_END_DATE >= TRUNC(CURRENT_DATE)
                                AND IB.PMA_CODE = P.PMA_CODE
                                AND IB.PMA_CATEGORY_CODE = PC.PMA_CATEGORY_CODE
                                AND IB.COMPANY_ID = P.COMPANY_ID
                            LEFT JOIN CHANGE_PMA CP ON CP.ITEM_ID_OLD = IB.ITEM_ID
                                AND CP.PMA_CODE_OLD = IB.PMA_CODE
                            WHERE
                                1 = 1
                                AND U.IS_ACTIVE = '1'
                                AND U.IS_INTERNAL = '1'
                                AND (UP.IS_ALL_PMA = '1'
                                    OR (UP.PMA_ID IS NOT NULL
                                        AND (UP.IS_ALL_CATEGORY = '1'
                                            OR UP.PMA_CATEGORY_ID IS NOT NULL)
                                         )
                                    )
                            AND IB.COMPANY_ID = :companyId
                            AND P.PMA_ID = :pmaId
                            AND U.USER_ID = :userId
                            ) I
                        WHERE :effectiveStartDateNew BETWEEN I.EFFECTIVE_START_DATE AND I.EFFECTIVE_END_DATE
                        ORDER BY I.ITEM_ID, I.PMA_CODE , I.PMA_CATEGORY_CODE, I.PMA_SUB_CATEGORY_CODE, I.EFFECTIVE_START_DATE DESC