from dc_base_scrapers.arcgis_scraper import ArcGisScraper


stations_url = "https://gis.tmbc.gov.uk/arcgis/rest/services/External_Maps/Electors/MapServer/0/query?where=OBJECTID_1+LIKE+%27%25%27&text=&objectIds=&time=&geometry=&geometryType=esriGeometryPoint&inSR=&spatialRel=esriSpatialRelIntersects&relationParam=&outFields=*&returnGeometry=true&maxAllowableOffset=&geometryPrecision=&outSR=4326&returnIdsOnly=false&returnCountOnly=false&orderByFields=PD_LETTER&groupByFieldsForStatistics=&outStatistics=&returnZ=false&returnM=false&gdbVersion=&returnDistinctValues=false&f=pjson"
districts_url = "https://gis.tmbc.gov.uk/arcgis/rest/services/External_Maps/Electors/MapServer/1/query?where=OBJECTID+LIKE+%27%25%27&text=&objectIds=&time=&geometry=&geometryType=esriGeometryEnvelope&inSR=&spatialRel=esriSpatialRelIntersects&relationParam=&outFields=*&returnGeometry=true&maxAllowableOffset=&geometryPrecision=&outSR=4326&returnIdsOnly=false&returnCountOnly=false&orderByFields=PROPOSED_P&groupByFieldsForStatistics=&outStatistics=&returnZ=false&returnM=false&gdbVersion=&returnDistinctValues=false&f=pjson"
council_id = 'E07000115'


stations_scraper = ArcGisScraper(stations_url, council_id, 'utf-8', 'stations', key='OBJECTID_1')
stations_scraper.scrape()
districts_scraper = ArcGisScraper(districts_url, council_id, 'utf-8', 'districts')
districts_scraper.scrape()
