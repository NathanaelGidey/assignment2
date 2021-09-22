
dataset_list = [{'url': "https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2018/2018-06-12/week11_fifa_audience.csv" , # a dataset with nonnumerical data in at least one column
     'name': "Fifa Attendance",
     'load_func': "read_csv" },
     {'url': "https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2019/2019-04-30/bird_call.csv", #any dataset you're interested in
     'name': "Species",
     'load_func': "read_csv"},
     {'url': "https://www.govtrack.us/api/v2/role?current=true&role_type=senator", #any dataset you're interested in
     'name': "Music",
     'load_func': "read_tsv"}]
