SELECT s.agency_id,s.agency_description,count(s.agency_id) FROM nc_stop s
GROUP BY s.agency_id,s.agency_description
ORDER BY s.agency_id