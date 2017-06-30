# JSON-to-CSV-Converter

Totally Generic JSON to CSV Converter. 
Provide the following details to the `config.ini` file
  1. The CSV file name and the name of the JSON file that is to be converted
  2. The headers that are to be extracted from the JSON file
  
Nested documents within JSON are keyed-in and accessed using `.` operator.

## Example:

```
{
    "_id" : "tag:search.twitter.com,2005:743231670216691716",
    "id" : "tag:search.twitter.com,2005:743231670216691716",
   "actor" : {
        "id" : "id:twitter.com:843880873",
        "languages" : [ 
            "en"
        ],
        "statusesCount" : 6257,
        "twitterTimeZone" : "Amsterdam",
        "followersCount" : 268,
        "location" : {
            "objectType" : "place",
            "displayName" : "Ireland"
        },
        "utcOffset" : "7200",
}
```
Here to access the `twitterTimeZone` we have to use `actor.twitterTimeZone` in the headers key in the config file. All the headers are space seperated. 
