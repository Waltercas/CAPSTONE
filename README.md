<img src="https://cisp.cachefly.net/assets/articles/images/resized/0000915734_resized_diamonds1022.jpg" alt="Test Image 1" style="zoom: 50%;" />

## Diamonds

## Background/Story

Diamonds, we all know and love them, but other than how pretty they are the next thing in your head might be how expensive they are. In our day and age diamonds are everywhere, an individual cannot hope to be married without having to buy one or multple diamonds. Having a wife myself I have had to purchase diamonds in the past but I never really understood what gives a diamond its price. In this project I aim to assist an everyday consumer like you and I (assuming you aren't a millionaire) understand better what gives a diamond its value.  

## Data

The data used in this project derives from data acquired from Kaggle. The data sat contains about 54000 diamonds with 11 columns of attributes. The data does not provide what markets and when these diamonds were sold. 

The dataset I used has two distinct classifications for the diamond characteristics: 
Numerical:

          * Carat = weight of the diamond which ranges from 0.2 to 5.
                    * Depth = percentage of depth in a diamond which ranges from 43 to 79.
                    * Price = price in USD which ranges from $326 to $18823
                    Categorical:
                              * Cut = quality of the cut ranging from Fair, Good, Very Good, Premium, Ideal in order.
                                        * Clarity = clarity of the diamond ranging from worst to best I1, SI2, SI1, VS2, VS1, VVS2, VVS1, IF 
                                        * Color = color of diamond ranging from worst to best J to D

<img src="https://beyond4cs.com/wp-content/uploads/2020/12/4Cs-of-diamond-quality-chart-gia-reference.jpg" alt="GIA%20Diamond%20Chart.jpg" style="zoom: 67%;" />

Although not completely matching our data this imagine should give you a general idea of the characteristics in a diamond.

## 4 C's

In the diamond industry the big determining factor of price and quality of a diamond is often referred as the 4 C's. The 4 C's stand for Clarity, Cut, Color and Carat of a diamond. Below I delved deeper into each of these characteristic in my data set to see if I can find anything interesting or worth noting that might give us an insight into diamonds and their prices.  

### Carat

The carat of a diamond is often the first thing people think about when purchasing a diamond but first what is a carat? A carat divided into smaller numbers called points. A carat has 100 points it is important to be precise when talking about carats because even a small fraction of a carat can drastically change the price. It is also important to remember that two diamonds of the exact same carat can be different in price because although carats are important they are only one portion of what determines the price of a diamond.



<img src="/home/walter/Desktop/CAPSTONE/CAPSTONE/Images/Diamond Carat VS Price EDA.png" style="zoom: 80%;" />

In this scatter plot you can see the average price of diamonds vs carats. This scatter plot brought to my attention several important points. First is that the vast majority of diamonds sold in this data set are actually of very low carat. In fact in this sample of diamonds 36,438 of them are under a carat which is 67% of the whole . This makes me feel better about not buying my wife a carat diamond! Also worth noting is that past 3 carats not many diamonds are sold only 0.05% or 32 diamonds are over 3 carats!

![](/home/walter/Desktop/CAPSTONE/CAPSTONE/Images/Diamond Carat Vs Diamond Price 0-1 Carat.png)

Another fact about diamond carats to know is that even the smallest increase in carat can cause the price to rise significantly. This graph shows a steady increase in price even when the carat changes by 0.1 or 10 points. 