# Project - Anomaly Detection

Contributers:
- [Deangelo Bowen](https://github.com/DeangeloBowen1)
- [Fred Lindsey](https://github.com/fred-lindsey)
- [Mindy Shiben](https://github.com/mindyshiben)
- [Jason Turner](https://github.com/Jason-R-Turner)

---
## Project Deliverables:

---
Email to Team:


Hello,

I have some questions for you that I need to be answered before the board meeting Thursday afternoon. I need to be able to speak to the following questions. I also need a single slide that I can incorporate into my existing presentation (Google Slides) that summarizes the most important points. My questions are listed below; however, if you discover anything else important that I didn’t think to ask, please include that as well.

1. Which lesson appears to attract the most traffic consistently across cohorts (per program)?
2. Is there a cohort that referred to a lesson significantly more than other cohorts seemed to gloss over?
3. Are there students who, when active, hardly access the curriculum? If so, what information do you have about these students?
4. Is there any suspicious activity, such as users/machines/etc accessing the curriculum who shouldn’t be? Does it appear that any web-scraping is happening? Are there any suspicious IP addresses?
5. At some point in 2019, the ability for students and alumni to access both curriculums (web dev to ds, ds to web dev) should have been shut off. Do you see any evidence of that happening? Did it happen before?
6. What topics are grads continuing to reference after graduation and into their jobs (for each program)?
7. Which lessons are least accessed?
8. Anything else I should be aware of?

---

## Project Goals:

- To answer a set of questions and provide additional feedback on findings
- Submit a link to a final notebook on GitHub that asks and answers questions 
- Properly ocument the work done to justify findings
- Compose an email with the answers to the questions/your findings, and in the email, include the link to your notebook in GitHub and attach your slide.

---

## Data Dictionary
|Column | Description | Dtype|
|--------- | --------- | ----------- |
|path| website path accessed| object|
|user_id| user id| int64|
|cohort_id| program numerical id| float64|
|ip| access point of user| object|
|name| actual name of cohort group| object|
|start_date| date cohorts started programs| datetime|
|end_date| date cohort ended/graduated| datetime|
|created_at| date lessons were created| datetime|
|updated_at|date lessons were updated|datetime|
|program_id| ID of programs available|object|
|date_time| date last accessed|datetime|

---

## Project Outline

### 1. Acquire, prepare and clean data set.

We acquired the dataset from the `CodeUp database MySQL server` where we pulled all information related to CodeUp cohorts in the `logs` and the `cohorts` tabel. The pulled dataframe was then saved as a `cirriculum_logs.csv` where we performed our analysis on. 
<br>

### 2. Perform Exploratory Data Analysis on the unencoded data set

To perform exploratory analysis on the dataset, we primarily utilized many vizual tools deriving from seaborn and matplotlib. Then performed mathematical, statistical, and time analysis from various pandas dataframes. 
<br>  

---

## Exploration Summary/Executive Summary:

### Recommendations and Takeaways:

<br> 

#### Question 1: Most accessed lessons:
- Javascript I
- Classification
- HTML-CSS & SQL 
<br>

#### Question 2: Popular lessons accesseds by cohorts
- Teddy & Darden cohorts referred significantly more to the “Slides” & “SQL” lessons respectively than the average of their respective program cohorts
<br>

#### Question 3: Curriculums accessed by active students
- ~50% of the bottom quarter of of active student accessors ceased to access the curriculum over a month before their graduation date
<br>

#### Question 6: Topics referenced MOST by graduates
- Fundamentals (Data Science)
- JavaScript I (Full-Stack)
- Content (Full Stack PHP & Front End Programming)
<br>

#### Question 7: Least accessed lessons: 
- Regression & Story-Telling 


#### _We have no recommendations at this time as this is primarily an analytical observation_

--
### With More Time

- With the data available in this dataset, we cannot draw conclusions on why the bottom accessors cease accessing the curriculum and I'd like to request more data to evaluate the following questions:

- Do students stop accessing because they feel they've acquired enough knowledge? (assess a relationship between access and student performance)

- Could ceasing access be due to dropping out of the program? If so, how often does this occur?

- Do the instructors seem to influence the amount of program access?
--

## Steps to reproduce
- Acquire access to the CodeUp MySQL Database
- Acquire the dataset from the `CodeUp database MySQL server` 
- Pull all information related to CodeUp cohorts in the `logs` and the `cohorts` tabel.
- Utilize many vizual tools deriving from seaborn and matplotlib.
- Then perform mathematical, statistical, and time analysis from various pandas dataframes. 




