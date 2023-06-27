## LO
- Use select, groupby, date, string functions to translate a business problem into an sql query.

## P3
Count the number of movies that Abigail Breslin nominated for oscar

**oscar_nominees:**

| year:   int         |
| :------------------ |
| category:   varchar |
| nominee:    varchar |
| movie:  varchar     |
| winner: int         |
| id: int             |

## P4 [link](https://datalemur.com/questions/tesla-unfinished-parts)
Tesla is investigating production bottlenecks and they need your help to extract the relevant data. Write a query that determines which parts with the assembly steps have initiated the assembly process but remain unfinished.

Assumptions:

parts_assembly table contains all parts currently in production, each at varying stages of the assembly process.
An unfinished part is one that lacks a finish_date.
This question is straightforward, so let's approach it with simplicity in both thinking and solution.

**parts_assembly Table**

| Column Name   | Type     |
| :------------ | :------- |
| part          | string   |
| finish_date   | datetime |
| assembly_step | integer  |

**parts_assembly Example Input**

| part    | finish_date         | assembly_step |
| :------ | :------------------ | :------------ |
| battery | 01/22/2022 00:00:00 | 1             |
| battery | 02/22/2022 00:00:00 | 2             |
| battery | 03/22/2022 00:00:00 | 3             |
| bumper  | 01/22/2022 00:00:00 | 1             |
| bumper  | 02/22/2022 00:00:00 | 2             |
| bumper  |                     | 3             |
| bumper  |                     | 4             |

**Example Output**

| part   | assembly_step |
| :----- | :------------ |
| bumper | 3             |
| bumper | 4             |

**Explanation**

The bumpers in step 3 and 4 are the only item that remains unfinished as it lacks a recorded finish date.

## P5 [link](https://datalemur.com/questions/sql-histogram-tweets)

Assume you're given a table Twitter tweet data, write a query to obtain a histogram of tweets posted per user in 2022. Output the tweet count per user as the bucket and the number of Twitter users who fall into that bucket.

In other words, group the users by the number of tweets they posted in 2022 and count the number of users in each group.

**tweets Table:**

| Column Name | Type      |
| :---------- | :-------- |
| tweet_id    | integer   |
| user_id     | integer   |
| msg         | string    |
| tweet_date  | timestamp |

**tweets Example Input:**

| tweet_id | user_id | msg                                                               | tweet_date          |
| :------- | :------ | :---------------------------------------------------------------- | :------------------ |
| 214252   | 111     | Am considering taking Tesla private at $420. Funding secured.     | 12/30/2021 00:00:00 |
| 739252   | 111     | Despite the constant negative press covfefe                       | 01/01/2022 00:00:00 |
| 846402   | 111     | Following @NickSinghTech on Twitter changed my life!              | 02/14/2022 00:00:00 |
| 241425   | 254     | If the salary is so competitive why won’t you tell me what it is? | 03/01/2022 00:00:00 |
| 231574   | 148     | I no longer have a manager. I can't be managed                    | 03/23/2022 00:00:00 |


**Example Output:**

| tweet_bucket | users_num |
| :----------- | :-------- |
| 1            | 2         |
| 2            | 1         |

**Explanation:**

Based on the example output, there are two users who posted only one tweet in 2022, and one user who posted two tweets in 2022. The query groups the users by the number of tweets they posted and displays the number of users in each group.

## P6 [link](https://datalemur.com/questions/teams-power-users)

Write a query to identify the top 2 Power Users who sent the highest number of messages on Microsoft Teams in August 2022. Display the IDs of these 2 users along with the total number of messages they sent. Output the results in descending order based on the count of the messages.

Assumption:

No two users have sent the same number of messages in August 2022.

**messages Table:**

| Column Name | Type     |
| :---------- | :------- |
| message_id  | integer  |
| sender_id   | integer  |
| receiver_id | integer  |
| content     | varchar  |
| sent_date   | datetime |
|             |          |

**messages Example Input:**

| message_id | sender_id | receiver_id | content                 | sent_date           |
| :--------- | :-------- | :---------- | :---------------------- | :------------------ |
| 901        | 3601      | 4500        | You up?                 | 08/03/2022 00:00:00 |
| 902        | 4500      | 3601        | Only if you're buying   | 08/03/2022 00:00:00 |
| 743        | 3601      | 8752        | Let's take this offline | 06/14/2022 00:00:00 |
| 922        | 3601      | 4500        | Get on the call         | 08/10/2022 00:00:00 |

**Example Output:**

| sender_id | message_count |
| :-------- | :------------ |
| 3601      | 2             |
| 4500      | 1             |


## p8 [link](https://datalemur.com/questions/sql-avg-review-ratings)

Given the reviews table, write a query to retrieve the average star rating for each product, grouped by month. The output should display the month as a numerical value, product ID, and average star rating rounded to two decimal places. Sort the output first by month and then by product ID.

**reviews Table:**

| Column Name | Type          |
| :---------- | :------------ |
| review_id   | integer       |
| user_id     | integer       |
| submit_date | datetime      |
| product_id  | integer       |
| stars       | integer (1-5) |

**reviews Example Input:**

| review_id | user_id | submit_date         | product_id | stars |
| :-------- | :------ | :------------------ | :--------- | :---- |
| 6171      | 123     | 06/08/2022 00:00:00 | 50001      | 4     |
| 7802      | 265     | 06/10/2022 00:00:00 | 69852      | 4     |
| 5293      | 362     | 06/18/2022 00:00:00 | 50001      | 3     |
| 6352      | 192     | 07/26/2022 00:00:00 | 69852      | 3     |
| 4517      | 981     | 07/05/2022 00:00:00 | 69852      | 2     |

**Example Output:**

| mth | product | avg_stars |
| :-- | :------ | :-------- |
| 6   | 50001   | 3.50      |
| 6   | 69852   | 4.00      |
| 7   | 69852   | 2.50      |

****Explanation**

Product 50001 received two ratings of 4 and 3 in the month of June (6th month), resulting in an average star rating of 3.5.

## Comparison between Potgresql and MySQL Datetime functions

[Link](https://www.the-art-of-web.com/sql/postgres-mysql/)