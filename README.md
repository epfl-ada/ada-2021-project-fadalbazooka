## Recent trends in gender issues in a global context : seeking for contrasted opinions

## 1. Abstract

Gender norms are social principles that govern the behavior of all of us in society and restrict our gender identity into what is considered to be appropriate. These are neither static nor universal and change over time, and can result in inequalities. 

More and more countries have recently legalized and recognized same-sex marriage, sometimes following long legal procedures. In Switzerland, this law was introduced in 2013, passed in 2020 by the parliament and adopted by referendum in September 2021.
The feminism topic also indicates real changes in society. LGBT+ issues are also extremely present in public life, with emerging pride movements and pure gender questioning.

We will focus on observing changes in the speakers’ opinion on the topics of gender equality and same-sex relations, depending on their nationality, age, as well as possibly occupation, and quote date. It is also of interest to compare opinions within countries before and after national events, such as same-sex marriage legalization.

## 2. Research Questions:

- How legalization of same-sex marriage influenced the opinion of the authors of the quotes?
- Which countries' opinions significantly contrast with others ?
- Does the author's age significantly lead to different trends, i.e. does the youngest authors generally have broader gender norms 
- Do our sentiment analysis of gender equality opinion per country matches with related indexes (European Institute for Gender Equality https://eige.europa.eu/gender-equality-index/2021 or United Nations Development Program - Human Development Report - Gender Inequality Index http://hdr.undp.org/en/content/gender-inequality-index-gii for example) ?

## 3. Additional datasets

We do not plan to use any additional datasets than the one provided for the outlook of this project.
The Wikidata was however used to have access to the speaker's attributes such as their nationality, gender, age and occupation.

## 4. Methods

1) Loading & Preprocessing data from Quotebank: 'DataLoading.ipynb'

First of all, in order to handle the heavy and memory-consuming dataset Quotebank, we had to do some data pre-processing steps.
The final goal of this first crucial step was to have a clean and specific dataset for our research study. Concretely, it means filtering the quotes to retain only those that interest our topic on gender norms. Below is the method we used :

- The dataset is large, so we had to divide it into parts/chunks. 
- From those parts, we took only quotes that contain keywords concerning our topics. You can find the bank of keywords we used for filtering (and its source) the Quotebank dataset in the file (Quotes.ipynb).
- Then, in order to address our research questions, we needed speakers' features: nationality, date of birth, gender and occupation. We could get them from the WikiData. Initial WikiData contains IDs that have to be mapped with labels.   
- We finally joined quotes and information about speakers into a final json file on which we can perform our analysis.

Our final dataset contains 9 features and 209'000 quotes to analyse.

2) Initial analysis / Exploratory data analysis: 'InitialAnalysis.ipynb'

Firstly, we decided to check if research questions were feasible. Indeed, if the interest in gender-related topics haven't noticeably changed in these years, it will be complicated to find enhancements. We therefore plotted many variables such as the distribution of quotes per year or the most used words in our key-words database, in order to fully understand the data and be able to establish a strategy for the data analysis.

3) Sentiment analysis: Analysis of quotes

We started the sentiment analysis by seeking for libraries that have such functions. We compared the 2 most popular we found in "NLP_testing.ipynb" and concluded we will use the NLTK library in this study.

It will allow us to give an appreciation score to the quotes we selected for this study, and to further analyze them in the next parts of the project.

4) Observational study: Looking for trends

We are going to make an observational study thanks to the sentimental analysis that we will have made beforehand. Thanks to the sentimental scores, we will be able to establish people's positions concerning the topic we chose according to the countries, the ages as well as the political positions.

5) Data visualization: Showing the data story

On the website, we are going to create, we are going to work on the types of curves that will allow us to express our results in a clear way.

## 5. Proposed timeline

1) Based on our dataset observations, correct it - Goal: by 03/12

2) Compute the sentiment analysis and assess the validity of our data - Goal: by 03/10

At the end of the this phase, we should :

3) Compute the figures we are interested in and answer our research questions - Goal: by 10/12

4) Make the interactive maps we are interested in - Goal: by 17/12

5) Build the website and make the data story - Goal: by 17/12

### 6. Organization within the team

Below is how we plan to divide the task for the 3 weeks in between Homework 2 due date and Project Milestone 3 due date :

- Week 1 : Arina will work on solving the data issues we so far detected (duplicates and languages). Benoit will work on computing the analysis which are linked to the validity of our data and to distribution on author-related features. William will compute the sentiment analysis on the data sample. Nicolas will compute statistics on these sentiment scores to assess their distribution. While names are assigned to these tasks, the whole team will combine its forces in the common goal.
- Week 2 : The whole team will work on answering the research questions statistically based on the data (combined from Quotebank and Wikidata, with the related sentiment analysis) to seek for interesting trends.
- Week 3 : The whole team will contribute to the website creation, to the data story writing and to integrating the interactive visualization to it.

