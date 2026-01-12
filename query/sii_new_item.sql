WITH UP
                         AS (SELECT USER_ID,
                                    PMA_ID,
                                    PMA_CATEGORY_ID,
                                    IS_ALL_PMA,
                                    IS_ALL_CATEGORY
                             FROM   %s.USER_PMA
                             WHERE  COMPANY_ID = :companyId
                                    AND USER_ID = :userId),
                         ITEM_STATUS
                         AS (SELECT ITEM_ID,
                                    CASE
                                      WHEN MAX(CASE
                                                 WHEN EFFECTIVE_END_DATE = DATE '9999-12-31' THEN 1
                                                 ELSE 0
                                               END) = 1 THEN 'A'
                                      ELSE 'S'
                                    END AS STATUS
                             FROM   %s.ITEM
                             WHERE  COMPANY_ID = :companyId
                             GROUP  BY ITEM_ID),
                         ITEM_MIN_STATUS
                         AS (SELECT ITEM_ID,
                                    MIN(EFFECTIVE_START_DATE) AS MIN_EFFECTIVE_START_DATE
                             FROM   %s.ITEM
                             WHERE  COMPANY_ID = :companyId
                             GROUP  BY ITEM_ID)
                    SELECT          I.ITEM_ID,
                                    I.ITEM_NAME,
                                    P.PMA_ID,
                                    P.PMA_CODE,
                                    P.PMA_NAME,
                                    PC.PMA_CATEGORY_ID,
                                    PC.PMA_CATEGORY_CODE,
                                    PC.PMA_CATEGORY_NAME,
                                    PSC.PMA_SUB_CATEGORY_ID,
                                    PSC.PMA_SUB_CATEGORY_CODE,
                                    PSC.PMA_SUB_CATEGORY_NAME,
                                    I.EFFECTIVE_START_DATE,
                                    I.EFFECTIVE_END_DATE,
                                    IS2.STATUS               AS STATUS,
                                    CASE
                                      WHEN IMS.MIN_EFFECTIVE_START_DATE = I.EFFECTIVE_START_DATE THEN 'Y'
                                      ELSE 'N'
                                    END                      AS ITEM_STATUS,
                                    I.UNIT_SIZE,
                                    I.UNIT_TYPE,
                                    I.SII_FLAG,
                                    CCSF.CODE_NAME           AS SII_FLAG_NAME,
                                    I.INVENTORY_CHECK_FLAG,
                                    CCICF.CODE_NAME          AS INVENTORY_CHECK_FLAG_NAME,
                                    I.ORDER_TYPE,
                                    CCOT.CODE_NAME           AS ORDER_TYPE_NAME,
                                    I.ORDER_GROUP,
                                    CCOG.CODE_NAME           AS ORDER_GROUP_NAME,
                                    I.ORDER_FLAG,
                                    CCOF.CODE_NAME           AS ORDER_FLAG_NAME,
                                    I.UPDATED_DATE,
                                    ICC2.ORDER_UNIT_QTY      AS PRICE_SIZE,
                                    CASE
                                      WHEN ICC2.ORDER_UNIT_QTY IS NULL THEN NULL
                                      ELSE '1x'
                                           || ICC2.ORDER_UNIT_QTY
                                    END                      AS PRICE_PACK_SIZE,
                                    ICC2.FINAL_NET_UNIT_COST AS PRICE,
                                    CASE
                                      WHEN ( ( LAG(ICC2.FINAL_NET_UNIT_COST)
                                                 OVER (
                                                   PARTITION BY I.ITEM_ID
                                                   ORDER BY I.EFFECTIVE_START_DATE) IS NULL
                                               AND ICC2.FINAL_NET_UNIT_COST IS NOT NULL )
                                              OR ( LAG(ICC2.FINAL_NET_UNIT_COST)
                                                     OVER (
                                                       PARTITION BY I.ITEM_ID
                                                       ORDER BY I.EFFECTIVE_START_DATE) IS NOT NULL
                                                   AND ICC2.FINAL_NET_UNIT_COST IS NULL )
                                              OR ( LAG(ICC2.FINAL_NET_UNIT_COST)
                                                     OVER (
                                                       PARTITION BY I.ITEM_ID
                                                       ORDER BY I.EFFECTIVE_START_DATE) <> ICC2.FINAL_NET_UNIT_COST ) ) THEN 'Y'
                                      ELSE 'N'
                                    END                      AS PRICE_FLAG,
                                    ICR.SELLING_UNIT_QTY     AS RETAIL_SIZE,
                                    CASE
                                      WHEN ICR.SELLING_UNIT_QTY IS NULL THEN NULL
                                      ELSE '1x'
                                           || ICR.SELLING_UNIT_QTY
                                    END                      AS RETAIL_PACK_SIZE,
                                    ICR.RETAIL,
                                    CASE
                                      WHEN ( ( LAG(ICR.SELLING_UNIT_QTY)
                                                 OVER (
                                                   PARTITION BY I.ITEM_ID
                                                   ORDER BY I.EFFECTIVE_START_DATE) IS NULL
                                               AND ICR.SELLING_UNIT_QTY IS NOT NULL )
                                              OR ( LAG(ICR.SELLING_UNIT_QTY)
                                                     OVER (
                                                       PARTITION BY I.ITEM_ID
                                                       ORDER BY I.EFFECTIVE_START_DATE) IS NOT NULL
                                                   AND ICR.SELLING_UNIT_QTY IS NULL )
                                              OR ( LAG(ICR.SELLING_UNIT_QTY)
                                                     OVER (
                                                       PARTITION BY I.ITEM_ID
                                                       ORDER BY I.EFFECTIVE_START_DATE) <> ICR.SELLING_UNIT_QTY ) ) THEN 'Y'
                                      ELSE 'N'
                                    END                      AS RETAIL_FLAG
                    FROM   %s.ITEM I
                           JOIN ITEM_STATUS IS2
                             ON IS2.ITEM_ID = I.ITEM_ID
                           JOIN ITEM_MIN_STATUS IMS
                             ON IMS.ITEM_ID = I.ITEM_ID
                           JOIN %s.PMA P
                             ON P.PMA_CODE = I.PMA_CODE
                                AND P.COMPANY_ID = I.COMPANY_ID
                           JOIN %s.PMA_CATEGORY PC
                             ON PC.PMA_CATEGORY_CODE = I.PMA_CATEGORY_CODE
                                AND PC.PMA_ID = P.PMA_ID
                           JOIN %s.PMA_SUB_CATEGORY PSC
                             ON PSC.PMA_SUB_CATEGORY_CODE = I.PMA_SUB_CATEGORY_CODE
                                AND PSC.PMA_CATEGORY_ID = PC.PMA_CATEGORY_ID
                           JOIN UP
                             ON ( UP.IS_ALL_PMA = 1
                                   OR UP.PMA_ID = P.PMA_ID )
                                AND ( UP.IS_ALL_CATEGORY = 1
                                       OR UP.PMA_CATEGORY_ID = PC.PMA_CATEGORY_ID )
                           JOIN %s."USER" U
                             ON U.USER_ID = UP.USER_ID
                           LEFT JOIN (SELECT ITEM_ID,
                                             DELIVERY_TYPE_CODE,
                                             ORDER_UNIT_QTY,
                                             FINAL_NET_UNIT_COST,
                                             EFFECTIVE_START_DATE,
                                             EFFECTIVE_END_DATE,
                                             VENDOR_ID,
                                             VENDOR_SUB_ID,
                                             ROW_NUMBER()
                                               OVER(
                                                 PARTITION BY ITEM_ID
                                                 ORDER BY VENDOR_ID DESC, VENDOR_SUB_ID DESC, EFFECTIVE_END_DATE DESC) RN
                                      FROM   %s.ITEM_CONTROL_C2) ICC2
                                  ON ICC2.ITEM_ID = I.ITEM_ID
                                     AND ICC2.DELIVERY_TYPE_CODE = I.DELIVERY_TYPE_CODE
                                     AND I.EFFECTIVE_START_DATE BETWEEN ICC2.EFFECTIVE_START_DATE AND ICC2.EFFECTIVE_END_DATE
                                     AND ICC2.RN = 1
                           LEFT JOIN (SELECT ITEM_ID,
                                             SELLING_UNIT_QTY,
                                             RETAIL,
                                             EFFECTIVE_START_DATE,
                                             EFFECTIVE_END_DATE,
                                             ROW_NUMBER()
                                               OVER(
                                                 PARTITION BY ITEM_ID
                                                 ORDER BY EFFECTIVE_END_DATE DESC) RN
                                      FROM   %s.ITEM_CONTROL_RETAIL) ICR
                                  ON ICR.ITEM_ID = I.ITEM_ID
                                     AND I.EFFECTIVE_START_DATE BETWEEN ICR.EFFECTIVE_START_DATE AND ICR.EFFECTIVE_END_DATE
                                     AND ICR.RN = 1
                           JOIN %s.COMMON_CODE CCSF
                             ON CCSF.CODE_TYPE = '00081'
                                AND CCSF.CODE_VALUE = I.SII_FLAG
                           JOIN %s.COMMON_CODE CCICF
                             ON CCICF.CODE_TYPE = '01018'
                                AND CCICF.CODE_VALUE = I.INVENTORY_CHECK_FLAG
                           JOIN %s.COMMON_CODE CCOT
                             ON CCOT.CODE_TYPE = '00500'
                                AND CCOT.CODE_VALUE = I.ORDER_TYPE
                           JOIN %s.COMMON_CODE CCOG
                             ON CCOG.CODE_TYPE = '01201'
                                AND CCOG.CODE_VALUE = I.ORDER_GROUP
                           JOIN %s.COMMON_CODE CCOF
                             ON CCOF.CODE_TYPE = '01202'
                                AND CCOF.CODE_VALUE = I.ORDER_FLAG
                    WHERE  I.COMPANY_ID = :companyId
                           AND P.PMA_ID BETWEEN :pmaIdFrom AND NVL(:pmaIdTo, :pmaIdFrom)
                           AND I.EFFECTIVE_START_DATE BETWEEN :effectiveStartDateFrom AND :effectiveStartDateTo
                           AND ( :status = 'ALL'
                                  OR ( :status = 'A'
                                       AND IS2.STATUS = 'A' )
                                  OR ( :status = 'S'
                                       AND IS2.STATUS = 'S' ) )
                           AND ( :siiFlag = 'ALL'
                                  OR ( :siiFlag = 'SII'
                                       AND I.SII_FLAG = 'Y' ) )
                           AND ( :inventoryCheckFlag = 'ALL'
                                  OR ( :inventoryCheckFlag = 'Y'
                                       AND I.INVENTORY_CHECK_FLAG = 'Y' )
                                  OR ( :inventoryCheckFlag = 'N'
                                       AND I.INVENTORY_CHECK_FLAG = 'N' ) )
------------------------------------------------------------------------------
WITH UP
                         AS (SELECT USER_ID,
                                    PMA_ID,
                                    PMA_CATEGORY_ID,
                                    IS_ALL_PMA,
                                    IS_ALL_CATEGORY
                             FROM   USER_PMA
                             WHERE  COMPANY_ID = :companyId
                                    AND USER_ID = :userId),
                         ITEM_STATUS
                         AS (SELECT ITEM_ID,
                                    CASE
                                      WHEN MAX(CASE
                                                 WHEN EFFECTIVE_END_DATE = DATE '9999-12-31' THEN 1
                                                 ELSE 0
                                               END) = 1 THEN 'A'
                                      ELSE 'S'
                                    END AS STATUS
                             FROM   ITEM
                             WHERE  COMPANY_ID = :companyId
                             GROUP  BY ITEM_ID),
                         ITEM_MIN_STATUS
                         AS (SELECT ITEM_ID,
                                    MIN(EFFECTIVE_START_DATE) AS MIN_EFFECTIVE_START_DATE
                             FROM   ITEM
                             WHERE  COMPANY_ID = :companyId
                             GROUP  BY ITEM_ID)
                    SELECT          I.ITEM_ID,
                                    I.ITEM_NAME,
                                    P.PMA_ID,
                                    P.PMA_CODE,
                                    P.PMA_NAME,
                                    PC.PMA_CATEGORY_ID,
                                    PC.PMA_CATEGORY_CODE,
                                    PC.PMA_CATEGORY_NAME,
                                    PSC.PMA_SUB_CATEGORY_ID,
                                    PSC.PMA_SUB_CATEGORY_CODE,
                                    PSC.PMA_SUB_CATEGORY_NAME,
                                    I.EFFECTIVE_START_DATE,
                                    I.EFFECTIVE_END_DATE,
                                    IS2.STATUS               AS STATUS,
                                    CASE
                                      WHEN IMS.MIN_EFFECTIVE_START_DATE = I.EFFECTIVE_START_DATE THEN 'Y'
                                      ELSE 'N'
                                    END                      AS ITEM_STATUS,
                                    I.UNIT_SIZE,
                                    I.UNIT_TYPE,
                                    I.SII_FLAG,
                                    CCSF.CODE_NAME           AS SII_FLAG_NAME,
                                    I.INVENTORY_CHECK_FLAG,
                                    CCICF.CODE_NAME          AS INVENTORY_CHECK_FLAG_NAME,
                                    I.ORDER_TYPE,
                                    CCOT.CODE_NAME           AS ORDER_TYPE_NAME,
                                    I.ORDER_GROUP,
                                    CCOG.CODE_NAME           AS ORDER_GROUP_NAME,
                                    I.ORDER_FLAG,
                                    CCOF.CODE_NAME           AS ORDER_FLAG_NAME,
                                    I.UPDATED_DATE,
                                    ICC2.ORDER_UNIT_QTY      AS PRICE_SIZE,
                                    CASE
                                      WHEN ICC2.ORDER_UNIT_QTY IS NULL THEN NULL
                                      ELSE '1x'
                                           || ICC2.ORDER_UNIT_QTY
                                    END                      AS PRICE_PACK_SIZE,
                                    ICC2.FINAL_NET_UNIT_COST AS PRICE,
                                    CASE
                                      WHEN ( ( LAG(ICC2.FINAL_NET_UNIT_COST)
                                                 OVER (
                                                   PARTITION BY I.ITEM_ID
                                                   ORDER BY I.EFFECTIVE_START_DATE) IS NULL
                                               AND ICC2.FINAL_NET_UNIT_COST IS NOT NULL )
                                              OR ( LAG(ICC2.FINAL_NET_UNIT_COST)
                                                     OVER (
                                                       PARTITION BY I.ITEM_ID
                                                       ORDER BY I.EFFECTIVE_START_DATE) IS NOT NULL
                                                   AND ICC2.FINAL_NET_UNIT_COST IS NULL )
                                              OR ( LAG(ICC2.FINAL_NET_UNIT_COST)
                                                     OVER (
                                                       PARTITION BY I.ITEM_ID
                                                       ORDER BY I.EFFECTIVE_START_DATE) <> ICC2.FINAL_NET_UNIT_COST ) ) THEN 'Y'
                                      ELSE 'N'
                                    END                      AS PRICE_FLAG,
                                    ICR.SELLING_UNIT_QTY     AS RETAIL_SIZE,
                                    CASE
                                      WHEN ICR.SELLING_UNIT_QTY IS NULL THEN NULL
                                      ELSE '1x'
                                           || ICR.SELLING_UNIT_QTY
                                    END                      AS RETAIL_PACK_SIZE,
                                    ICR.RETAIL,
                                    CASE
                                      WHEN ( ( LAG(ICR.SELLING_UNIT_QTY)
                                                 OVER (
                                                   PARTITION BY I.ITEM_ID
                                                   ORDER BY I.EFFECTIVE_START_DATE) IS NULL
                                               AND ICR.SELLING_UNIT_QTY IS NOT NULL )
                                              OR ( LAG(ICR.SELLING_UNIT_QTY)
                                                     OVER (
                                                       PARTITION BY I.ITEM_ID
                                                       ORDER BY I.EFFECTIVE_START_DATE) IS NOT NULL
                                                   AND ICR.SELLING_UNIT_QTY IS NULL )
                                              OR ( LAG(ICR.SELLING_UNIT_QTY)
                                                     OVER (
                                                       PARTITION BY I.ITEM_ID
                                                       ORDER BY I.EFFECTIVE_START_DATE) <> ICR.SELLING_UNIT_QTY ) ) THEN 'Y'
                                      ELSE 'N'
                                    END                      AS RETAIL_FLAG
                    FROM   ITEM I
                           JOIN ITEM_STATUS IS2
                             ON IS2.ITEM_ID = I.ITEM_ID
                           JOIN ITEM_MIN_STATUS IMS
                             ON IMS.ITEM_ID = I.ITEM_ID
                           JOIN PMA P
                             ON P.PMA_CODE = I.PMA_CODE
                                AND P.COMPANY_ID = I.COMPANY_ID
                           JOIN PMA_CATEGORY PC
                             ON PC.PMA_CATEGORY_CODE = I.PMA_CATEGORY_CODE
                                AND PC.PMA_ID = P.PMA_ID
                           JOIN PMA_SUB_CATEGORY PSC
                             ON PSC.PMA_SUB_CATEGORY_CODE = I.PMA_SUB_CATEGORY_CODE
                                AND PSC.PMA_CATEGORY_ID = PC.PMA_CATEGORY_ID
                           JOIN UP
                             ON ( UP.IS_ALL_PMA = 1
                                   OR UP.PMA_ID = P.PMA_ID )
                                AND ( UP.IS_ALL_CATEGORY = 1
                                       OR UP.PMA_CATEGORY_ID = PC.PMA_CATEGORY_ID )
                           JOIN "USER" U
                             ON U.USER_ID = UP.USER_ID
                           LEFT JOIN (SELECT ITEM_ID,
                                             DELIVERY_TYPE_CODE,
                                             ORDER_UNIT_QTY,
                                             FINAL_NET_UNIT_COST,
                                             EFFECTIVE_START_DATE,
                                             EFFECTIVE_END_DATE,
                                             VENDOR_ID,
                                             VENDOR_SUB_ID,
                                             ROW_NUMBER()
                                               OVER(
                                                 PARTITION BY ITEM_ID
                                                 ORDER BY VENDOR_ID DESC, VENDOR_SUB_ID DESC, EFFECTIVE_END_DATE DESC) RN
                                      FROM   ITEM_CONTROL_C2) ICC2
                                  ON ICC2.ITEM_ID = I.ITEM_ID
                                     AND ICC2.DELIVERY_TYPE_CODE = I.DELIVERY_TYPE_CODE
                                     AND I.EFFECTIVE_START_DATE BETWEEN ICC2.EFFECTIVE_START_DATE AND ICC2.EFFECTIVE_END_DATE
                                     AND ICC2.RN = 1
                           LEFT JOIN (SELECT ITEM_ID,
                                             SELLING_UNIT_QTY,
                                             RETAIL,
                                             EFFECTIVE_START_DATE,
                                             EFFECTIVE_END_DATE,
                                             ROW_NUMBER()
                                               OVER(
                                                 PARTITION BY ITEM_ID
                                                 ORDER BY EFFECTIVE_END_DATE DESC) RN
                                      FROM   ITEM_CONTROL_RETAIL) ICR
                                  ON ICR.ITEM_ID = I.ITEM_ID
                                     AND I.EFFECTIVE_START_DATE BETWEEN ICR.EFFECTIVE_START_DATE AND ICR.EFFECTIVE_END_DATE
                                     AND ICR.RN = 1
                           JOIN COMMON_CODE CCSF
                             ON CCSF.CODE_TYPE = '00081'
                                AND CCSF.CODE_VALUE = I.SII_FLAG
                           JOIN COMMON_CODE CCICF
                             ON CCICF.CODE_TYPE = '01018'
                                AND CCICF.CODE_VALUE = I.INVENTORY_CHECK_FLAG
                           JOIN COMMON_CODE CCOT
                             ON CCOT.CODE_TYPE = '00500'
                                AND CCOT.CODE_VALUE = I.ORDER_TYPE
                           JOIN COMMON_CODE CCOG
                             ON CCOG.CODE_TYPE = '01201'
                                AND CCOG.CODE_VALUE = I.ORDER_GROUP
                           JOIN COMMON_CODE CCOF
                             ON CCOF.CODE_TYPE = '01202'
                                AND CCOF.CODE_VALUE = I.ORDER_FLAG
                    WHERE  I.COMPANY_ID = :companyId
                           AND P.PMA_ID BETWEEN :pmaIdFrom AND NVL(:pmaIdTo, :pmaIdFrom)
                           AND I.EFFECTIVE_START_DATE BETWEEN :effectiveStartDateFrom AND :effectiveStartDateTo
                           AND ( :status = 'ALL'
                                  OR ( :status = 'A'
                                       AND IS2.STATUS = 'A' )
                                  OR ( :status = 'S'
                                       AND IS2.STATUS = 'S' ) )
                           AND ( :siiFlag = 'ALL'
                                  OR ( :siiFlag = 'SII'
                                       AND I.SII_FLAG = 'Y' ) )
                           AND ( :inventoryCheckFlag = 'ALL'
                                  OR ( :inventoryCheckFlag = 'Y'
                                       AND I.INVENTORY_CHECK_FLAG = 'Y' )
                                  OR ( :inventoryCheckFlag = 'N'
                                       AND I.INVENTORY_CHECK_FLAG = 'N' ) )                            