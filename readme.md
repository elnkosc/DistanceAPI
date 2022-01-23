Generate Distance Matrix between addresses.

This program requires a valid API for the Google Maps Distance Matrix API (see https://developers.google.com/maps).

As input to this program an Excel file in 95 format (.xls extension) is needed. It is a simple sheet containing the the following columns (note, all need to be in 'text-format'):

* Abbreviation of location
* Full name of location
* Streetname
* Housenumber plus extension
* Zip-code
* Place
* Country

An example file is included as part of this repository. This program generated .csv output to stdout. You should redirect this to a file with .csv extension. MS Excel can be used to read the matrix file and further process it.

~~~~
usage: DistanceAPI.py filename

arguments:
  filename              file to be used as input
  
output:
  csv-data to standard output in a format MS Excel can import. Redirect stdout to a file to import it into MS Excel.
~~~~

Example input:

|     |                        |                         |     |         |           |                 |
|-----|------------------------|-------------------------|-----|---------|-----------|-----------------|
| AMS | Royal Palace Amsterdam | Nieuwezijds Voorburgwal | 147 | 1012 RJ | Amsterdam | The Netherlands |
| EIF | Eiffel Tower           | Av. Anatole France      | 5   | 75007   | Paris     | France          |
| COL | Colosseum              | Piazza del Colosseo     | 1   | 00184   | Rome      | Italy           |

Result (on stdout):

"From / To";"AMS";"EIF";"COL"<br>
"AMS";0;514;1660<br>
"EIF";511;0;1408<br>
"COL";1663;1434;0

Result (when imported in MS Excel):

| From / To | AMS  | EIF  | COL  |
|-----------|------|------|------|
| AMS       | 0    | 514  | 1660 |
| EIF       | 511  | 0    | 1408 |
| COL       | 1663 | 1434 | 0    |

Want to stimulate the ongoing development? Your BTCs are welcome! Send them to bitcoin:15pqCjD7pPPraGJ8T4yfbkrtFTBX8M4jyw
