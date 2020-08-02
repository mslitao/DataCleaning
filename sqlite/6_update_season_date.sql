UPDATE Farmers_Market_Data
SET Season1StartDate=Season1EndDate, Season1EndDate=Season1StartDate
WHERE FMID IN
  (SELECT FMID
    FROM Farmers_Market_Data
    WHERE Season1StartDate>Season1EndDate
    AND Season1EndDate!="")
