### The World Bank’s
# Women, Business, and Law Index
## Analyzing the Presence of Laws Regarding Women in the Workplace, and Economic and Life Outcomes: A Global Inspection

![image](https://user-images.githubusercontent.com/117952432/202291058-c8c87360-7b26-4fe4-be23-1e88bca5384e.png)

Utilizing the World Bank’s Women, Business and the Law Index, along with a few supplemental datasets, I analyzed the presence of laws regarding women’s equality in the workplace and economic and life outcomes in different regions of the world over time (1971-2022).

Created by: Kristin Akervall, June 2022


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

