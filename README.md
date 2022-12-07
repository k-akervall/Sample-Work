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

##### Q2. What subindices are the highest and lowest? For each region?
This table lists the average subindices value for each region. The output data table is saved as 2_Avg_Subindex_By_Region.csv and corresponding bar chart is saved as 2_Avg_Subindex_By_Region.jpg.

| ISO_region | MOBILITY | WORKPLACE | PAY | MARRIAGE | PARENTHOOD | ENTRE | ASSETS | PENSION |
|------------|----------|-----------|-----|----------|------------|-------|--------|---------|
| Africa | 75.569801 | 34.196937 | 42.120726 | 47.656695 | 28.176638 | 61.235755 | 56.189459 | 65.019587 |
| Americas | 86.414835 | 46.991758 | 60.453297 | 67.824176 | 31.439560 | 74.285714 | 88.043956 | 72.074176 |
| Asia | 71.013622 | 36.568510 | 31.730769 | 51.474359 | 24.190705 | 74.759615 | 68.285256 | 48.888221 |
| Europe | 97.656250 | 56.334135 | 57.115385 | 80.115385 | 66.019231 | 80.685096 | 97.230769 | 59.627404 |
| Oceania | 88.381410 | 39.943910 | 53.565705 | 82.275641 | 6.730769 | 79.607372 | 52.179487 | 68.669872 |

This bar chart shows the variation of scores for subindices by region. In almost every region (with Europe being the exception) the lowest subindex score is for Parenthood. The scores for Workplace are also generally low, and scores for Mobility are quite high across all regions. Oceania appears to have large variation of scores depending on the subindex.

![image](https://user-images.githubusercontent.com/117952432/202825653-f050475a-4720-4781-90a1-4c43eba53b17.png)

##### Q3. What is the standard deviation for the indices within regions?
It occurred to me that each region has its own variation of scores within the region. For example, the Africa region contains countries such as Sudan, with a WBL Index of 29.4 in 2022 and South Africa, with an WBL Index of 88.1 in 2022. The standard deviation reveals the amount of variation within a region and over time. The table below lists the minimum WBL Index score, maximum WBL Index score, and standard deviation for each region. This table shows that Asia has the highest standard deviation and Oceania has the lowest. Asia also ties with Africa for the lowest WBL Index score, and Europe and the Americas tie with the highest WBL Index score. The output data table is saved as 3_WBL_MinMax_By_Region.csv. 

| ISO_region | min INDEX | max INDEX | std INDEX |
|------------|-----------|-----------|-----------|
| Africa | 17.500 | 89.375 | 15.327807 |
| Americas | 30.625 | 100.000 | 14.083300 |
| Asia | 17.500 | 94.375 | 18.558649 |
| Europe | 33.750 | 100.000 | 15.012421 |
| Oceania | 41.250 | 97.500 | 11.962596 |

This table lists the standard deviation for all subindices. The output data table is saved as 3_Std_Subindex_By_Region.csv. One thing that stood out to me in this table is that Oceania has a lower standard deviation within the Marriage and Entrepreneurship subindices. I also remembered from the previous bar chart that these subindices are some of the highest scores for Oceania. It is interesting that there is a higher level of alignment in this area within Oceania. 

| ISO_region | MOBILITY | WORKPLACE | PAY | MARRIAGE | PARENTHOOD | ENTRE | ASSETS | PENSION |
|------------|----------|-----------|-----|----------|------------|-------|--------|---------|
| Africa | 15.327807 | 21.770071 | 33.215429 | 28.351552 | 28.772420 | 25.665800 | 28.196988 | 27.901471 | 28.947663 |
| Americas | 14.083300 | 15.459461 | 34.202650 | 23.555008 | 24.908670 | 23.594387 | 19.339299 | 16.563412 | 24.111991 |
| Asia | 18.558649 | 37.649292 | 30.032276 | 27.600594 | 32.726316 | 26.887767 | 14.242472 | 27.952586 | 27.349807 |
| Europe | 15.012421 | 8.819150 | 32.776172 | 36.043787 | 17.346486 | 24.741465 | 14.396614 | 10.288041 | 31.613925 |
| Oceania | 11.962596 | 13.408942 | 27.025434 | 27.325730 | 9.908781 | 18.260236 | 9.700888 | 34.301933 | 19.729145 |

Since these data tables are accounting for variation within a region and variation over time, I also created tables that only look at the most current year of data to isolate the geographic variations from the time variations.

The table below lists the minimum WBL Index score, maximum WBL Index score, and standard deviation for each region for 2022 only. This table shows that now Europe has the lowest standard deviation. I believe this means that Europe has had more change over time in their WBL Index scores. Asia continues to have the largest standard deviation even within the 2022 data. The output data table is saved as 3_WBL_2022MinMax_By_Region.csv.

| ISO_region | min INDEX | max INDEX | std INDEX |
|------------|-----------|-----------|-----------|
| Africa | 29.375 | 89.375 | 13.747722 |
| Americas | 61.250 | 100.000 | 9.304250 |
| Asia | 26.250 | 94.375 | 19.767862 |
| Europe | 73.125 | 100.000 | 7.147131 |
| Oceania | 55.625 | 97.500 | 15.340208 |

This table lists the standard deviation for all subindices for 2022 only. From this table we see that Europe has a standard deviation of 0 for Mobility and for Assets. This means that the European countries are in total alignment in these areas. The output data table is saved as 3_Std_2022_Subindex_By_Region.csv.

| ISO_region | MOBILITY | WORKPLACE | PAY | MARRIAGE | PARENTHOOD | ENTRE | ASSETS | PENSION |
|------------|----------|-----------|-----|----------|------------|-------|--------|---------|
| Africa | 13.747722 | 20.693978 | 28.178452 | 30.987278 | 29.543463 | 22.792474 | 21.943681 | 27.400796 | 24.479202 |
| Americas | 9.304250 | 12.964074 | 28.752055 | 19.119263 | 13.144319 | 28.367338 | 13.480456 | 10.273569 | 17.513500 |
| Asia | 19.767862 | 30.052407 | 32.781615 | 32.304890 | 32.678859 | 29.890462 | 13.965510 | 27.470164 | 28.403126 |
| Europe | 7.147131 | 0.000000 | 13.736882 | 22.636693 | 6.076436 | 11.886213 | 8.373302 | 0.000000 | 28.278605 |
| Oceania | 15.340208 | 12.309149 | 36.084392 | 27.866021 | 5.773503 | 36.306774 | 12.309149 | 37.294894 | 7.216878 |

I created a visual representation of this data with a heat map. The heatmap shows us that Asia and Africa have a larger amount of variation within different countries’ laws as it has a darker blue color for many of the subindices. The differences in Oceania really seem to vary based on the subindex as this region seems to have a lot of contrast in the heat map: Workplace, Parenthood and Assets have a high standard deviation and Marriage, and Pension have a lower standard deviation. Looking along the verticals, Entrepreneurship seems to have the least amount of variation in all the regions and Workplace has more variation. This output file is saved as 3_Std_2022_Subindex_By_Region.jpg.

![image](https://user-images.githubusercontent.com/117952432/202826427-205cfe7f-333c-4481-b911-b512cafb8874.png)

I wondered how much of the variation with regions can be explained with income and decided to create the same data tables and chart with the data displayed by income group instead of region. The data table output was saved as 3_Std_2022_Subindex_By_Income.csv.

| ISO_region | MOBILITY | WORKPLACE | PAY | MARRIAGE | PARENTHOOD | ENTRE | ASSETS | PENSION |
|------------|----------|-----------|-----|----------|------------|-------|--------|---------|
| High income | 16.814039 | 18.147699 | 25.054765 | 23.697260 | 21.067977 | 33.965189 | 11.889872 | 23.023362 | 22.089332 |    
| Upper middle | 13.258919 | 17.657661 | 30.928779 | 25.429938 | 24.587088 | 30.488729 | 17.770746 | 25.157123 | 24.829737 |
| Lower middle | 14.609014 | 21.923497 | 29.601734 | 30.130189 | 28.403063 | 24.971364 | 18.768930 | 26.208180 | 25.893137 |
| Low income | 17.369171 | 26.764644 | 31.086109 | 35.841532 | 31.496031 | 22.257237 | 16.554107 | 28.153426 | 28.216198 |

And the chart output was saved as 3_Std_2022_Subindex_By_Income.jpg. This chart shows that the low income group has the most variation in laws, while the high income group has the least variation with the exception of Parenthood. Parenthood appears to have a higher standard deviation within the upper middle and high income groups. Entrepreneurship appears to have less variation in laws in all income groups.

![image](https://user-images.githubusercontent.com/117952432/205554923-35988f86-f27d-448f-a84f-ddc74fb3cc19.png)

##### Q4. Are there any trends in indices changing over time? For specific regions?

To answer this question, I created a line chart with the average WBL Index over time by ISO region. This chart shows that in every region the WBl Index has increased over time and is saved as 4_Avg_WBL_Trend_By_Region.jpg.

![image](https://user-images.githubusercontent.com/117952432/205555032-cc5185c6-16d0-40b3-a2de-2d924317bf21.png)

This question can also be examined with the separate python program created as part of this project named Akervall_Choropleth_Project.py. This program can be run in python and imports the same data as used in the jupyter notebook (WBL Index data and ISO data). It uses the same steps to read in the data and convert it into the indexdf dataframe format. Then it created an animated choropleth map that shows how the WBL Index changes in countries over time. The python program opens a new browser window and the user is able to “play” through the data by clicking the play button at the bottom near the year legend. A static version of the chart is included below. This snapshot is from year 2022. (Spoiler alert! Keep your eye on Spain as the animation progresses. I was surprised to see this country’s WBL Index value pop up so early. Analysis included later on in this report will also touch on this data point.)

![image](https://user-images.githubusercontent.com/117952432/205555088-456f8fef-88eb-49e8-94b4-e2de62b6e092.png)

I also created a line chart displaying the change in the Mobility subindex over time by region and saved it as 4_Avg_Mobility_Trend_By_Region.jpg. Again, Europe has the highest score in this area in all years of data. It is interesting that Oceania appears to have flatlined in about 1985, but is possibly increasing again now.

![image](https://user-images.githubusercontent.com/117952432/205555137-906295a0-8cd4-4090-9e50-9559085e4e6a.png)

I created a line chart displaying the change in the Workplace subindex over time by region and saved it as 4_Avg_Workplace_Trend_By_Region.jpg. This chart shows that many of the regions had a similar subindex score up until the mid-2000s when Europe put in place laws in this area. It is also interesting to see that Africa actually has a higher average Workplace score than the Americas now. Africa rose from the lowest line to the second highest line in the course of the 50 years. 

![image](https://user-images.githubusercontent.com/117952432/205555174-8e22587d-f5df-40de-81b0-da571ad411fe.png)

I created a line chart displaying the change in the Pay subindex over time by region and saved it as 4_Avg_Workplace_Trend_By_Region.jpg. This chart shows that Europe did not actually start with the highest average subindex score, but made changes again in the mid-2000s that raised their average to the highest score.

![image](https://user-images.githubusercontent.com/117952432/205555201-148bef41-388d-4072-8c25-af197874e318.png)

I created a line chart displaying the change in the Marriage subindex over time by region and saved it as 4_Avg_Marriage_Trend_By_Region.jpg. I remember finding that the standard deviation for Oceania in the area of Marriage was quite low. It is interesting to see that this region has had laws regarding women’s quality in Marriage for a long time and must have a great deal of alignment within different Oceanic countries. I am curious if this might be a reflection of culture.

![image](https://user-images.githubusercontent.com/117952432/205555245-36f46c90-e043-41bd-895b-c0cc7da39dd1.png)

I created a line chart displaying the change in the Parenthood subindex over time by region and saved it as 4_Avg_Parenthood_Trend_By_Region.jpg. This chart displays that the average score for the Americas, Africa and Asia all hover around the same point that Europe was in 1980—40 years ago.

![image](https://user-images.githubusercontent.com/117952432/205555273-55a0d121-74d9-4dae-9ec4-d83470c61048.png)

I created a line chart displaying the change in the Entrepreneurship subindex over time by region and saved it as 4_Avg_Entre_Trend_By_Region.jpg. Again, this chart appears to show that Europe made changes to their laws in the mid-2000s that considerable rose this average subindex score.

![image](https://user-images.githubusercontent.com/117952432/205555311-b4ccbddd-af89-41cd-8ea2-7b42fecb692f.png)

I created a line chart displaying the change in the Assets subindex over time by region and saved it as 4_Avg_Assets_Trend_By_Region.jpg. This chart shows that while there has been modest change in Europe, the Americas, and Africa, both Asia and Oceania have had minor changes during the last 50 years in the area of Assets.

![image](https://user-images.githubusercontent.com/117952432/205555366-c52e355a-73b9-49aa-bc36-d885204c5142.png)

I created a line chart displaying the change in the Pension subindex over time by region and saved it as 4_Avg_Pension_Trend_By_Region.jpg. This chart shows that the Americas actually have the highest average subindex score. It also shows that while the subindex increased over the course of the 50 years, at certain time periods the average subindex score actually decreased in regions. None of the other subindex line charts showed a decrease. I am curious why this is.

![image](https://user-images.githubusercontent.com/117952432/205555409-5049ae8f-9594-484b-9e44-d4d01ec4170f.png)


##### Q5. What country has had the greatest change in index value?

This table displays the County, ISO code and region, income group, and 1971 WBL Index value (the earliest index available), the 2022 WBL Index value (the most latest index available) and the variation between the two indices. The complete output file is saved as 5_Change_In_WBL_Index_by_Country and the first five records are listed below. Looking at the table, many of the countries with the highest index change are in the high income group. For this reason, the index change of 64.375 for São Tomé and Príncipe stands out to me as an interesting piece of data. I am curious what happened in this country (which is classified as Lower middle income) to move from a score of 18.750 to 83.125.


|  | Country | ISO_code | ISO_region | Income_group | 1971 INDEX | 2022 INDEX | Index_Change | 
|--|---------|----------|------------|--------------|------------|------------|--------------|
| 156 | Spain	| ESP	| Europe	| High income	| 33.750	| 100.000	| 66.250 |
| 178	| United Arab Emirates	| ARE	| Asia	| High income	| 17.500	| 82.500	| 65.000 |
| 143	| São Tomé and Príncipe	| STP	| Africa	| Lower middle income	| 18.750	| 83.125	| 64.375 |
| 154	| South Africa	| ZAF	| Africa	| Upper middle income	| 25.625	| 88.125	| 62.500 |
| 15 |	Belgium	| BEL	| Europe	| High income	| 38.125	| 100.000	| 61.875 |

The program also identifies the country with the greatest change in WBL Index value in a printed statement:

> Country with the greatest change in index value: 

|  | Country | ISO_code | ISO_region | Income_group | 1971 INDEX | 2022 INDEX | Index_Change | 
|--|---------|----------|------------|--------------|------------|------------|--------------|
| 156 | Spain	| ESP	| Europe	| High income	| 33.750	| 100.000	| 66.250 |

I remember being surprised how Spain became a lighter yellow color around year 1997 when viewing the map animation. I am curious what drove the laws in this country to change and if it influenced other European countries in changing their laws.

##### Q6. What is the average length of paid maternity leave over time for each region? And paid paternity leave?
This data table includes current data (2022) and lists the average length of paid maternity leave and paid paternity leave by region. The output file is saved as 6_Avg_Mat_Pat_Leave_By_Region_2022.csv. The variance in averages in this table seems very large. Oceania has an average of 31.5 and all other regions have an average of more than 90 days. The length of paid paternity leave is very small for all regions, with Europe having the greatest average value of 20.575.

| ISO_region | Length of Maternity Leave | Length of Paternity Leave |
|------------|---------------------------|---------------------------|
| Africa |	90.09	| 2.56 |
| Americas	| 93.37	| 3.83 |
| Asia	| 98.69	| 4.15 |
| Europe	| 157.20	| 20.58 |
| Oceania	| 31.50	| 1.83 |

These two line charts show how this data has changed over time by region. The chart showing average length of paid maternity leave is saved as 6_Avg_Mat_Leave_By_Region.jpg and the chart showing average length of paid paternity leave is saved as 6_Avg_Pat_Leave_By_Region.jpg. 

The chart displaying average length of maternity leave shows there appears to be three tiers of regions: Europe has the most paid maternity leave, Asia, the Americas and Africa have similar average lengths of leave, and Oceania has the least.

![image](https://user-images.githubusercontent.com/117952432/206100778-f7aa3785-96a6-44b6-86ea-bf072cb1b197.png)

The chart showing the average length of paid paternity leave shows that this really hasn’t become a thing until the 2000s and then only in Europe. Other regions are slowly making small changes in just recent years.

![image](https://user-images.githubusercontent.com/117952432/206100808-2500781c-f614-475a-93ac-0fc608529ba2.png)

##### Q7. How does the WBL Index relate to the percent of national parliamentary seats held by women in a country?

This plot shows the average percent of national parliamentary seats held by women of the 22 years of data. (This supplemental dataset was not complete for the same years as in the WBL Index dataset.) The pattern shown in this chart seems familiar with Europe on the top of the line chart followed by the Americas. The output file is saved as 7_Avg_Parl_Seats_By_Region_Over_Time.jpg.

![image](https://user-images.githubusercontent.com/117952432/206100871-0d21d4a0-7312-4a9a-b22d-26daf24767b2.png)

After merging the supplemental dataset with WBL Index data, I produced a correlation table for the merged dataset. This file is saved as 7_Corr_PercentWomen_Parl.csv. It shows that there is a 0.529 correlation between the percent of women in parliamentary seats and the WBL index.

I created a scatterplot of the relationship between the percent of parliamentary seats held by women and the WBL Index for each year and country’s data in the merged dataset.  Plots are colored by region and the output file is saved as 7_Percent_Parl_Seats_And_Index.jpg. There seems to be slightly more cohesion in the purple plots representing Europe, while Asia and Africa plots are scattered all over the graph. I found it interesting to see the plots with the highest percent of parliamentary seats held by women are in Africa, while the plots with the highest WBL Index are in Europe. (Remember that this chart is not the average for each region, but each individual county’s data plots.)

![image](https://user-images.githubusercontent.com/117952432/206100932-a3c767aa-5944-4307-b05d-2df1425230b9.png)

Because I was interested in how the relationship with these two variables displayed within each region, I created a series of dual-axis line charts. The first axis has the average percent of parliamentary seats held by women and the second axis has the average WBL Index. Each region is displayed on a separate chart. Output files are saved as 7_Avg_Parl_Index_Africa.jpg, 7_Avg_Parl_Index_Americas.jpg, 7_Avg_Parl_Index_Asia.jpg, 7_Avg_Parl_Index_Europe.jpg and 7_Avg_Parl_Index_Oceania.jpg. It was fascinating seeing how these dual-axis line charts show that the slope of the two lines are very similar in chart—even down to the little divot in the early 2000s in the Oceania region.

![image](https://user-images.githubusercontent.com/117952432/206100961-d52ef60c-79b5-473b-923c-09d4d35bf967.png)

![image](https://user-images.githubusercontent.com/117952432/206100975-25a802c3-19c0-4f55-aea9-2cb823ded6f7.png)

![image](https://user-images.githubusercontent.com/117952432/206100995-64390c3e-cb0c-4c4f-ab34-a4a913c90d49.png)

![image](https://user-images.githubusercontent.com/117952432/206101011-d5f9d04f-464b-4011-abb3-dfefb941491f.png)

![image](https://user-images.githubusercontent.com/117952432/206101056-c06f7579-aa54-4e18-988d-b12d692970c4.png)


##### Q8. How does the WBL Index relate to the ratio of female to male labor force participation rate (%)?

This plot shows the average ratio of women to men in the labor force as a percent figure by region for more than 30 years of data. (This supplemental dataset was not complete for the same years as in the WBL Index dataset.) Again, Europe is the top of the line in the chart. I found it interesting that you can see the impacts of COVID in the Americas data line—when millions of women withdrew from their employment because of the lack of childcare. The output file is saved as 8_Avg_Ratio_Women_Labor_By_Region.jpg.

![image](https://user-images.githubusercontent.com/117952432/206101123-dba791b2-9039-4b2b-b9f5-bceb54c92944.png)

I created a scatterplot of the relationship between the ratio of women to men in the labor force and the WBL Index for each year and country’s data in the merged dataset. Plots are colored by region. This chart was difficult to read, however, and appeared quite blurred, so I tried making the same chart with just 2021 data. This output file is saved as 8_Ratio_Women_Labor_And_Index_2021.jpg. Again the Asia and Africa plots are scattered all over the graph and I am interested in the variation within these regions. 

![image](https://user-images.githubusercontent.com/117952432/206101165-898de779-bfee-402c-a2be-7a80d6a56a74.png)

I investigated the patterns within each region by again creating a series of dual-axis line charts. The first axis has the average ratio of women to men in the labor force as a percentage and the second axis has the average WBL Index. Each region is displayed on a separate chart. Output files are saved as 8_Avg_Ratio_Women_Labor_Index_Africa.jpg, 8_Avg_ Ratio_Women_Labor_Index_Americas.jpg, 8_Avg_ Ratio_Women_Labor_Index_Asia.jpg, 8_Avg_ Ratio_Women_Labor_Index_Europe.jpg and 8_Avg_ Ratio_Women_Labor_Index_Oceania.jpg. I found it interesting that these charts did not appear to show a similar change in trend line with the two variables. As the WBL Index rises in each region, the percent of women in the labor force doesn’t appear to increase at the same rate.

![image](https://user-images.githubusercontent.com/117952432/206101227-d2577679-89a3-4aa8-910c-6a599ec29bf0.png)

![image](https://user-images.githubusercontent.com/117952432/206101238-899bf170-7120-4cae-8505-63a8cc84bd4f.png)

![image](https://user-images.githubusercontent.com/117952432/206101254-883c4236-17fc-44c1-bc75-f947895e2bed.png)

![image](https://user-images.githubusercontent.com/117952432/206101262-ca41f74c-8458-40b3-8acd-719fdc9cfad5.png)

![image](https://user-images.githubusercontent.com/117952432/206101280-7ca22b76-7f88-45fa-a382-d21dc9540b49.png)


##### Q9. How does the ratio of women to men in the labor force relate to the Workplace subindex? To the Pay subindex? To the Parenthood subindex?

Because I didn’t find a similar pattern in the WBL Index data when examining the ratio of women to men in the labor force, I was curious if using one of the subindices would help coax out any findings. Again, I created a series of dual-axis line charts, but this time the first axis has the average ratio of women to men in the labor force as a percentage and the second axis has the average Workplace subindex score for each region. Output files are saved as 9_Avg_Ratio_Women_Labor_WorkSubindex_Africa.jpg, 9_Avg_Ratio_Women_Labor_WorkSubindex_Americas.jpg, 9_Avg_Ratio_Women_Labor_WorkSubindex_Asia.jpg, 9_Avg_Ratio_Women_Labor_WorkSubindex_Europe.jpg, and 9_Avg_Ratio_Women_Labor_WorkSubindex_Oceania.jpg. This series of line charts actually revealed even less similarly between the two variables.

![image](https://user-images.githubusercontent.com/117952432/206101359-23549f74-ec3d-437b-9149-f91b7ab08812.png)

![image](https://user-images.githubusercontent.com/117952432/206101371-ad2a173c-9a18-43a2-bae5-b40f05551fc2.png)

![image](https://user-images.githubusercontent.com/117952432/206101394-024c9375-ad8c-4917-a4f4-5bba2c960c1f.png)

![image](https://user-images.githubusercontent.com/117952432/206101410-1bf54b69-982d-4721-b362-9f2921964f80.png)

![image](https://user-images.githubusercontent.com/117952432/206101436-7a245f9b-2dcd-4d0f-bf86-5948ae4f4780.png)

So, I tried doing the same series of charts with the Pay subindex. Output files are saved as 9_Avg_Ratio_Women_Labor_PaySubindex_Africa.jpg, 9_Avg_Ratio_Women_Labor_PaySubindex_Americas.jpg, 9_Avg_Ratio_Women_Labor_PaySubindex_Asia.jpg, 9_Avg_Ratio_Women_Labor_PaySubindex_Europe.jpg, and 9_Avg_Ratio_Women_Labor_PaySubindex_Oceania.jpg. This series of charts also did not show a similar change in curve for the two variables with the exception of the Americas. I wonder if this could have something to do with the cost of childcare. As women are paid more for their work, they are able to afford childcare and enter the labor force. However, this is just my speculation and is only based on my knowledge of childcare in the US.

![image](https://user-images.githubusercontent.com/117952432/206101485-2d107db9-525d-473c-9b45-7f8f67eafaa7.png)

![image](https://user-images.githubusercontent.com/117952432/206101504-dbe1525c-6825-4279-80b8-8b39229ae345.png)

![image](https://user-images.githubusercontent.com/117952432/206101519-7c84a275-7fa8-4fbf-a630-b05179ad61ac.png)

![image](https://user-images.githubusercontent.com/117952432/206101538-0e1b4c6e-3683-4cd2-8e07-e3f0efb443c5.png)

![image](https://user-images.githubusercontent.com/117952432/206101553-a0f94be5-935d-4b19-a98c-9b078215d570.png)

And finally, I recreated the same series of charts using the Parenthood subindex. Output files are saved as 9_Avg_Ratio_Women_Labor_ParentSubindex_Africa.jpg, 9_Avg_Ratio_Women_Labor_ParentSubindex_Americas.jpg, 9_Avg_Ratio_Women_Labor_ParentSubindex_Asia.jpg, 9_Avg_Ratio_Women_Labor_ParentSubindex_Europe.jpg, and 9_Avg_Ratio_Women_Labor_ParentSubindex_Oceania.jpg. This series appears to have some similarity in the two variables for the Americas region, but the other regions don’t share much similarity and the European region especially appears to have different curves for each variable. When viewing this, I started to wonder if the Europe region charts tell us that women in this region have reached the percent of women in the workforce that will be realized. Although the average WBL Index and subindices rise year after year in this region, the ratio of women to men in the labor force appears to be rather flat. 

![image](https://user-images.githubusercontent.com/117952432/206101613-f0da6f10-b931-4f64-8ed3-50aa69a4680a.png)

![image](https://user-images.githubusercontent.com/117952432/206101622-855942bc-338e-4050-9b7e-d255bd2a8d3e.png)

![image](https://user-images.githubusercontent.com/117952432/206101643-51573ae8-a58a-40f1-8f4c-fe1df29f18d0.png)

![image](https://user-images.githubusercontent.com/117952432/206101663-b7e6358e-a89d-4d32-aadc-6dfc2c189a66.png)

![image](https://user-images.githubusercontent.com/117952432/206101688-46793db5-3140-4302-9b3a-a277a31a2cba.png)


##### Q10. How does childhood mortality relate to the Parenthood subindex?

This plot shows the average of children that live past age five by region for more than 30 years of data. (This supplemental dataset was not complete for the same years as in the WBL Index dataset.) Again, Europe is the top of the line in the chart. I am curious what accounts for the divot in the Americas around year 2010, but don’t recall what the cause might be. The output file is saved as 10_Avg_Child_Mortality_By_Region.jpg. The inverted version of this chart is saved as 10_Avg_Child_Life_By_Region.jpg.

![image](https://user-images.githubusercontent.com/117952432/206101780-615b80a1-2c4a-48da-82ae-83d0430a9daf.png)

![image](https://user-images.githubusercontent.com/117952432/206101804-37920846-c0a5-4fc0-99d3-23adaa75ecda.png)

Again, I examined the patterns within each region by creating a series of dual-axis line charts. The first axis has the average percent of children that live past age five and the second axis has the average Parenthood subindex. Each region is displayed on a separate chart. Output files are saved as 10_Avg_Child_Live_Parent_Africa.jpg, 10_Avg_Child_Live_Parent_Americas.jpg, 10_Avg_Child_Live_Parent_Asia.jpg, 10_Avg_Child_Live_Parent_Europe.jpg, and 10_Avg_Child_Live_Parent_Oceania.jpg. These two variables do appear to have a similar slope in the dual-axis line charts—especially in the Americas, Asia and Oceania regions.

![image](https://user-images.githubusercontent.com/117952432/206101847-93695800-41c6-4eb1-9404-8c9d30225cdc.png)

![image](https://user-images.githubusercontent.com/117952432/206101873-b3d2caf1-57c5-496e-bf7f-ae91c1656a73.png)

![image](https://user-images.githubusercontent.com/117952432/206101890-cd32b61a-61a6-4a12-840b-f1c4ec94ef31.png)

![image](https://user-images.githubusercontent.com/117952432/206101912-e2171045-87e2-46dd-87de-a7ffb010e2c7.png)

![image](https://user-images.githubusercontent.com/117952432/206101934-f6eae573-1560-43e2-b2d0-d8cf546fa8b8.png)


##### Q11. How does gross national income per capita relate to the WBL Index? To the Pay subindex?

This plot shows the average of gross national income per capital by region for more than 25 years of data. (This supplemental dataset was not complete for the same years as in the WBL Index dataset.) Again, Europe is the top of the line in the chart. The Americas, Asia, and Oceania all appear in a similar range, and the line representing the Africa region is at the bottom of the chart and does not have the same fluctuation over time seen in the other regions. The output file is saved as 11_Avg_GNI_By_Region.jpg.

![image](https://user-images.githubusercontent.com/117952432/206102028-ed1d3585-e425-4e46-ab4d-4efa67db2f28.png)

The correlation table with gross national income per capita data and WBL Index data shoes a correlation of 0.420574 between GNI and the WBL Index, and a correlation of 0.365168. This doesn’t sound like a very strong correlation, but I decided to see what regional charts would reveal for the GNI variable and WBL Index. 

The patterns show on these dual-axis region charts show that overall, as the WBL Index increases, the GNI also increases, however, there are some adjustments up and down along the way. Output files are saved as 11_Avg_GNI_Index_Africa.jpg, 11_Avg_GNI_Index_Americas.jpg, 11_Avg_GNI_Index_Asia.jpg, 11_Avg_GNI_Index_Europe.jpg, and 11_Avg_GNI_Index_Oceania.jpg.

![image](https://user-images.githubusercontent.com/117952432/206102108-419eef2e-69a5-41d4-be3c-8da096c32b3c.png)

![image](https://user-images.githubusercontent.com/117952432/206102120-4c642ef2-19d3-465e-801d-9b13914d3304.png)

![image](https://user-images.githubusercontent.com/117952432/206102141-a137a0a7-9130-4553-9dfd-41f77d45646f.png)

![image](https://user-images.githubusercontent.com/117952432/206102155-5b7f6cdc-23e3-4b40-ad57-7986ea93f43a.png)

![image](https://user-images.githubusercontent.com/117952432/206102177-c6b9c031-9578-48b7-aa97-aaacb05d598c.png)

I then created the same series of dual-axis charts but compared GNI with the Pay subindex. The most interesting region in this series of charts was the Europe region. The two lines appear to mimic each other’s shape over time, which was especially interesting as there was quite a bit of movement in the lines. Output files are saved as 11_Avg_GNI_Pay_Africa.jpg, 11_Avg_GNI_Pay_Americas.jpg, 11_Avg_GNI_Pay_Asia.jpg, 11_Avg_GNI_Pay_Europe.jpg, and 11_Avg_GNI_Pay_Oceania.jpg.

![image](https://user-images.githubusercontent.com/117952432/206102231-28086779-33aa-4128-8770-4593be182c6b.png)

![image](https://user-images.githubusercontent.com/117952432/206102253-75798c32-6e73-49b8-9480-f2588f1eebe1.png)

![image](https://user-images.githubusercontent.com/117952432/206102267-6fa30813-ad74-4693-b46b-c409a22dc6d8.png)

![image](https://user-images.githubusercontent.com/117952432/206102300-36e831b5-5fdd-46d7-87bc-3b186074d336.png)

![image](https://user-images.githubusercontent.com/117952432/206102313-9d13d3f8-aef3-49e6-b52d-d9bc1ff88d41.png)

### VI. Conclusion and Remaining Questions
Ultimately, I believe this data is a reflection of both policy and culture. Several times during my research I was curious why a certain pattern emerged (for instance the prominence of the Marriage laws in Oceania) and I wondered if it was a reflection of a particular cultural value. If I had a greater knowledge of world cultures, further insights might have been able to be gleaned from this research. However, many interesting observations were still able to be made. Information described in the Output Files and Initial Findings section detail many of my conclusions, but broad themes found in my research are also listed below.

Europe appears to generally have the most laws regarding women’s equality and has had for the last 50 years. This region was consistently at the top of my charts. They also had a lower standard deviation meaning there is less variation of laws between countries. I wonder how much of this lower standard deviation scores are driven by European Union membership. Did the EU spur increased alignment of laws regarding women?

Asia has the most variation in laws (the highest standard deviation) and has the lowest cumulative WBL Index score. If I had more time, I would be curious to do more investigation of the various subregions within Asia. As mentioned in the initial findings section, some subregions within Asia may be comparable to parts of Europe.

The parenthood subindex was an interesting area that I wish I could investigate further. The highest income group has the most variation in laws regarding parenthood. From my bar chart showing the average subindices by region, I know that parenthood has the lowest subindices score in all regions except for Europe. With additional time I would have been interested to see how individual countries within this high income group stack up against each other.

Africa, the Americas, and Asia have similar maternity leave now compared to what Europe had 40 years ago. I’m curious if it will take another 40 years for these regions of the world to reach comparable maternity leave policies as Europe. Paid paternity leave really didn’t register in most countries until 2000, and then only in Europe. Will paid paternity leave have a quicker rate of growth in the remaining regions over the next few decades? What patterns will emerge in Oceania—a region with a very low length of maternity leave, but very strong marriage equality laws?

Some countries in Africa have the highest percent of parliamentary seats held by women, however, as a region, Europe has the highest average. I am curious to find out more information about these African countries that have a high number of seats held by women. What encouraged women to move into these seats? What structures were in place for them to be elected?

The percent of women in parliament and the WBL Index appears to change in a very similar way. I was surprised that I didn’t find that one variable would lead the other in terms of timing, but the changes appeared to be in lock step over time. Does this mean public pressure is changing both occurrences in concert?

The percent of children that live past age 5 and the parenthood subindex seem to have similar curves over time by region. And, the average gross national income per capita and the pay subindex seem to have similar curves over time by region.

I could have spent many more months working with this dataset and finding new views to examine the data. One area of data that wasn’t included in my research is childcare. I think this is a topic that may lead to some interesting insights if combined with the datasets I had available. With more time, I would have tried to find some supplemental data to use in this area. Another area that would be interesting to examine is education levels. I would have liked to include some data about women’s educational attainment to compare with these datasets.

#### FURTHER LIMITATIONS OF THE STUDY
None of the analysis in this project was intended to capture causation, and this can’t be asserted by any of the findings.
