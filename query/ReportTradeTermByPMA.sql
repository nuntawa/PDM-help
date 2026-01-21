-- searchCategoryReportTradeTermByPMAList
SELECT DISTINCT
					       t.PMA_CATEGORY_CODE,
					       c.PMA_CATEGORY_NAME
					FROM WKSP_WSPDMDEV.TRADE_TERM_PMA t
					JOIN WKSP_WSPDMDEV.PMA_CATEGORY c
					  ON c.PMA_CATEGORY_CODE = t.PMA_CATEGORY_CODE
					WHERE t.PMA_CODE = :pmaCode
                      AND t.DELIVERY_TYPE_CODE = :deliveryTypeCode

 --searchWarehouseReportTradeTermByPMAList
 SELECT DISTINCT
					       t.WAREHOUSE_ID,
					       v.SHIP_TO_NAME AS WEARHOUSE_NAME
					FROM WKSP_WSPDMDEV.TRADE_TERM_PMA t
					JOIN STORE_VENDOR_USR.VENDOR v
					  ON v.VENDOR_ID || '-' || v.VENDOR_SUB_ID = t.WAREHOUSE_ID
					WHERE t.PMA_CODE = :pmaCode
					  AND t.DELIVERY_TYPE_CODE = :deliveryTypeCode 

--searchCostGroupReportTradeTermByPMAList
  SELECT DISTINCT
                        t.CTRL_COST_GRP_CODE,
                    	t.DELIVERY_TYPE_CODE,
                    	c.CTRL_COST_GRP_NAME
                    FROM
                    	WKSP_WSPDMDEV.TRADE_TERM_PMA t
                    JOIN WKSP_WSPDMDEV.CTRL_COST_GRP c
                                          ON
                    	c.CTRL_COST_GRP_CODE = t.CTRL_COST_GRP_CODE
                    AND :lastSaturday BETWEEN c.EFFECTIVE_START_DATE AND c.EFFECTIVE_END_DATE
                    WHERE
                    	t.PMA_CODE = :pmaCode
                    AND t.DELIVERY_TYPE_CODE = :deliveryTypeCode

