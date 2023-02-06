project('Website', 'Red', 'Paris').                    
project('Computer', 'Green', 'London').                      
project('CPU', 'Yellow', 'Paris').
project('Console', 'Blue', 'Berlin').

find_project(Location, Projects) :- 
    findall(Project, project(Project,_,Location), Projects).
Sample call:

| ?- find_project('Paris', Projects).

Projects = ['Website', 'CPU']
yes
