# Exploring-Migration-Trends-Through-Data-Analysis-and-Visualization
This study analyzes the history of human migration from 2000- 2014 from data to get insights on the migration dynamics
Human migration refers to any movement of people between locations, often across
long distances or in huge groups. It is known that throughout prehistory and human
history, humans have migrated widely. Human migration is the movement by people
from one place to another, particularly different countries, with the intention of settling
temporarily or permanently in the new location. It typically involves movements over
long distances and from one country or region to another.Human migration has
occurred throughout history and under a wide range of conditions. Tribal, national,
class, and individual levels have all been involved. Climate change, politics, the
economy, religion, or a simple desire for adventure have all been factors for migration.
Migrations are the essence of inhabiting the world and they are believed to have begun
approximately 2 million years ago with the early expansions out of Africa by Homo
erectus.
In more modern times, migrations have often been driven by necessity, that could
include forced displacement (in various forms such as deportation, slave trade,
trafficking in human beings) and flight (war refugees, ethnic cleansing).
This study analyzes the history of human migration from 2000- 2014 from data to get
insights on the migration dynamics and attempts to answer the following questions:
1. What are the major flows of migration (meaning from where to where) ?
2. Where people from the more developed regions are migrating to ?
3. Where are people from the less developed regions are migrating to ?
4. What are the dynamics by income and geographic region ?
5. What are the migration patterns in India over the years ?

# Dataset Description
The dataset used in this study was from United Nation migration data.
● The data is a collection of 289 columns and there are 2733 rows.
● There are 51 columns with data type as float and 238 columns with data type as
object.
● There are many rows as the migration data contains data of every 5 years from
1990 to 2019 of every country and region defined by the United Nations. Dataset
has more developed regions and least developed countries where according to
the UN more developed regions comprise Europe, Northern America, Australia,
New Zealand, and Japan whereas group of least developed countries, as
defined by the United Nations General Assembly, currently comprises 47
countries: Afghanistan, Angola, Bangladesh, Benin, Bhutan, Burkina Faso,
Burundi, Cambodia, Central African Republic, Chad, Comoros, Democratic
Republic of the Congo, Djibouti, Eritrea, Ethiopia, Gambia, Guinea,
Guinea-Bissau, Haiti, Kiribati, Lao People’s Democratic Republic, Lesotho,
Liberia, Madagascar, Malawi, Mali, Mauritania, Mozambique, Myanmar, Nepal,
Niger, Rwanda, São Tomé and Príncipe, Senegal, Sierra Leone, Solomon
Islands, Somalia, South Sudan, Sudan, Timor-Leste, Togo, Tuvalu, Uganda,
United Republic of Tanzania, Vanuatu, Yemen and Zambia.
● There are rows with migrants' destinations to income based regions where
income level is based on June 2018 Gross National Income per capita from the
World Bank.

## Dataset Preparation
1. The dataset UN_Migrations.csv was loaded into a dataframe using the pandas
library in python and was stored in variable df.
2. The variables in dataset were :- Year, Sort order, Major area, region, country or
area of destination, Notes, Code, Type of data (a), Unnamed:6, Unnamed:7,
Unnamed:8, Country or area of origin, Unnamed:10, Unnamed:11,.....….,
Unnamed:288.
3. As noticed there were many columns with unnamed names because the origin
countries names were stored in 2 rows, so again the data frame was opened by
passing parameter skiprows to skip the first row and all origin countries names
were retrieved.
4. The dataset contained values like NaN, "..", and "-." As a result, these values
were changed to 0.
5. The following variables were dropped from dataframe as they were not required
in analysis :
5.1. Sort order
5.2. Notes
5.3. Code
5.4. Type of data (a)
5.5. Other South
5.6. Other North
6. The column with name as Major area, region, country or area of destination was
renamed Destination for ease of future use.
7. Also, there was one duplicate column detected in visualization with the same
name and data with a different case which was NORTHERN AMERICA was then
dropped.
8. Columns with migrant data figures were in string type for analysis migrant was
converted to float
