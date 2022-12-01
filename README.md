# Amazon_vine_analysis

# Summary
1- Deliverable 1
In this deliverable we did the following steps:

- Extracted the "Gift Cards" reviews dataset from the list of review datasets from AWS S3 bucket and loaded into a DataFrame.

- Conducted necessary Transformations of the extracted dataset to make sure that the DataFrames match in both data type and column name. This will fit the dataset into tables of the schema file.

- Loaded the DataFrames that correspond to tables in pgAdmin.

and got the following results

![Custermer_ID](https://user-images.githubusercontent.com/53358476/204941274-0ab6a904-6a48-47b9-9255-14d4eb114632.PNG)


![Products_Id](https://user-images.githubusercontent.com/53358476/204941281-9e521a75-bb2a-44d1-babf-7de5d3cf72cc.PNG)


![Review_ID](https://user-images.githubusercontent.com/53358476/204941294-bee1d776-b48a-4e43-a80b-fc9770162d8a.PNG)


![Vine_table](https://user-images.githubusercontent.com/53358476/204941302-9d885e56-94de-46da-a228-d0a0b6c55f3a.PNG)

# Deliverable 2

 We shown if there is any bias towards reviews that were written as part of the Vine program. and we will determine if having a paid Vine review makes a difference in the percentage of 5-star reviews
 
 ![Total_votes](https://user-images.githubusercontent.com/53358476/204941595-bd6f3689-7fd0-4317-bac5-9149e99f951f.PNG)
 
- There are 149086 total reivews
- There are 129709 5-star reviews
- There are total 0 vine (vine = Y) reviews
- There are 0,Five-star vine (vine = Y) reviews
- There are 0.0 % 5-star vine (vine = Y) reviews

# Results
There are zero paid 5 start reviews. Our dataset is for gift cards and it seems like companies don't pay for gift card reviews.
It's hard to detremine bias as there is not enough data to conclude paid reviews.
