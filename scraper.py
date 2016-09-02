from arcgis_scraper import scrape


stations_url = "https://maps.tmbc.gov.uk/arcgis/rest/services/LocalViewPublic/Polling_Stations/MapServer/0/query?where=OBJECTID+LIKE+%27%25%27&text=&objectIds=&time=&geometry=&geometryType=esriGeometryPoint&inSR=&spatialRel=esriSpatialRelIntersects&relationParam=&outFields=*&returnGeometry=true&maxAllowableOffset=&geometryPrecision=&outSR=4326&returnIdsOnly=false&returnCountOnly=false&orderByFields=OBJECTID&groupByFieldsForStatistics=&outStatistics=&returnZ=false&returnM=false&gdbVersion=&returnDistinctValues=false&f=pjson"
districts_url = "https://maps.tmbc.gov.uk/arcgis/rest/services/LocalViewPublic/Polling_Stations/MapServer/1/query?where=OBJECTID+LIKE+%27%25%27&text=&objectIds=&time=&geometry=&geometryType=esriGeometryEnvelope&inSR=&spatialRel=esriSpatialRelIntersects&relationParam=&outFields=*&returnGeometry=true&maxAllowableOffset=&geometryPrecision=&outSR=4326&returnIdsOnly=false&returnCountOnly=false&orderByFields=OBJECTID&groupByFieldsForStatistics=&outStatistics=&returnZ=false&returnM=false&gdbVersion=&returnDistinctValues=false&f=pjson"
council_id = 'E07000115'


scrape(stations_url, council_id, 'utf-8', 'stations')
scrape(districts_url, council_id, 'utf-8', 'districts')
