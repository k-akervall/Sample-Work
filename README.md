The World Bank’s
# Women, Business, and Law Index
# Analyzing the Presence of Laws Regarding Women in the Workplace, and Economic and Life Outcomes: A Global Inspection

![image](https://user-images.githubusercontent.com/117952432/202291058-c8c87360-7b26-4fe4-be23-1e88bca5384e.png)

Utilizing the World Bank’s Women, Business and the Law Index, along with a few supplemental datasets, I analyzed the presence of laws regarding women’s equality in the workplace and economic and life outcomes in different regions of the world.

Created by: Kristin Akervall, June 2022


MAIN DATA

WBL Index
The main dataset, Women, Business and the Law Index (WBL Index) consists of an Excel spreadsheet that contains information on the presence of gender equality laws for countries around the world in years 1971-2022. This 50+ years of data covers 190 countries in a dataset with 9880 rows and 55 columns. The data can be downloaded at https://wbl.worldbank.org/en/wbl-data.

The WBL Index score is calculated each year from eight subindices: Mobility, Workplace, Pay, Marriage, Parenthood, Entrepreneurship, Assets, and Pension. Each subindex, and the WBL Index itself, is on a scale of 0-100 depending on the coverage of laws in that specific area. This coverage is measured depending on the response to a list of questions for each subindex category. These questions, subindices, the WBL Index score and a few categorization labels for each country (ISO Code, Region, Income Group) create all the columns of the dataset. The fields are described below: (Field names were changed after uploading the file into python for brevity. New field name is in the FIELDS column below.)

