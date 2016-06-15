SELECT traffic.*, census.*,survey.*
FROM combined_traffic_stops_integrate_year_surveyid traffic
JOIN census_population_sum census ON traffic.surveyid = census.surveyid
JOIN police_surveys survey ON census.surveyid = survey.surveyid