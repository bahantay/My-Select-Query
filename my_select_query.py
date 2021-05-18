import csv
from io import StringIO

class MySelectQuery:
    reader = csv.reader('')
    f_dict = {}
    f_list = []

    def __init__ (self, param_1):
        csv_file = StringIO(param_1)
        self.reader = csv.reader(csv_file)
        self.f_list = next(self.reader)
        self.f_dict = {i:self.f_list[i] for i in range (len(self.f_list))}

    def where(self, column_name, criteria):
        for key, value in self.f_dict.items():
            if value == column_name:
                index_selected = key
        for row in self.reader:
            if row[index_selected] == criteria:
                answer_list = []
                answer_string = ",".join(row)
                answer_list.append(answer_string)
                return answer_list




# param_1 = "name,year_start,year_end,position,height,weight,birth_date,college\nAlaa Abdelnaby,1991,1995,F-C,6-10,240,'June 24 1968',Duke University\nZaid Abdul-Aziz,1969,1978,C-F,6-9,235,'April 7 1946',Iowa State University\nKareem Abdul-Jabbar,1970,1989,C,7-2,225,'April 16 1947','University of California, Los Angeles\nMahmoud Abdul-Rauf,1991,2001,G,6-1,162,'March 9 1969',Louisiana State University"
# column_name = "name"
# criteria = "Alaa Abdelnaby"
# obj = MySelectQuery(param_1)
# print(obj.where(column_name,criteria))

# Input: "name" && "Abdelnaby"
# Output: [["Alaa Abdelnaby,1991,1995,F-C,6-10,240,'June 24 1968',Duke University"]]
