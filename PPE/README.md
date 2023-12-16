PPE Project Workup

Link for Google Forms where users will input supplies based on date
https://docs.google.com/forms/d/e/1FAIpQLSeQx7_eBEn1f_WGSCtWhvprcfF37wvhGl_Ek9gUXlNjs-axeg/viewform?usp=sf_link

![Google Forms](https://github.com/rshaikh95/PPE_PROJ/assets/141374132/1190e25d-1cff-465c-af73-741272074280)

Using App Script webhook form input will be added to flask app using input from Google Forms sent to hospital staff (See googleappsscript file)

![Apps Script Code Screenshot](https://github.com/rshaikh95/PPE_PROJ/assets/141374132/cd9349f6-09c2-44b6-9551-a4df71bf352f)

Airtable base creation via Airtable.com, Excel sheet converted into Airtable Base
https://airtable.com/appOcV2IR3hAH3YCd/shrtoWaduR8QSOYOC

![Base for Airtable](https://github.com/rshaikh95/PPE_PROJ/assets/141374132/67be0584-9fc4-4660-91dd-cdc96e098b72)

Airtable API (pip install pyairtable) will be added to flask app (https://hevodata.com/learn/airtable-python/) 

Responses will be populated to Airtable Base from flask app 

The base on airtable API will calculate burn and usage rate using formulas function 

![Formula Calculations](https://github.com/rshaikh95/PPE_PROJ/assets/141374132/126b9721-a587-4ba1-b169-f52364a71a9a)

The calculated values will then be shown flask app via report that can be downloaded or emailed back to staff for use. Airtable API for email use.

upload flask app to azure for public access

