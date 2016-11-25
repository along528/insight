SELECT surveyid,agency,city,state,
       hits_white / nullif(searches_white,0) AS white_hit_rate, 
       hits_black / nullif(searches_black,0) AS black_hit_rate,
       searches_white / nullif(stops_white,0) AS white_search_rate, 
       searches_black / nullif(stops_black,0) AS black_search_rate
FROM traffic_joined_with_features
WHERE stops_total > 100