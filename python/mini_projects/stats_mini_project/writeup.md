## Analyzing consumer behavior of a mobile gaming app

You have been given data for a mobile game publisher. There are four tables:

- Game users: This contains the records for people who downloaded the mobile game.
- Game actions: This contains the records for the actions that the user took in the game.
- Game purchases: Tracks the purchases of in game currency in USD
- Exp_assignment: Table contains records of which variant users were assigned to for a particular experiment.

The company has many business questions and they think that some one with a statistics background can help them.

You are given a postgres data dump [`dwh.sql`](./sql_dump/dwh.sql). Use `psql` to create database with the desired tables using the `dwh.sql` file. (Hint use `psql -U <username> -h <host> -d <dbname>  < dwh.sql`. You may want to create a database called `dwh` before you run this command) 

**Task 1**

A product team at this company has implemented a new version of the onboarding flow in the gaming app. This consists of series of screens that allow a new user to register on the gaming app and start playing mobile games.

It is hoped that the new version will increase the number of new users who complete the onboarding flow. 

The new version was introduced in an experiment called `Onboarding`. Under this experiment, users are assigned to either a control group or a treatment group. This data should be present in the `exp_assignment` table if you did the data upload correctly.

If you see an entry `onboarding complete` in the table `game_actions`, then that means that a user has completed the onboarding flow.

Armed with this information, can you help them? (Hint: You will need to identify which statistical test you can do. After you've done this, you need to do necessary data transforms in sql and finally do the test either using excel or python.)

**Task 2**

Another related question that the business needs an answer to is, if the new onboarding flow has increased the user spending on in-game currency?

You will need to consider `game_purchases` and `exp_assignment` tables. (Hint: You will need to identify which statistical test you can do. After you've done this, you need to do necessary data transforms in sql and finally do the test either using excel or python.)


**Task 3**

Related to the previous task, a similar business question that has to be answered is the following:

Is there any difference in the spending by users who completed the new onboarding flow vs those who completed the old onboarding flow? (Hint: You will need to identify which statistical test you can do. After you've done this, you need to do necessary data transforms in sql and finally do the test either using excel or python.)

**Task 4**

The game developer has been rolling out the previous versions of this app, where in the marketing emails are auto opted-in by new users.

Lately there has been a legislation which prevents app companies from auto opt in services like marketing emails etc.

The company had to comply to this legislation. So on 27/01/2020, the automatic email opt-in was removed.

Was there any negative impact on the email opt-in rates? You can compare the rates 2 weeks before and after the change was done.

`game_users` and `game_actions` are the relevant tables you should be looking at. (Hint: You will need to identify which statistical test you can do. After you've done this, you need to do necessary data transforms in sql and finally do the test either using excel or python.)


## Submission Guidelines and Rubric

You can either make a submission via jupyter notebook on v-learn or make a submission on github and provide the github link.

Below are some examples of good readme and github project structure:

- [Example Readme](https://github.com/Wittline/uber-expenses-tracking)
- [Example Readme](https://github.com/JarrodAJ/sec_employee_information_extraction)
- [Example Readme](https://github.com/Gunnvant/autocomplete_ngrams)
- [Example Readme](https://github.com/Gunnvant/calendar_parser)

### Rubric

**Task 1,2,3 and 4**

- Correct null and alternate hypothesis is provided
- SQL code to pull relevant data is provided
- Correct p-value is computed and subsequent rejection or non-rejection of null hypothesis is provided.




