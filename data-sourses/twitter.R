# gather data from twitter

library("selectr")
library("rvest")
library("xml2")
library(rtweet)
library(twitteR)
library(ROAuth)
library(jsonlite)

## My Twitter Dev APIs
consumerKey=as.character('27ABsemCQV0ma3NEOD6OpPLCh')
consumerSecret=as.character('md1etoLaJmeAZBrstaojla2eUvUxH12eH5IRtqB0R38ETnUz6k')
access_Token=as.character('1423271293097582595-7B60uKGYwIBXIawZvBkLFEd8AXicdj')
access_Secret=as.character('YLNAiXvQMyP0CjVgjY5qHyi3kgL8StAMIUm3tXr4Ax12n')

requestURL='https://api.twitter.com/oauth/request_token'
accessURL='https://api.twitter.com/oauth/access_token'
authURL='https://api.twitter.com/oauth/authorize'

setup_twitter_oauth(consumerKey,consumerSecret,access_Token,access_Secret)

# keywords
terms = c('stock', 'DJIA', '^GSPC', 'SP500', 'S&P 500', 'AT&T', 'ATT', 'Ford Motor','AAPL', 'Apple', 'MSFT', 'Microsoft', 'NIO', 'BAC', 'INTC', 'VZ', 'TMUS', 'PFE', 'TSLA', 
          'Bank of America', 'Intel', 'Verizon', 'T-Mobile', 'Pfizer', 'Tesla', 'GOOG', 'AMZN', 'UBER', 'CSCO', 'BABA', 'FB', 'JPM', 'TWTR', 'KO', 'PYPL', 'GS', 'MRNA', 
          'NFLX', 'ZM', 'Google', 'Amazon', 'Uber', 'Costco', 'Alibaba', 'Citi', 'Facebook', 'Meta', 'JPMorgan', 'Twitter', 'Coca-Cola', 'Paypal', 'Goldman Sachs', 
          'Moderna', 'Netflix', 'Zoom')
terms = paste(terms, collapse = " OR ")

Search1<-twitteR::searchTwitter(terms,n=1000, since="2016-01-01", lang="en")
Search_DF2 <- twListToDF(Search1)

# (Search_DF2$text[1])

## Writing tweets to csv file
FName = "twitter.csv"
write.table(Search_DF2,FName, append=T, row.names=F, col.names=T,  sep=",")