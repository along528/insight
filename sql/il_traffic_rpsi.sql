SELECT year,searches_black/stops_black as black,searches_white/stops_white as white, (searches_black/stops_black)/(searches_white/stops_white) as rpsi FROM il_traffic_stops_split_by_year WHERE agencycode = 13194