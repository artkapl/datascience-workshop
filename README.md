# datascience-workshop

## Small internal datascience workshop

We use this workshop to learn about data science using real-life examples.  
We use Python as our main programming language for this purpose.  

### Mindmap

![mindmap](https://github.com/OreoCassowary/datascience-workshop/blob/master/datascience-workshop-Mind-Map.jpg "Mindmap to structure our project")  
Link to mindmap: (https://bubbl.us/010902974515863474)  

### Tools

[Github](https://github.com/) allows us to collaborate on projects.  
[Getting started guide](https://guides.github.com/activities/hello-world/)  

Data sets:
- [Worldbank data](data.worldbank.org)
- [Data sets for data science](https://www.dataquest.io/blog/free-datasets-for-projects/)
- [Berkeley Earth](http://berkeleyearth.org/data/) - Global temperature data
- [Open Refine](http://openrefine.org/) - edit/cleanup data sets
- [Plotly](https://plot.ly) - Plot/visualize data


### Basic programming techniques

CSV 
- [ETL](https://en.wikipedia.org/wiki/Extract,_transform,_load) - extract, transform, load

### Libraries

[csv](https://docs.python.org/3/library/csv.html)  

### Documentation

Here is how to write easy documentation in [Markdown](https://daringfireball.net/projects/markdown).  
We use markdown editor [SDingus](https://daringfireball.net/projects/markdown/dingus) and markdown converter [pandoc](http://pandoc.org/).  

### Debugging


### Books and references

- Jacobs, J., & Rudis, B. (2014). *Data-Driven Security: Analysis, Visualization and Dashboards*. John Wiley & Sons.

### To-Do List

(For beginners)  
Read about:
- [ ] string formatting in Python 3 - [String operations](https://docs.python.org/3.3/library/string.html)
- [ ] Theory behind IP adresses, [ASN](https://en.wikipedia.org/wiki/Autonomous_System_Number) (autonomous system number), Traceroute, announcing IP adresses
- [ ] [Unix time](https://en.wikipedia.org/wiki/Unix_time): date format "epoch" --> seconds from Jan 1, 1970. A common time stamp format in IT.

## Homework 

(Check pull request for data set)  
Data has timestamp, IP, ASN, country

- count facets (= nominal data, e.g. sex, eye color) of selected columns in data & print them
- Descriptive stat for rows in csv - mean, median, std dev & print
Hint: look at dicts, sets and lists

### Typical mistakes

Reading a file with csv.reader returns strings - need to cast as int  
"Off by one" -> index starts at 1 in csv
