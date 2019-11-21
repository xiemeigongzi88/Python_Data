# Which provinces and cities of our country did Typhoons often land in?

  Dataset: http://www.stwc.icoc.cc/h-col-205.html

## Target: 
	Collecting all the typhoon data that made landfall in China from 1945 to 2015, and made visual analysis of these data through Python, which turns to get some interesting conclusions. 

## Main Tools:
Google Cloud, Pandas, Numpy, Matplotlib, Seaborn, requests, Beautiful Soup, Geopandas, WordCloud

## Steps:
	Web crawler obtains the table of all typhoon data. 
	Data Cleansing: there is only land in address in the data set, and there is no exact longitude and latitude information. In this case, we need to obtain the longitude and latitude through geocoding, using google map API through Google Cloud. After the landing longitude and latitude information is obtained, the provincial, municipal, district and county level information is obtained through geographic inverse coding. Using Geopandas to place typhoon landing sites on maps, using latitude and longitude data,
	Data visualization: land in province distribution; land in city distribution; what  the typhoon degree that landed in each province was; the number of land-in typhoons varied every year from 1945 to 2015; Heatmap of the typhoon intensity changes every month and so on. 
