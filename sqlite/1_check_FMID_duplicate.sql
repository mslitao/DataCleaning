SELECT FMID
  FROM Farmers_Market_Data
  GROUP BY FMID
  HAVING COUNT(FMID)>1;

