.mode column
SELECT "Website  == Othermedia cases ", COUNT(OtherMedia)
  FROM Farmers_Market_Data
  WHERE Website = OtherMedia AND OtherMedia!="";
SELECT "Facebook == Othermedia cases ", COUNT(OtherMedia)
  FROM Farmers_Market_Data
  WHERE Facebook = OtherMedia AND OtherMedia!="";
SELECT "Twitter  == Othermedia cases ", COUNT(OtherMedia)
  FROM Farmers_Market_Data
  WHERE Twitter = OtherMedia AND OtherMedia!="";
SELECT "Youtube  == Othermedia cases ", COUNT(OtherMedia)
  FROM Farmers_Market_Data
  WHERE Youtube = OtherMedia AND OtherMedia!="";
