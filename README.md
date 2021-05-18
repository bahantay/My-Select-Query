# My-Select-Query
Remember to git add && git commit && git push each exercise!

We will execute your function with our test(s), please DO NOT PROVIDE ANY TEST(S) in your file

For each exercise, you will have to create a folder and in this folder, you will have additional files that contain your work. Folder names are provided at the beginning of each exercise under submit directory and specific file names for each exercise are also provided at the beginning of each exercise under submit file(s).

My Select Query	
Submit directory	ex00
Submit file	my_select_query*
Languages	javascript => .js, python => .py, ruby => .rb, c => .c, ...
Description
Create a class MySelectQuery.
Your constructor will receive a CSV content (as a string), first line will be the name of the column.

Example:

"name,year_start,year_end,position,height,weight,birth_date,college\nAlaa Abdelnaby,1991,1995,F-C,6-10,240,'June 24, 1968',Duke University\nZaid Abdul-Aziz,1969,1978,C-F,6-9,235,'April 7, 1946',Iowa State University\nKareem Abdul-Jabbar,1970,1989,C,7-2,225,'April 16, 1947','University of California, Los Angeles
Mahmoud Abdul-Rauf,1991,2001,G,6-1,162,'March 9, 1969',Louisiana State University\n"
It will be prototyped:

constructor(csv_content)

Implement a where method which will take 2 arguments: column_name and value.
It will return an array of strings which matches the value.

It will be prototyped:

where(column_name, criteria)

Our examples will use these CSV
Nba Player Data
Nba Players
Nba Seasons Stats

Example00

Input: "name" && "Andre Brown"
Output: [{"name" => "Andre Brown", "year_start" => "2007", "year_end" => "2009", "position" => "F", "height" => "6-9", "weight" => "245", "birth_date" => "May 12, 1981", "college" => "DePaul University"}]
