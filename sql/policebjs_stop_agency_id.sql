SELECT s."SURVEYID",s.agency,s.city,count(s."SURVEYID") FROM police_data_table s
WHERE s.state='NC'
GROUP BY s.agency,s.city,s."SURVEYID";
