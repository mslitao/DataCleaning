UPDATE Farmers_Market_Data
SET OtherMedia = ""
  WHERE FMID IN
  (SELECT FMID
    FROM Farmers_Market_Data
    WHERE Website=OtherMedia AND OtherMedia!="");

UPDATE Farmers_Market_Data
SET OtherMedia = ""
  WHERE FMID IN
  (SELECT FMID
    FROM Farmers_Market_Data
    WHERE Facebook=OtherMedia AND OtherMedia!="");

UPDATE Farmers_Market_Data
SET OtherMedia = ""
  WHERE FMID IN
  (SELECT FMID
    FROM Farmers_Market_Data
    WHERE Twitter=OtherMedia AND OtherMedia!="");

UPDATE Farmers_Market_Data
SET OtherMedia = ""
  WHERE FMID IN
  (SELECT FMID
    FROM Farmers_Market_Data
    WHERE Youtube=OtherMedia AND OtherMedia!="");
