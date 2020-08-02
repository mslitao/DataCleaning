.mode column
SELECT FMID, Season1StartDate, Season1EndDate
  FROM Farmers_Market_Data
  WHERE Season1StartDate>Season1EndDate
  AND Season1EndDate!=""
