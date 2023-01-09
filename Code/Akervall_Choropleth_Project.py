#Name of File: Akervall_Choropleth_Project.py
#Info: Plotly Animated Map of WBL Index
#Date created: 5/31/2022
#Written By: Kristin Akervall
#Create an animated choropleth map with plotly to display WBL Index over time
#
#Import necessary libraries
import pandas as pd
import numpy as np
import plotly
import plotly.express as px
#
#Use the same steps as used in the Jupyter notebook program to read in data and get it into indexdf format.
#
#Read the xlsx file and correct sheet in the file
data = pd.read_excel (r'C:\Users\krist\programska\Project\\WBL_19712022.xlsx', sheet_name='WBL Panel 2022')
#
#some columns are not necessary so I just read in what I need and put it in a dataframe
df = pd.DataFrame(data, columns = ['Economy', 'ISO Code', 'Region', 'Income Group', 'Report Year', 'WBL INDEX', 'MOBILITY', 'Can a woman choose where to live in the same way as a man?', 'Can a woman travel outside her home in the same way as a man?', 'Can a woman apply for a passport in the same way as a man?', 'Can a woman travel outside the country in the same way as a man?', 
                                   'WORKPLACE', 'Can a woman get a job in the same way as a man?', 'Does the law prohibit discrimination in employment based on gender?', 'Is there legislation on sexual harassment in employment?', 'Are there criminal penalties or civil remedies for sexual harassment in employment?', 
                                   'PAY', 'Does the law mandate equal remuneration for work of equal value?', 'Can a woman work at night in the same way as a man?', 'Can a woman work in a job deemed dangerous in the same way as a man?', 'Can a woman work in an industrial job in the same way as a man?',
                                   'MARRIAGE', 'Is there no legal provision that requires a married woman to obey her husband?', 'Can a woman be head of household in the same way as a man?', 'Is there legislation specifically addressing domestic violence?', 'Can a woman obtain a judgment of divorce in the same way as a man?', 'Does a woman have the same rights to remarry as a man?',
                                   'PARENTHOOD', 'Is paid leave of at least 14 weeks available to mothers?', 'Length of paid maternity leave', 'Does the government administer 100% of maternity leave benefits?', 'Is there paid leave available to fathers?', 'Length of paid paternity leave', 'Is there paid parental leave?', 'Shared days', 'Days for the mother', 'Days for the father', 'Is dismissal of pregnant workers prohibited?',
                                   'ENTREPRENEURSHIP', 'Does the law prohibit discrimination in access to credit based on gender?', 'Can a woman sign a contract in the same way as a man?', 'Can a woman register a business in the same way as a man?', 'Can a woman open a bank account in the same way as a man?',
                                   'ASSETS', 'Do men and women have equal ownership rights to immovable property?', 'Do sons and daughters have equal rights to inherit assets from their parents?', 'Do male and female surviving spouses have equal rights to inherit assets?', 'Does the law grant spouses equal administrative authority over assets during marriage?', 'Does the law provide for the valuation of nonmonetary contributions?',
                                   'PENSION', 'Is the age at which men and women can retire with full pension benefits the same?', 'Is the age at which men and women can retire with partial pension benefits the same?', 'Is the mandatory retirement age for men and women the same?', 'Are periods of absence due to childcare accounted for in pension benefits?'])
#
#Rename the columns so they are easier to work with.
df.columns=['country', 'ISO_code', 'region', 'income_group', 'year', 'INDEX', 'MOBILITY', 'choose_where_live', 'travel_outside_home', 'apply_passport', 'international_travel', 
                                   'WORKPLACE', 'job', 'emp_discr', 'leg_sex_harassment', 'penal_sex_harassment', 
                                   'PAY', 'equal_pay', 'work_night', 'danger_job', 'indust_job',
                                   'MARRIAGE', 'obey_husband', 'head_household', 'dom_violence', 'divorce', 'remarry',
                                   'PARENTHOOD', '14_wk_leave', 'length_mat_leave', 'leave_benefit', 'paternal_leave', 'length_pat_leave', 'pat_paid', 'shared_days', 'mat_days', 'pat_days', 'pregnant',
                                   'ENTRE', 'credit', 'contract', 'register_bus', 'bank_account',
                                   'ASSETS', 'prop_owner', 'daught_inherit', 'spouses_inherit', 'admin_autho_assets', 'value_nonmon_cont',
                                   'PENSION', 'retire_age', 'retire_partial', 'mandatory_age', 'childcare_accounted']
#
#Add an ID column to my main data because I like to have unique ID in my original data.
df.insert(0,'ID', range(1,1+len(df))) #Let the ID numbering start at 1 and continue for the length of the dataset.
#
#Change the ID to string
df['ID'] = df['ID'].map(str)
#
#read csv file for ISO region codes
data2 = pd.read_csv(r'C:\Users\krist\programska\Project\ISO_3166_Countries_With_Regional_Codes.csv')
#
#put data in dataframe
regiondf = pd.DataFrame(data2)
#
#trim down to just what I need for analysis
regiondf=regiondf[['name', 'alpha-3', 'region', 'sub-region', 'intermediate-region']]
#
#rename ISO region columns for clarity
regiondf.columns=['ISO_country', 'ISO_code', 'ISO_region', 'ISO_subregion', 'ISO_intermed']
#
#Add the ISO region data to my main dataset
newdf = pd.merge(df, regiondf, how='left', on=['ISO_code']) # left join and link on ISO_code
#
#Create new dataframe that just has the index summaries
indexdf = newdf[['country', 'ISO_code', 'ISO_region', 'ISO_subregion', 'ISO_intermed', 'region', 'income_group', 'year', 'INDEX', 'MOBILITY', 'WORKPLACE', 'PAY', 'MARRIAGE', 'PARENTHOOD', 'ENTRE', 'ASSETS', 'PENSION']]
#
#What does a choropleth map of the WBL Index look like?
#create figure for the data, color will be the WBL Index, animation will happen on year
figure = px.choropleth(indexdf, locations='ISO_code', color='INDEX', hover_name='country', animation_frame='year', color_continuous_scale = px.colors.sequential.Plasma, projection='natural earth')
figure.show()
