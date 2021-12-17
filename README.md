### Repository content

- ```1_datasets```: the .json and .pkl files we used to filter *Quotebank* data and further analyze it to aswer our questions.
- ```2_initial_analysis```: the notebooks we used to import and filter the original datasets, and to further understand its main features.
- ```3_sentiment_analysis```: the notebooks were we tested differend NLP (Natural Language Processing) libraries onto our datasets, and where we computed the sentiment score for each quote.
- ```4_stance_analysis```: the files and notebooks were we run stance analysis on our datasets, to compare author's opinions.
- ```5_ML_predictions```: the files required to perform the prediction of nationalities based on quotes, containing :
     - ```GPT2```: the files were GPT2 (Generative Pre-trained Transformer 2) open-source artificial intelligence was used (based on deep neural networks), 
     - ```LSTM```: the files where LSTM (Long Short-Term Memory) artificial intelligence model was used (based on a recurrent neural network architecture).
- ```6_research_questions```: the files where we analyzed our data to answer the 4 research questions we originally detailed.
- ```7_interactive_plots```: the notebooks we used to generate interactive plots for the website.

# Recent trends in gender issues in a global context : seeking for contrasted opinions

## 1. Abstract

Gender norms are social principles that govern the behavior of all of us in society and restrict our gender identity into what is considered to be appropriate. These are neither static nor universal and change over time, and can result in inequalities. 

More and more countries have recently legalized and recognized same-sex marriage, sometimes following long legal procedures. In Switzerland, this law was introduced in 2013, passed in 2020 by the parliament and adopted by referendum in September 2021.
The feminism topic also indicates real changes in society. LGBT+ issues are also extremely present in public life, with emerging pride movements and pure gender questioning.

We focused on observing changes in the speakers’ opinion on the topics of gender equality and same-sex relations, depending on their nationality and age. 
We also compared opinions within countries before and after national events, such as same-sex marriage legalization.
We tried to model the effect of such variables, in order to assess their correlation with author's opinion.
Finally, we tried to determine a model, based on quotes, which could predict an author's nationality based from it.

Our website can be consulted on: https://benoitdelec.github.io/FadalBazooka.github.io/

It was built with the repository: https://github.com/BenoitDelec/FadalBazooka.github.io

## 2. Research Questions:

- How legalization of same-sex marriage influenced the opinion of the authors of the quotes?
- Which countries' opinions significantly contrast with others ?
- Does the author's age significantly lead to different trends, i.e. does the youngest authors generally have broader gender norms 
- Do our sentiment analysis of gender equality opinion per country matches with related indexes (European Institute for Gender Equality https://eige.europa.eu/gender-equality-index/2021 or United Nations Development Program - Human Development Report - Gender Inequality Index http://hdr.undp.org/en/content/gender-inequality-index-gii for example) ?

## 3. Additional datasets

We did not use any additional datasets than the one provided for the outlook of this project.
The Wikidata was however used to have access to the speaker's attributes such as their nationality, gender, age and occupation.
The external libraires we used contained pre-trained models, so we did not need to use additional datasets.

## 4. Methods

**1) Loading & Preprocessing data from Quotebank**

First of all, in order to handle the heavy and memory-consuming dataset Quotebank, we had to do some data pre-processing steps, in ```2_initial_analysis/DataLoading.ipynb```.
The final goal of this first crucial step was to have a clean and specific dataset for our research study.
It consisted of filtering quotes to retain only those that interest our topic on gender norms. 

Below is the method we used :
- Given the dataset was large, we had to divide it into parts/chunks for preprocessing. 
- From those parts, we took only quotes that contain keywords concerning our topics.
- Then, in order to address our research questions, we needed speakers' features: nationality, date of birth, gender and occupation. We could get them from the WikiData. Initial WikiData contains IDs that had to be mapped with labels.   
- We finally joined quotes and information about speakers from WikiData into a final json file : ```1_datasets/filtered.json``` that we analyzed.

**2) Initial analysis / Exploratory data analysis: 'InitialAnalysis.ipynb'**

The main features of the preprocessed and cleaned dataset can be found on the file of the same name : ```2_initial_analysis/Initial_analysis_clean_data.ipynb```, which analyzes data in 
Firstly, we decided to check if research questions were feasible. 
Indeed, if the interest in gender-related topics haven't noticeably changed in these years, it will be complicated to find interesting insights. 
We therefore plotted many variables such as the distribution of quotes per year or the most used words in our key-words database, in order to fully understand the data and to be able to establish a strategy for its analysis.
NLP techniques, including some from the NLTK library, such as Text Tokenization, Text Lemmatization, and Identification of Stop Words, were used in this purpose.

**3) Sentiment analysis: Analysis of quotes**

We started the sentiment analysis by seeking for libraries that have such functions. We compared the ones we found in ```3_sentiment_analysis/NLP tests``` and concluded we will use the *NLTK* library in this study (rather than *spaCy* or *roBERTa*).
It allowed us to give an appreciation score to the quotes we selected for this study, and to further analyze them in the next parts of the project.
We performed this analysis on our quotes, and expanded our intial dataset into ```/1_datasets/added_sentiment.pkl``` (where the *.pkl* format is simply a *pandas.dataframe* storing option).

**4) Observational study: Looking for trends**

We are going to make an observational study thanks to the sentimental analysis that we will have made beforehand. Thanks to the sentimental scores, we will be able to establish people's positions concerning the topic we chose according to the countries, the ages as well as the political positions. Most of our research questions will be answered in this phase. 

**5) Data visualization: Showing the data story**

On the website, we are going to create, we are going to work on the types of curves that will allow us to express our results in a clear way.

## 5. Organization within the team

Below is how we divided tasks between team members :

- Arina preprocessed the data, combined it with Wikidata, made the initial analysis, run the ML predictive models, made interactive plots and contributed to the data story.
- Benoit contributed to the initial analysis, run the sentiment analysis on our datasets, answered research questions, and set-up the website while contributing to the data story.
- Nicolas contributed to the initial analysis, run the stance analysis on our datasets, answered research questions and contributed to the data story.
- William contributed to the initial analysis, compared the sentiment analysis models, answered research questions and developped the data story while contributing to the website creation.
