## Recent trends in gender issues in a global context : seeking for contrasted opinions

### Abstract

Gender norms are social principles that govern the behavior of all of us in society and restrict our gender identity into what is considered to be appropriate. These are neither static nor universal and change over time, and can result in inequalities. 

More and more countries have recently legalized and recognized same-sex marriage, sometimes following long legal procedures. In Switzerland, this law was introduced in 2013, passed in 2020 by the parliament and adopted by referendum in September 2021.
The feminism topic also indicates real changes in society. LGBT+ issues are also extremely present in public life, with emerging pride movements and pure gender questioning.

We will focus on observing changes in the speakers’ opinion on the topics of gender equality and same-sex relations, depending on their nationality, age, as well as possibly occupation, and quote date. It is also of interest to compare opinions within countries before and after national events, such as same-sex marriage legalization.



### Research Questions:

- How legalization of same-sex marriage influenced the opinion of the authors of the quotes?
- Which countries' opinions significantly contrast with others ?
- Does the author's age significantly lead to different trends, i.e. does the youngest authors generally have broader gender norms - Do our sentiment analysis of gender equality opinion per country matches with related indexes (European Institute for Gender Equality https://eige.europa.eu/gender-equality-index/2021 or United Nations Development Program - Human Development Report - Gender Inequality Index http://hdr.undp.org/en/content/gender-inequality-index-gii for example) ?


### Additional datasets

We do not plan to use any additional datasets than the one provided for the outlook of this project.
The Wikidata was however used to have access to the speaker's attributes such as their nationality, gender, or age.


### Methods

1) Data preparation (DONE)

First of all, in order to handle the dataset which is really heavy, we had to do some data pre-processing steps.

The dataset is large, so we had to divide it into parts. 
To limit its size, we took only quotes that contain keywords concerning our topics. 
We added speakers' features: nationality, date of birth, gender etc to the dataset from WikiData. 
Initial WikiData contains IDs that have to be mapped with labels.   
Finally, we got the dataset aggregating quotes and information about speakers. 
This dataset contains % features and % samples.

Looking through the dataset we found NaN values, which we removed or filled by correct values. 
Missing quotes or authors have to be removed. 
Wikidata missing values can be processed with WikiData API.  
The result contains ..... samples. It means that the analysis can proceed with a sufficient sample. 

2) Initial analysis (DONE)

Firstly, we decided to check if research questions are feasible. 
If the interest in gender-related topics hasn't noticeably changed for these years, it will be complicated to find enhancements. 
We looked at the frequency of gender-related topics mentioned in quotes depending on the year.   

After that, we checked which words were the most frequent quotes containing keywords depending on the year.

Finally, we plotted the distribution of the most frequent words by year and their word cloud.  

### Proposed timeline


### Organization within the team: A list of internal milestones up until project Milestone 3.

### Questions for TAs (optional): Add here any questions you have for us related to the proposed project.

...
