<img src="https://cisp.cachefly.net/assets/articles/images/resized/0000915734_resized_diamonds1022.jpg" alt="Test Image 1" style="zoom: 50%;" />

## Diamonds

## Background/Story

Diamonds, we all know and love them, but other than how pretty they are the next thing in your head might be how expensive they are. In our day and age diamonds are everywhere, an individual cannot hope to be married without having to buy one or multiple diamonds. Having a wife myself I have had to purchase diamonds in the past but I never really understood what gives a diamond its price. In this project I aim to assist an everyday consumer like you and I (assuming you aren't a millionaire) understand better what gives a diamond its value.  

## Data

The data used in this project derives from data acquired from Kaggle. The data sat contains about 54000 diamonds with 11 columns of attributes. The data is from Tiffany & Co's snapshot price list from the year 2017.

The dataset I used has two distinct classifications for the diamond characteristics: 
Numerical:

   Carat = weight of the diamond which ranges from 0.2 to 5.
   Depth = percentage of depth in a diamond which ranges from 43 to 79.
   Price = price in USD which ranges from $326 to $18823
            Categorical:
                       Cut = quality of the cut ranging from Fair, Good, Very Good, Premium, Ideal in order.
                                Clarity = clarity of the diamond ranging from worst to best I1, SI2, SI1, VS2, VS1, VVS2, VVS1, IF 
                        Color = color of diamond ranging from worst to best J to D

<img src="https://beyond4cs.com/wp-content/uploads/2020/12/4Cs-of-diamond-quality-chart-gia-reference.jpg" alt="GIA%20Diamond%20Chart.jpg" style="zoom: 67%;" />

Although not completely matching our data this imagine should give you a general idea of the characteristics in a diamond.

## 4 C's

In the diamond industry the big determining factor of price and quality of a diamond is often referred as the 4 C's. The 4 C's stand for Clarity, Cut, Color and Carat of a diamond. Below I delved deeper into each of these characteristic in my data set to see if I can find anything interesting or worth noting that might give us an insight into diamonds and their prices.  

### Carat

The carat of a diamond is often the first thing people think about when purchasing a diamond but first what is a carat? A carat divided into smaller numbers called points. A carat has 100 points it is important to be precise when talking about carats because even a small fraction of a carat can drastically change the price. It is also important to remember that two diamonds of the exact same carat can be different in price because although carats are important they are only one portion of what determines the price of a diamond.



<img src="Images/Diamond Carat VS Price EDA.png"  />

In this scatter plot you can see the average price of diamonds vs carats. This scatter plot brought to my attention several important points. First is that the vast majority of diamonds sold in this data set are actually of very low carat. In fact in this sample of diamonds 36,438 of them are under a carat which is 67% of the whole . This makes me feel better about not buying my wife a carat diamond! Also worth noting is that past 3 carats not many diamonds are sold only 0.05% or 32 diamonds are over 3 carats!

<img src="Images/Diamond Carat Vs Diamond Price 0-1 Carat.png">

Another fact about diamond carats to know is that even the smallest increase in carat can cause the price to rise significantly. This graph shows a steady increase in price even when the carat changes by 0.1 or 10 points.  It is important to understand that even with other factors affecting the diamonds carats for the most part still has a steady increase regardless of other factors.

### Color

Diamond color is the next characteristic I explored. Diamond color can be confusing as when we refer to color in a diamond we are looking at the lack of color or colorlessness. The closer to colorlessness the higher quality the diamond is. In the diamond industry color ranges from Z to D. D being the highest quality. In the data set I explored it ranges from J (worst) to D (best). 

<img src="Images/Diamond Color VS Price.png"   >

When I plotted the color and price of diamonds I found a very conflicting answer. According to my data set the best rating of color (D) appears to have the second lowest average price the only lower average price is actually the second best rating. This confused me as one could expect because it only makes sense for the better quality the higher the price but in this data set it actually is not the case. This leads to believe me that there must be other factor or factors at play that influence the price more than color. Although interesting that is something that can be investigated further on a subsequent analysis. 

### Clarity

Due to the nature of diamonds when they are formed in the earth like humans they are not always born perfect they are formed with blemishes or defects either internally or on the outside. Diamond clarity refers to the lack of defects. The less defects a diamond has the higher quality therefore a higher price.  Every diamond is very unique, under high magnification no diamond is perfect although some come close. The highest level of clarity is F for flawless they are in fact so rare most jewelers have never seen one. It is important to know diamonds in the flawless category are very rare. In this data frame we have clarity from I1 to IF. I diamonds are Included meaning they have obvious inclusions, IF or Internally Flawless have no inclusions and have blemishes only visible under a 10x magnification.

<img src="Images/Diamond Clarity VS Price.png"  >

This bar chart can be confusing as well as the higher the quality the lower the average price this brings into perspective how rare diamonds are the higher we go in clarity. Like stated previously flawless diamonds are exceedingly rare and we can see that in this chart its rarity causing its average price to be quite low. The two lowest quality diamonds boast the highest average price due to how common their sale is.

### Cut

The beauty of a diamond depends more on the cut of a diamond than anything else. Often confused cut does not actually refer to the shape of the diamond, rather the symmetry, proportion and polish of a diamond. Cut is driven by craftsmanship and technology recent technology like laser cutting and computer-based design have developed cuts of increased complexity and optical performance while minimizing waste. 

<img src="Images/Diamond Cut VS Price.png"  >

In this graph we can see one very interesting thing. The Ideal cut is the lowest average price while also being a good middle ground in quality. So it is safe to say that in this data set diamonds of ideal cut provide more bang for your buck as you can get a decent quality diamond for a relatively low price. Again the lowest quality has the highest price due to the sheer amount of diamonds sold at that quality level, although the others are not very far behind.