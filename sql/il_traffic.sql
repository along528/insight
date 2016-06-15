SELECT agencycode,agencyname,count(agencycode) AS stops,
SUM(CASE WHEN "searchconducted" = 'Yes' THEN 1 ELSE 0 END) as searches,
SUM(CASE WHEN "contrabandfound" = 'Yes' THEN 1 ELSE 0 END) as hits,
year 
FROM traffic_stops_2004
WHERE race = 'white'
GROUP BY agencycode,agencyname,year