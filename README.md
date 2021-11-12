## Recent trends in gender issues in a global context : seeking for contrasted opinions

### Abstract

Gender norms are social principles that govern the behavior of all of us in society and restrict our gender identity into what is considered to be appropriate. These are neither static nor universal and change over time, and can result in inequalities. 

More and more countries have recently legalized and recognized same-sex marriage, sometimes following long legal procedures. In Switzerland, this law was introduced in 2013, passed in 2020 by the parliament and adopted by referendum in September 2021.
The feminism topic also indicates real changes in society. LGBT+ issues are also extremely present in public life, with emerging pride movements and pure gender questioning.

We will focus on observing changes in the speakers’ opinion on the topics of gender equality and same-sex relations, depending on their nationality, age, as well as possibly occupation, and quote date. It is also of interest to compare opinions within countries before and after national events, such as same-sex marriage legalization.



### Research Questions:

- How legalization of same-sex marriage influenced the opinion of the authors of the quotes?
- Which countries' opinions significantly contrast with others ?
- Does the author's age significantly lead to different trends, i.e. does the youngest authors generally have broader gender norms 
- Do our sentiment analysis of gender equality opinion per country matches with related indexes (European Institute for Gender Equality https://eige.europa.eu/gender-equality-index/2021 or United Nations Development Program - Human Development Report - Gender Inequality Index http://hdr.undp.org/en/content/gender-inequality-index-gii for example) ?


### Additional datasets

We do not plan to use any additional datasets than the one provided for the outlook of this project.
The Wikidata was however used to have access to the speaker's attributes such as their nationality, gender, or age.


### Methods

1) Loading & Preprocessing data from Quotebank : 'Quotes.ipynb'

First of all, in order to handle the heavy and memory-consuming dataset Quotebank, we had to do some data pre-processing steps.
The final goal of this first crucial step was to have a clean and specific dataset for our research study. Concretely, it means filtering the quotes to retain only those that interest our topic on gender norms. Below is the method we used :

- The dataset is large, so we had to divide it into parts/chunks. 
- From those parts, we took only quotes that contain keywords concerning our topics. You can find the bank of keywords we used for filtering (and its source) the Quotebank dataset in the file (Quotes.ipynb).
- Then, in order to adress our research questions, we needed speakers' features: nationality, date of birth, gender and occupation. We could get them from the WikiData. Initial WikiData contains IDs that have to be mapped with labels.   
- We finally joined quotes and information about speakers into a final json file on which we can perform our analysis.

Our final dataset contains  features and 209'000 quotes.


2) Initial analysis / Exploratory data analysis : 'InitialAnalysis.ipynb'

Firstly, we decided to check if research questions were feasible.
If the interest in gender-related topics hasn't noticeably changed for these years, it will be complicated to find enhancements.


3) Sentiment analysis : Analysis of quotes


4) Observational study : 

### Proposed timeline

1) Based on our dataset observations, correct it - Goal : by ../..

We saw a lot of "nearly duplicates", below is an example :
- "What is worse than violence? Violence sanctioned by misogyny."
- "violence that is sanctioned by misogyny"

So far, our restrictions on duplicates have not allowed to solve this issue.

We also face a language issue. The word "gay" (for example) is included in many quotes that are not relevant here, like :
"Desh bhakti ko bhi kosa jaata ho, aisa mahaul ban **gaya** hai, (there is an atmosphere in the country where even gestures of nationalism and patriotism are abused)"

2) Compute the interest figures we are interested in - Goal : by ../..

...

3) Make the interactive maps we are interested in - Goal : by ../..

...

4) Build the website - Goal : by ../..

### Organization within the team: A list of internal milestones up until project Milestone 3.

...

### Questions for TAs (optional): Add here any questions you have for us related to the proposed project.

...
