# Keeping Count of the Journalists Killed in Palestine

The [assassination of Anas Al-Sharif on August 10, 2025](https://apnews.com/article/mideast-wars-gaza-journalist-jazeera-c7d73f1d3cfa3d24fb4ce5a294c08d32) brought the plight of journalists in Palestine to my attention.

I wanted to find reliable data to create a chart about the issue. But the United Nations does not a provide detailed data of [the 242 journalists](https://palestine.un.org/en/299624-guterres-urges-probe-killing-journalists-child-malnutrition-deaths-rise?utm_source=chatgpt.com) they say have been killed in Gaza. And the [Committee to Protect Journalists](https://cpj.org/data/killed/2025/?status=Killed&motiveConfirmed%5B%5D=Confirmed&type%5B%5D=Journalist&cc_fips%5B%5D=IS&start_year=2023&end_year=2025&group_by=location) provided what I thought was a significant undercount of 170 names.

So I used Wikipedia, copying and pasting from [a table they maintained](https://en.wikipedia.org/wiki/List_of_journalists_killed_in_the_Gaza_war#Palestine) into a CSV file. I then used a python script to create another CSV file with the number of journalists killed each month from October 2023 through August 2025, the month when I decided to create this chart.

I took the monthly totals and put them into [a Google Sheet](https://docs.google.com/spreadsheets/d/11njVes18TC83KHEzsO90ZC3mJ5gTbGEAKsZoLyLPryE/edit?usp=sharing), which I then connected to Datawrapper. The result is this chart, which [you can interact with here](https://www.datawrapper.de/_/3l4Sl/), and view below:

![Datawrapper chart](./img/datawrapper_chart.png?raw=true "Title")
