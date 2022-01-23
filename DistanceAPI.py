import xlrd
import sys
from requests import get

API_KEY = "<Your Google Maps API Key>"
CSV_SEPERATOR = ";"
ADD_BEFORE_ROUNDING = 499


def xstr(*strings):
    r = ""
    try:
        for s in strings:
            r += s
    except:
        return ""
    return r


class Address:
    def __init__(self, short_name=None, long_name=None, street=None, number=None, zip=None, city=None, country=None):
        self.short_name = short_name
        self.long_name = long_name
        self.street = street
        self.number = number
        self.zip = zip
        self.city = city
        self.country = country
        self.format = format

    def __str__(self):
        return xstr(self.street) + \
               xstr(" ", self.number) + \
               xstr(", ", self.zip) + \
               xstr(", ", self.city) + \
               xstr(", ", self.country)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise Exception("Invalid number of arguments")

    address_file = sys.argv[1]
    workbook = xlrd.open_workbook(address_file)
    sheet = workbook.sheet_by_index(0)

    address_list = []
    for row in range(sheet.nrows):
        a = {"short_name": sheet.cell_value(row, 0),
             "long_name": sheet.cell_value(row, 1),
             "street": sheet.cell_value(row, 2),
             "number": sheet.cell_value(row, 3),
             "zip": sheet.cell_value(row, 4),
             "city": sheet.cell_value(row, 5),
             "country": sheet.cell_value(row, 6)}
        address_list.append(Address(**a))

    print("\"From / To\"", sep="", end="")
    for a in address_list:
        print(CSV_SEPERATOR, "\"", a.short_name, "\"", sep="", end="")
    print("", sep="")

    for a in address_list:
        origin = str(a)
        print("\"", a.short_name, "\"", sep="", end="")
        for b in address_list:
            if not a is b:
                destination = str(b)
                url = "https://maps.googleapis.com/maps/api/distancematrix/json?origins=" + origin +\
                      "&destinations=" + destination + "&key=" + API_KEY
                response = get(url)
                if response.status_code != 200:
                    raise Exception("Error when accessing Google Maps API")
                data = response.json()
                distance = round((data["rows"][0]["elements"][0]["distance"]["value"] + ADD_BEFORE_ROUNDING) / 1000)
                print(CSV_SEPERATOR, distance, sep="", end="")
            else:
                print(CSV_SEPERATOR, 0, sep="", end="")
        print("")
