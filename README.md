### The World Bank’s
# Women, Business, and Law Index
## Analyzing the Presence of Laws Regarding Women in the Workplace, and Economic and Life Outcomes: A Global Inspection

![image](https://user-images.githubusercontent.com/117952432/202291058-c8c87360-7b26-4fe4-be23-1e88bca5384e.png)

Utilizing the World Bank’s Women, Business and the Law Index, along with a few supplemental datasets, I analyzed the presence of laws regarding women’s equality in the workplace and economic and life outcomes in different regions of the world over time (1971-2022).

##### *Created by: Kristin Akervall, June 2022*
 

### I. Introduction and Data

#### MAIN DATA

##### WBL Index

The main dataset, Women, Business and the Law Index (WBL Index) consists of an Excel spreadsheet that contains information on the presence of gender equality laws for countries around the world in years 1971-2022. This 50+ years of data covers 190 countries in a dataset with 9880 rows and 55 columns. The data can be downloaded at https://wbl.worldbank.org/en/wbl-data.

The WBL Index score is calculated each year from eight subindices: Mobility, Workplace, Pay, Marriage, Parenthood, Entrepreneurship, Assets, and Pension. Each subindex, and the WBL Index itself, is on a scale of 0-100 depending on the coverage of laws in that specific area. This coverage is measured depending on the response to a list of questions for each subindex category. These questions, subindices, the WBL Index score and a few categorization labels for each country (ISO Code, Region, Income Group) create all the columns of the dataset. The fields are described below: (Field names were changed after uploading the file into python for brevity. New field name is in the FIELDS column below.)

| FIELDS | DESCRIPTIONS | EXAMPLE |
| ------ | ------------ | ------- |
| Country | Originally named ‘Economy’ in WBL dataset | Afghanistan |
| ISO | International Organization for Standardization code for country | AFG |
| Region | (Used appended ISO region code in analysis) | South Asia |
| Income Group | Four possible categories | Low income |
| Year | Report year | 1971 |
| Index | Women Business and Law summary index (ranges from 0-100, decimals possible) | 26.3 |
| MOBILITY | Index for questions regarding women’s mobility and freedom of movement (ranges from 0-100) | 25 |
| choose_where_live | Can a woman choose where to live in the same way as a man? | No |
| travel_outside_home | Can a woman travel outside her home in the same way as a man? | No |
| apply_passport | Can a woman apply for a passport in the same way as a man? | No |
| international_travel | Can a woman travel outside the country in the same way as a man? | No |
| WORKPLACE | Index for questions regarding environment in the workplace (ranges from 0-100) | 25 |
| job | Can a woman get a job in the same way as a man? | Yes |
| emp_discr | Does the law prohibit discrimination in employment based on gender? | No |
| leg_sex_harassment | Is there legislation on sexual harassment in employment? | No |
| penal_sex_harassment | Are there criminal penalties or civil remedies for sexual harassment in employment? | No |
| PAY | Index for questions regarding pay and income earning (ranges from 0-100) | 0 |
| equal_pay | Does the law mandate equal remuneration for work of equal value? | No |
| work_night | Can a woman work at night in the same way as a man? | No |
| danger_job | Can a woman work in a job deemed dangerous in the same way as a man? | No |
| indust_job | Can a woman work in an industrial job in the same way as a man? | No |
| MARRIAGE | Index for questions regarding marriage (ranges from 0-100) | 20 |
| obey_husband | Is there no legal provision that requires a married woman to obey her husband? | No |
| head_household | Can a woman be head of household in the same way as a man? | Yes |
| dom_violence | Is there legislation specifically addressing domestic violence? | No |
| divorce | Can a woman obtain a judgment of divorce in the same way as a man? | No |
| remarry | Does a woman have the same rights to remarry as a man? | No |
| PARENTHOOD | Index for questions regarding parental leave (ranges from 0-100) | 0 |
| 14_wk_leave | Is paid leave of at least 14 weeks available to mothers? | No |
| length_mat_leave | Length of paid maternity leave | 0 |
| leave_benefit | Does the government administer 100% of maternity leave benefits? | No |
| paternal_leave | Is there paid leave available to fathers? | No |
| length_pat_leave | Length of paid paternity leave | 0 |
| pat_paid | Is there paid parental leave? | No |
| shared_days | Shared days | 0 |
| mat_days | Days for the mother | 0 |
| pat_days | Days for the father | 0 |
| pregnant | Is dismissal of pregnant workers prohibited? | No |
| ENTRE | Index for questions regarding entrepreneurship opportunities (ranges from 0-100) | 75 |
| credit | Does the law prohibit discrimination in access to credit based on gender? | No |
| contract | Can a woman sign a contract in the same way as a man? | Yes |
| register_bus | Can a woman register a business in the same way as a man? | Yes |
| bank_account | Can a woman open a bank account in the same way as a man? | Yes |
| ASSETS | Index for questions regarding women’s opportunity to hold wealth (ranges from 0-100) | 40 |
| prop_owner | Do men and women have equal ownership rights to immovable property? | Yes |
| daught_inherit | Do sons and daughters have equal rights to inherit assets from their parents? | No |
| spouses_inherit | Do male and female surviving spouses have equal rights to inherit assets? | No |
| admin_autho_assets | Does the law grant spouses equal administrative authority over assets during marriage? | Yes |
| value_nonmon_cont | Does the law provide for the valuation of nonmonetary contributions? | No |
| PENSION | Index for questions regarding pension (ranges from 0-100) | 25 |
| retire_age | Is the age at which men and women can retire with full pension benefits the same? | No |
| retire_partial | Is the age at which men and women can retire with partial pension benefits the same? | No |
| mandatory_age | Is the mandatory retirement age for men and women the same? | Yes |
| childcare_accounted | Are periods of absence due to childcare accounted for in pension benefits? | No |

#### ADDITIONAL DATA

Additional datasets were merged with the WBL Index dataset to provide supplemental data for the analysis. These datasets include:

##### ISO Region Codes
Although the original dataset had a region category, I found that some records had “High income: OECD” listed as region. I wanted to be able to look at income separate from region (and vice versa) and decided instead to use ISO region data since they also have subregions available. This approach offers more granular information. The ISO region dataset includes data for 250 countries.
ISO Region Data source was https://github.com/lukes/ISO-3166-Countries-with-Regional-Codes/blob/master/all/all.csv. 

Only select fields were read in for use in the analysis:

| FIELDS | DESCRIPTIONS | EXAMPLE |
| ------ | ------------ | ------- |
| name | Country name | Aruba |
| alpha-3 | ISO code | ABW |
| region | 5 regions: Africa, Americas, Asia, Europe, Oceania | Americas |
| sub-region | Subregion for each region | Latin America and the Caribbean |
| intermediate region | Select subregions also have intermediate region the further divides the subregion | Caribbean |

##### Percent of National Parliamentary Seats Held By Women
This data was downloaded from the Kaggle website but was originally produced by the World Bank. It includes data for years 1997-2019, and 215 countries are represented in the dataset. It can be found at https://www.kaggle.com/datasets/mathurinache/women-in-power3.

| FIELDS | DESCRIPTIONS | EXAMPLE |
| ------ | ------------ | ------- |
| Country Name | Country name | Albania |
| Country Code | ISO code | ALB |
| Year | Year | 1999 |
| Proportion of seats held by women in national parliaments (%) | Percent of women holding national parliamentary seats | 0.051613 |

##### Ratio of Female to Male Labor Force Participation Rate
This data is available for download on the World Bank website at https://data.worldbank.org/indicator/SL.TLF.CACT.FM.ZS?view=chart. Its original source is from derived data from the International Labour Organization, ILOSTAT database. The dataset was last updated on 4/27/2022. This dataset includes years 1960-2021, however, up until 1990 the data is very sparse, so only data from 1990-2021 was read into my dataframe.

| FIELDS | DESCRIPTIONS | EXAMPLE |
| ------ | ------------ | ------- |
| Country Name | Country name | Albania |
| Country Code | ISO code | ALB |
| Indicator Name | Ratio of female to male labor force participation rate (%) (modeled ILO estimate) |  |
| Indicator Code | (not used in analysis) | SL.TLF.CACT.FM.ZS |
| 1960… 2021 | Each year was represented by a column. During the analysis, I changed the data to display in tall format. | 76.6892436192306 |

##### Child Mortality Rate, Under Age 5, per 1,000 Live Births
This data is also available for download on the World Bank website at https://data.worldbank.org/indicator/SH.DYN.MORT?view=chart. Its original source is from estimates developed by UN Interagency Group (UNICEF, WHO, World Bank, UN DESA Population Division). The dataset was last updated on 4/27/2022. This dataset includes years 1960-2020, however, up until 1990 the data is very sparse, so only data from 1990-2020 was read into my dataframe.

| FIELDS | DESCRIPTIONS | EXAMPLE |
| ------ | ------------ | ------- |
| Country Name | Country name | Albania |
| Country Code | ISO code | ALB |
| Indicator Name | Mortality rate, under-5 (per 1,000 live births) |  |
| Indicator Code | (not used in analysis) | SH.DYN.MORT |
| 1960… 2021 | Each year was represented by a column. During the analysis, I changed the data to display in tall format. | 9.8 |

##### Gross National income per Capita (Current US$)
This data is also available for download on the World Bank website at https://data.worldbank.org/indicator/NY.GNP.PCAP.CD?view=chart. Its original source is from both the World Bank and OECD. The dataset was last updated on 4/27/2022. This dataset includes years 1960-2020, however, up until 1995 the data is very sparse, so only data from 1995-2020 was read into my dataframe.

| FIELDS | DESCRIPTIONS | EXAMPLE |
| ------ | ------------ | ------- |
| Country Name | Country name | Albania |
| Country Code | ISO code | ALB |
| Indicator Name | GNI per capita, Atlas method (current US$) |  |
| Indicator Code | (not used in analysis) | NY.GNP.PCAP.CD |
| 1960… 2021 | Each year was represented by a column. During the analysis, I changed the data to display in tall format. | 5210 |

#### DATA CLEANING STEPS
* After reading in the data, I renamed the columns so they are easier to work with and match with other files.
* I added a unique ID column to the main WBL Index dataset. I then needed to change this ID to string type.
* Used the shape function to check that all my data had been correctly loaded.
* I checked for missing values with the df.isnull().sum() function.
  - I found a missing value in the ISO data and since I knew I would categorize my data with this field, I wanted to investigate this missing data further. I found that the missing value was for Antarctica. After checking my WBL Index data, I realized that I would not be needing Antarctica since it was missing in the WBL Index dataset.
* I checked the datatypes when reading in new files and periodically before merging files.
* I merged the ISO data with the WBL Index data.
* I periodically created new dataframes with a subset of data (for example all 2022 data, or all Europe data) to help keep the dataset I was using for an analysis question focused and manageable.
* When creating the heatmap displaying the standard deviation of subindices by income group, I needed to force a new sort of the data so that it would display in a logical order: High income, Upper middle income, Lower middle income and Low income. (The alphabetical sort was: High income, Low income, Lower middle income, Upper middle income.) In order to do this, I created a new column with a mapped value for my custom sorting.
* When analyzing which country has had the greatest change in index value over time, I created separate data tables for 1971 data and 2022 data. Then, I merged the two tables together and calculated the variance in indices values.
* I omitted rows that had blank data in the Women in Parliamentary Seat data, Percent of Women to Men in Labor Force data, Child Mortality data, and Gross National Income data since there was not complete coverage in these datasets.
* I changed the percent of parliamentary seats held by women column of data to appear neatly as a percentage instead of a decimal.
* I merged the Women in Parliamentary Seats data with the WBL Index data.
* I converted Percent of Women to Men in Labor Force dataset, Child Mortality dataset, and Gross National Income dataset to tall dataframe so it was easier to merge with WBL Index data.
* I merged the Percent of Women to Men in Labor Force dataset with the WBL Index data.
* I inverted the Child Mortality data to be percent of children surviving past age five (instead of children that do not make it to age five) so that it would appear as an increasing curve over time and would be easier to visually compare with the WBL Index data.
* I merged the Child Mortality data with the WBL Index data.
* I merged the Gross National Income data with the WBL Index data.


### II. Methodology
Data was read into python, examined for anomalies or cleaned, and analyzed or merged with other datasets (as described in the bullets above), and ultimately utilized to answer the determined analysis questions.

#### DATA EXPLORATION
Early in the program, I used the describe function to view basic stats on the numeric fields of data.
It was interesting to see that all of the subindices had a minimum value of 0 and maximum of 100 at some point in the dataset, so a very full range of data is included in the main WBL Index dataset. For this reason, I decided to often group the data by region. This allowed me to have a narrower group of data in the analysis and allowed for global comparison. In each chart where data is grouped by region a consistent color was assigned to that region: Africa – blue, Americas – green, Asia – red orange, Europe – purple, and Oceania – yellow.

#### ANALYSIS QUESTIONS AND METHOD OF ANLAYSIS
Below is a list of the analysis questions, fields used in each analysis, and resulting outputs.
Some of the analysis questions for this project centered on the WBL Index dataset alone:

__1.	What countries and regions have the highest WBL index?__

WBL Index data grouped by ISO_region and country, and maximum value of INDEX field displayed. Data then sorted by INDEX.

For additional data visualizations data is group data by ISO_region and ISO_subregion and the average value of the INDEX field is used.

Resulting outputs:
* 1_Highest_WBL_Index_by_Country.csv
* 1_Countries_WBL_Index_100.csv
* 1_Avg_Index_By_Region_2022.jpg
* 1_Avg_Index_Europe_By_Subregion_2022.jpg
* 1_Avg_Index_Asia_By_Subregion_2022.jpg

__2.	What subindices are the highest and lowest? For each region?__

WBL Index data grouped by ISO_region and an average value of each subindex (MOBILITY, WORKPLACE, PAY, MARRIAE, PARENTHOOD, ENTRE, ASSETS, and PENSION) displayed.

Resulting outputs:
* 2_Avg_Subindex_By_Region.csv
* 2_Avg_Subindex_By_Region.jpg

__3.	What is the standard deviation for the indices within regions? Within income group?__

WBL Index data is grouped by ISO_region and the standard deviation for each subindex (MOBILITY, WORKPLACE, PAY, MARRIAE, PARENTHOOD, ENTRE, ASSETS, and PENSION) is displayed. The same data table is produced with only 2022 data.

In additional data tables, data is grouped by ISO_region and the minimum and maximum of the INDEX field is found. The same data table is produced with only 2022 data.

2022 data is also grouped by income_group and the standard deviation for each subindex (MOBILITY, WORKPLACE, PAY, MARRIAE, PARENTHOOD, ENTRE, ASSETS, and PENSION) is displayed.

Resulting outputs:
* 3_Std_Subindex_By_Region.csv
* 3_WBL_MinMax_By_Region.csv
* 3_WBL_2022MinMax_By_Region.csv
* 3_Std_2022_Subindex_By_Region.csv
* 3_Std_2022_Subindex_By_Income.csv
* 3_Std_2022_Subindex_By_Region.jpg
* 3_Std_2022_Subindex_By_Income.jpg

__4.	Are there any trends in indices changing over time? For specific regions?__

WBL Index data is put into a pivot table with data organized with year as the row and ISO_region as the columns. The average of the INDEX is the values. This data is then plotted on a line chart. 

Additional charts are created for each of the subindices.

This question is also addressed by the separate python program named Akervall_Choropleth_Project.py. This program uses plotly to create an animated choropleth map that uses the ISO_code to map the data on a world map, and adjusts the color of each country by INDEX value. The animation is based on the year.

Resulting outputs:
* 4_Avg_WBL_Trend_By_Region.jpg
* 4_Avg_Mobility_Trend_By_Region.jpg
* 4_Avg_Workplace_Trend_By_Region.jpg
* 4_Avg_Pay_Trend_By_Region.jpg
* 4_Avg_Marriage_Trend_By_Region.jpg
* 4_Avg_Parenthood_Trend_By_Region.jpg
* 4_Avg_Entre_Trend_By_Region.jpg
* 4_Avg_Assets_Trend_By_Region.jpg
* 4_Avg_Pension_Trend_By_Region.jpg
* Animated Choropleth Map

__5.	What country has had the greatest change in index value?__

For this analysis question, I subtracted the 1971 WBL Index score from the 2022 score and put this value in a new column named Index_Change. The datatable was then sorted on Index_Change. More notes on how I set up the dataframe are included in the Data Cleaning section. 

Resulting outputs:

* 5_Change_In_WBL_Index_by_Country.csv

__6.	What is the average length of paid maternity leave over time for each region? And paid paternity leave?__

A subset of 2002 data containing Parenthood question responses was grouped by ISO_region and the average value for length_mat_leave and length_pat_leave was found for this question. 

For the data visualizations, all years of data was put into a pivot table with data organized with year as the row and ISO_region as the columns. The average of the length_mat_leave or length_pat_leave was the values. This data is then plotted on two separate line charts—one for length of maternity leave and one for length of paternity leave. 

Resulting outputs:
* 6_Avg_Mat_Pat_Leave_By_Region_2022.csv
* 6_Avg_Mat_Leave_By_Region.jpg
* 6_Avg_Pat_Leave_By_Region.jpg

Other research questions examined the WBL Index data in relation to other datasets:

__7.	How does the WBL Index relate to the percent of national parliamentary seats held by women in a country?__

Data for the percent of national parliamentary seats held by women is put into a pivot table with data organized with year as the row and ISO_region as the columns. The average of the Percent_Women is the values. This data is then plotted on a line chart. 

Data for WBL Index is merged with percent of parliamentary seats held by women and then a scatter plot is created drawing on Percent_Women for the x axis and INDEX for the y axis. The plot color is determined by ISO_region value.

A correlation table is produced based on the merged dataset utilizing the pearson method. 

Data is also grouped by ISO_region and year, and the average of Percent_Women and INDEX is calculated. This data is then sectioned off into subsets of data based on region and a dual axis line chart is created for each region. Percent_Women is placed on the first axis and INDEX is placed on the second axis.

Resulting outputs:

* 7_Avg_Parl_Seats_By_Region_Over_Time.jpg
* 7_Percent_Parl_Seats_And_Index.jpg
* 7_Corr_PercentWomen_Parl.csv
* 7_Avg_Parl_Index_Africa.jpg
* 7_Avg_Parl_Index_Americas.jpg
* 7_Avg_Parl_Index_Asia.jpg
* 7_Avg_Parl_Index_Europe.jpg
* 7_Avg_Parl_Index_Oceania.jpg

__8.	How does the WBL Index relate to the ratio of female to male labor force participation rate (%)?__

Ratio of female to male labor force participation rate data is put into a pivot table with data organized with year as the row and ISO_region as the columns. The average of the Ratio Women Labor field is the values. This data is then plotted on a line chart.

Merged data is used for a scatter plot and the Ratio Women Labor field is used for the x axis and INDEX for the y axis. The plot color is determined by ISO_region value. Because this initial scatterplot appeared a bit smudgy and unclear, the scatterplot was also created using only the most recent year of data, 2021.

Merged data is also grouped by ISO_region and year, and the average of the Ratio Women Labor field and INDEX is calculated. This data is then sectioned off into subsets of data based on region and a dual axis line chart is created for each region. Ratio Women Labor is placed on the first axis and INDEX is placed on the second axis.

Resulting outputs:

* 8_Avg_Ratio_Women_Labor_By_Region.jpg
* 8_Ratio_Women_Labor_And_Index_2021.jpg
* 8_Avg_Ratio_Women_Labor_Index_Africa.jpg 
* 8_Avg_Ratio_Women_Labor_Index_Americas.jpg
* 8_Avg_Ratio_Women_Labor_Index_Asia.jpg
* 8_Avg_Ratio_Women_Labor_Index_Europe.jpg
* 8_Avg_Ratio_Women_Labor_Index_Oceania.jpg

__9.	How does the ratio of women to men in the labor force relate to the Workplace subindex? To the Pay subindex? To the Parenthood subindex?__
Similar to the regional charts created for the ratio of women to men in the labor force and WBL Index, I created additional charts using the Workplace subindex instead of the WBL Index. Merged data is grouped by ISO_region and year, and the average of the Ratio Women Labor field and WORKPLACE is calculated. This data is then sectioned off into subsets of data based on region and a dual axis line chart is created for each region. Ratio Women Labor is placed on the first axis and WORKPLACE is placed on the second axis.

Merged data is grouped by ISO_region and year, and the average of the Ratio Women Labor field and PAY is calculated. This is similar to the regional charts above except uses the Pay subindex. This data is then sectioned off into subsets of data based on region and a dual axis line chart is created for each region. Ratio Women Labor is placed on the first axis and PAY is placed on the second axis.

Merged data is grouped by ISO_region and year, and the average of the Ratio Women Labor field and PARENTHOOD is calculated. This is similar to the regional charts above except uses the Parenthood subindex. This data is then sectioned off into subsets of data based on region and a dual axis line chart is created for each region. Ratio Women Labor is placed on the first axis and PARENTHOOD is placed on the second axis.

Resulting outputs:

* 9_Avg_Ratio_Women_Labor_WorkSubindex_Africa.jpg
* 9_Avg_Ratio_Women_Labor_WorkSubindex_Americas.jpg
* 9_Avg_Ratio_Women_Labor_WorkSubindex_Asia.jpg
* 9_Avg_Ratio_Women_Labor_WorkSubindex_Europe.jpg
* 9_Avg_Ratio_Women_Labor_WorkSubindex_Oceania.jpg
* 9_Avg_Ratio_Women_Labor_PaySubindex_Africa.jpg
* 9_Avg_Ratio_Women_Labor_PaySubindex_Americas.jpg
* 9_Avg_Ratio_Women_Labor_PaySubindex_Asia.jpg
* 9_Avg_Ratio_Women_Labor_PaySubindex_Europe.jpg
* 9_Avg_Ratio_Women_Labor_PaySubindex_Oceania.jpg
* 9_Avg_Ratio_Women_Labor_ParentSubindex_Africa.jpg
* 9_Avg_Ratio_Women_Labor_ParentSubindex_Americas.jpg
* 9_Avg_Ratio_Women_Labor_ParentSubindex_Asia.jpg
* 9_Avg_Ratio_Women_Labor_ParentSubindex_Europe.jpg
* 9_Avg_Ratio_Women_Labor_ParentSubindex_Oceania.jpg

__10.	How does childhood mortality relate to the Parenthood subindex?__
Child mortality rate is put into a pivot table with data organized with year as the row and ISO_region as the columns. The average of the Child Mortality field is the values. This data is then plotted on a line chart. This chart displayed a decreasing slope for each region as over time more and more children in every region survive through age five at greater numbers. I realized it would be difficult to compare this decreasing slope with an increasing slope of WBL Index score, so I inverted the Child Mortality data to instead show the percent of children surviving past age five and recreated the line chart. (More details on this data transformation is found in the Data Cleanup section of the report.)

Child survival data is merged with WBL Index data and is grouped by ISO_region and year, and the average of the Inverted Child Mortality field and Parenthood subindex is calculated. This data is then sectioned off into subsets of data based on region and a dual axis line chart is created for each region. InvertChild Mortality is placed on the first axis and PARENTHOOD is placed on the second axis.

Resulting outputs:

* 10_Avg_Child_Mortality_By_Region.jpg
* 10_Avg_Child_Life_By_Region.jpg
* 10_Avg_Child_Live_Parent_Africa.jpg
* 10_Avg_Child_Live_Parent_Americas.jpg
* 10_Avg_Child_Live_Parent_Asia.jpg
* 10_Avg_Child_Live_Parent_Europe.jpg
* 10_Avg_Child_Live_Parent_Oceania.jpg

__11.	How does gross national income per capita relate to the WBL Index? To the pay subindex?__
Data for WBL Index is merged with gross national income per capita and a correlation table is produced based on the merged dataset utilizing the pearson method.

Gross national income per capita data is put into a pivot table with year as the rows and ISO_region as the column. Data values are the average for the GNI (Gross National Income) field. This data is then plotted on a line chart.

Data is also grouped by ISO_region and year, and the average of GNI, INDEX, and the Pay subindex is calculated. This data is then sectioned off into subsets of data based on region and a dual axis line chart is created for each region. GNI is placed on the first axis and INDEX is placed on the second axis. Then a second round of charts is produced with Pay on the second axis.

Resulting outputs:

* 11_Corr_GNI.csv
* 11_Avg_GNI_By_Region.jpg
* 11_Avg_GNI_Index_Africa.jpg
* 11_Avg_GNI_Index_Americas.jpg
* 11_Avg_GNI_Index_Asia.jpg
* 11_Avg_GNI_Index_Europe.jpg
* 11_Avg_GNI_Index_Oceania.jpg
* 11_Avg_GNI_Pay_Africa.jpg
* 11_Avg_GNI_Pay_Americas.jpg
* 11_Avg_GNI_Pay_Asia.jpg
* 11_Avg_GNI_Pay_Europe.jpg
* 11_Avg_GNI_Pay_Oceania.jpg

### IV. Description of the Program and Output Files

#### PROGRAM DESCRIPTION
This program explores the WBL Index data and addresses the analysis questions previously listed. A Jupyter notebook contains the program with the exception of the analysis resulting in the animated choropleth map displaying the WBL Index values over time on a changing geographical map. This analysis is in a separate python file Akervall_Choropleth_Project.py. Noted in the code is an explanation of commands and why they were used.

The outputs of this program include 65 charts and 12 tables. The charts include a variety of visualizations including bar charts, heat maps, line charts, scatterplots, dual axis line charts, and an animated choropleth map. The tables include data tables and correlation tables.

Libraries used for this analysis include pandas, numpy, plotly, matplot, and seaborn.

#### OUTPUT FILES AND INITIAL FINDINGS
##### Q1. What countries and regions have the highest WBL index?
The table saved as output file 1_Highest_WBL_Index_by_Country.csv lists the region, country, and highest WBL Index value recorded for each country in the dataset. Below is a snapshot of the first 10 records. 

| ISO_region | Country | INDEX |
|------------|---------|-------|
| Europe | Portugal | 100 |
| Americas | Canada | 100 |
| Europe | Luxembourg | 100 |
| Europe | Belgium | 100 |
| Europe | Sweden | 100 |
| Europe | Latvia | 100 |
| Europe | Spain | 100 |
| Europe | Ireland | 100 |
| Europe | Iceland | 100 |
| Europe | Greece | 100 |

Because there were several countries that had a score of 100, I wanted to find out more about these countries specifically and how many there were. The program prints a statement with the total number of countries with a WBL Index score of 100 and saves this list of countries with an index score of 100 to a csv file 1_Countries_WBL_Index_100.csv.

> The number of countries that have received a WBL Index of 100:  12


| ISO_region |ISO_subregion | Country | INDEX |
|------------|--------------|---------|-------|
| Americas | Northern America | Canada | 100 |
| Europe | Northern Europe | Denmark | 100 |
| Europe | Northern Europe | Iceland | 100 |
| Europe | Northern Europe | Ireland | 100 |
| Europe | Northern Europe | Latvia | 100 |
| Europe | Northern Europe | Sweden | 100 |
| Europe | Southern Europe | Greece | 100 |
| Europe | Southern Europe | Portugal | 100 |
| Europe | Southern Europe | Spain | 100 |
| Europe | Western Europe | Belgium | 100 |
| Europe | Western Europe | France | 100 |
| Europe | Western Europe | Luxembourg | 100 |

Noticing that Europe was well represented in this list, I anticipated that Europe would have the highest average WBL Index score, but wanted to compare the regional averages with a data visualization. For this, I sectioned of just the most recent year of data and turned my data table into a bar chart. This bar chart (1_Avg_Index_By_Region_2022.jpg) shows how the average WBL Index for Europe is much higher than other regions.

![image](https://user-images.githubusercontent.com/117952432/202822119-8ff90d76-7155-43a6-b859-080b3cc7347d.png)

Since Europe had the highest average, I looked at the subregions in more detail and created another bar chart with just Europe, and grouped the INDEX data by ISO subregion. This chart is saved as 1_Avg_Index_Europe_By_Subregion_2022.jpg. Within Europe it appears that Northern Europe has the highest average WBL Index score and Eastern Europe has the lowest—however all subregions’ averages are greater than 80.

![image](https://user-images.githubusercontent.com/117952432/202822177-7507c374-0468-4844-b27a-61b62cec6398.png)

And, I looked at the subregions for Asia in more detail, as this region had the lowest average WBL Index in 2022. Again, I worked with a subset of the data that only included records for Asia in 2022 and grouped the data by ISO_subregion. This bar chart (1_Avg_Index_Asia_By_Subregion_2022.jpg) shows that Eastern Asia has the highest average WBL Index score and Southern and Western Asia have the lowest. Eastern Asia has an average WBL Index that is comparable to some of the European subregions (above 80), but the Southern and Western Asia subregions have an average score that hovers around 60.

![image](https://user-images.githubusercontent.com/117952432/202822196-5037a6ce-3555-462e-8e58-58e9abeaa1f2.png)

