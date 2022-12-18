# Importing all necessary library
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
sns.set_theme()
from pandas_profiling import ProfileReport

# Opening the UN Migration CSV File
df = pd.read_csv("UN_Migrations.csv")

# Getting details of our dataframe
print("----The details of dataframe----\n")
print("The first 5 rows of our dataframe :\n",df.head(5))
print("The last 5 rows of our dataframe :\n",df.tail(5))
print("Statistical data of our dataframe :\n",df.describe())

# Getting all columns names in colNames variable as header column first 6 names of column and the remaining names of column
# where in second row
colNames = df.columns.tolist()

# Now opening the csv by skipping header as it does not contain country names but this remove first 6 column's name
df = pd.read_csv("UN_Migrations.csv",skiprows=1)

# Removing all columns and all rows filled with NaN values
df = df.dropna(axis=1,how='all')
df = df.dropna(axis=0,how='all')

# Replacing all nan and '..', '-' with 0
df.replace(to_replace = '..', value = 0, inplace = True)
df.replace(to_replace = '-', value = 0, inplace = True)
df=df.fillna(0)

# Now getting all names of columns of our dataframe which has country names in countryNames variable
countryNames = df.columns.tolist()

# When skiping the header first 6 names of columns where unnamed, so replacing the first 6 names of coulmns
countryNames[0:6] = colNames[0:6]

# Now renaming the all columns with all names stored in our countryNames variable list
for j in range(len(df.columns)):
    old = df.columns[j]
    newNames = countryNames[j]
    df = df.rename(columns = {old:newNames})

# Dropping columns which will be not needed for our analysis
df = df.drop(columns=['Sort\norder', 'Notes','Code','Type of data (a)', 'Other South','Other North'])

# Changing column name for ease of use in future
df.rename(columns={'Major area, region, country or area of destination': 'Destination'}, inplace=True)

# It was noticed that data had two duplicate columns with different names so one was dropped
df.drop(df[(df['Destination'] == "NORTHERN AMERICA")].index,inplace=True)

# Changing data type of every column from object to float
allCols = df.columns.tolist()
allCols.remove('Destination')
for name in allCols:
    df[name] = df[name].astype('str')
    df[name] = df[name].apply(lambda x: x.replace(',', ''))
    df[name] = df[name].astype(float)

# Creating profile report for our data frame

# ----------------- Heatmap to analyze flow of people from where to where ---------------

# Creating dataframe to fit data for heatmap
dfHeatmap = df.melt(id_vars=['Year', 'Destination', 'Total'],var_name="Origin",\
                    value_name="Migrants").fillna(0).drop(columns='Total')

# This function plots flow of people from where to where with minmum migrants from their origin countries
def heatmap(dfHeatmap,minMigrants):
    dfMig = dfHeatmap[dfHeatmap.Migrants > minMigrants]
    migrantsDetails = dfMig.pivot_table(index='Origin', columns='Destination', values='Migrants', aggfunc='sum')
    f, ax = plt.subplots(figsize=(15,15))
    sns.heatmap(migrantsDetails, annot=True, fmt="f", linewidths=.5, ax=ax,annot_kws={'rotation':90})
    title = 'Migration of human population from origin to destination'
    plt.title(title,fontsize = 10)
    plt.xlabel('Destination', fontsize = 10)
    plt.ylabel('Origin', fontsize = 10)

# Calling the heatmap function different size of minimum migrants
heatmap(dfHeatmap,0)
heatmap(dfHeatmap,10000)
heatmap(dfHeatmap,100000)
heatmap(dfHeatmap,1000000)
heatmap(dfHeatmap,10000000)

# ----------------- Analysing flow of migration people from developed countries ---------------

# Preparing Dataframe to get insights on migration from developed countries
developedCountries = ["Germany","Denmark","Norway","Ireland","Switzerland","Sweden",\
                      "United States of America","Australia","New Zealand","Japan"]

# Created function modify dataframe which was created for heatmap
# Function takes parameter 'countries' take list of names of countries to analyze
# another parameter 'column' takes input in string to define which column to groupby in sorting the dataframe
def typeDf(countries,column):
    newDf = dfHeatmap.loc[dfHeatmap[column].isin(countries)]
    newDf = newDf.groupby([column])["Migrants"].sum().reset_index()
    return newDf

# Plotting bar chart for analysing migration pattern from developed countries
developedDf = typeDf(developedCountries,"Origin")
fig, ax = plt.subplots(figsize=(7,7))
x = developedDf["Origin"].tolist()
y = developedDf["Migrants"].tolist()
bar_colors = ['tab:green', 'tab:blue']

ax.bar( x,y,color=bar_colors)

ax.set_xlabel('Countries')
ax.set_ylabel('Number of Migrants')
ax.set_title('Migrants from developed countries')
plt.xticks(rotation = 90)
plt.show()

# ----------------- Analysing flow of migration people from developed countries ---------------

# Preparing Dataframe to get insights on migration from developed countries
developedCountries = ["Germany","Denmark","Norway","Ireland","Switzerland","Sweden",\
                      "United States of America","Australia","New Zealand","Japan"]

# Created function modify dataframe which was created for heatmap
# Function takes parameter 'countries' take list of names of countries to analyze
# another parameter 'column' takes input in string to define which column to groupby in sorting the dataframe
def typeDf(countries,column):
    newDf = dfHeatmap.loc[dfHeatmap[column].isin(countries)]
    newDf = newDf.groupby([column])["Migrants"].sum().reset_index()
    return newDf

# Plotting bar chart for analysing migration pattern from developed countries
developedDf = typeDf(developedCountries,"Origin")
fig, ax = plt.subplots(figsize=(7,7))
x = developedDf["Origin"].tolist()
y = developedDf["Migrants"].tolist()
bar_colors = ['tab:green', 'tab:blue']

ax.bar( x,y,color=bar_colors)

ax.set_xlabel('Countries')
ax.set_ylabel('Number of Migrants')
ax.set_title('Migrants from developed countries')
plt.xticks(rotation = 90)
plt.show()

# ----------------- Analysing flow of migration people from Least developed countries ---------------
# Less developed countries defined in info sheet of UN migration file
lessDeveloped = ['Afghanistan','Angola','Bangladesh','Benin','Bhutan','Burkina Faso','Burundi','Cambodia',
 'Central African Republic','Chad','Comoros','Democratic Republic of the Congo','Djibouti','Eritrea','Ethiopia',
 'Gambia','Guinea','Guinea-Bissau','Haiti','Kiribati','Lao People’s Democratic Republic','Lesotho','Liberia',
 'Madagascar','Malawi','Mali','Mauritania','Mozambique','Myanmar','Nepal','Niger','Rwanda','São Tomé and Príncipe','Senegal',
 'Sierra Leone','Solomon Islands','Somalia','South Sudan','Sudan','Timor-Leste','Togo','Tuvalu','Uganda',
 'United Republic of Tanzania','Vanuatu','Yemen','Zambia']

# Modifying dataframe for to plot least developed countries by calling the function created for modifying dataframe
lessDevelopedDf = typeDf(lessDeveloped,"Origin")

# Plotting bar chart for analysing migration pattern from least developed countries
fig, ax = plt.subplots(figsize=(30,20))
x = lessDevelopedDf["Origin"].tolist()
y = lessDevelopedDf["Migrants"].tolist()
bar_colors = ['tab:red', 'tab:grey']

ax.bar( x,y, color=bar_colors)

ax.set_xlabel('Countries',fontsize=30)
ax.set_ylabel('Number of Migrants',fontsize=30)
ax.set_title('Migrants from least developed countries',fontsize=30)
plt.xticks(rotation = 90,fontsize=20)
plt.yticks(fontsize=20)
plt.show()

# ----------------- Analysing flow of migration of people from countries based on income ---------------
countriesIncome = ['High-income countries','Middle-income countries','Upper-middle-income countries',\
                   'Lower-middle-income countries','Low-income countries']
incomeDf = typeDf(countriesIncome,"Destination")

# Creating function to plot piechart for migration based on income level countries and geographic region
# Function takes two parameter where dftype takes dataframe to visualize and chart param is to define title of chart
def piechart(dftype,chart = 'Income'):
    x = dftype.Destination.tolist()
    y = dftype.Migrants.tolist()

    # Creating explode data
    if chart == 'Income':
        explode = (0.05, 0.0, 0.0, 0.0, 0.0)
        colors = ( "orange", "cyan", "brown","grey", "beige")
    if chart == 'Geographic':
        explode = (0.0, 0.0, 0.1, 0.0, 0.0,0.0)
        colors = ( "orange", "cyan", "brown","grey", "beige","indigo")

    # Wedge properties
    wp = { 'linewidth' : 1, 'edgecolor' : "green" }

    # Creating autocpt arguments
    def func(pct, allvalues):
        absolute = int(pct / 100.*np.sum(allvalues))
        return "{:.1f}%\n({:d} g)".format(pct, absolute)

    # Creating plot
    fig, ax = plt.subplots(figsize =(10, 7))
    wedges, texts, autotexts = ax.pie(y,
                                      autopct = lambda pct: func(pct, y),
                                      explode = explode,
                                      labels = x,
                                      shadow = True,
                                      colors = colors,
                                      startangle = 90,
                                      wedgeprops = wp,
                                      textprops = dict(color ="black"))

    # Adding legend
    if chart == 'Income':
        ax.legend(wedges, x,title ="Contries based on Income",loc ="best",bbox_to_anchor =(1, 0, 0.5, 1))
        plt.setp(autotexts, size = 8, weight ="bold")
        ax.set_title("Migrants to countries based on income level")
    if chart == 'Geographic':
        ax.legend(wedges, x,title ="Contries based on Geographic area",loc ="best",bbox_to_anchor =(1, 0, 0.5, 1))
        plt.setp(autotexts, size = 8, weight ="bold")
        ax.set_title("Migrants to countries based on Geographic area")

    plt.show()

piechart(incomeDf,chart = 'Income')

# ----------------- Analysing flow of migration of people based on geographic area ---------------
geographicArea = ['Africa', 'Asia', 'Europe', 'Latin America and the Caribbean', 'Northern America', 'Oceania']
geographicDf = typeDf(geographicArea,"Destination")
piechart(geographicDf,chart = 'Geographic')

# -------------- Analyazing migration patterns in India --------------------

# Modifying dataframe where migrants destination was India in following year
indiaDf = dfHeatmap[dfHeatmap['Destination'] == 'India']
indiaDf = indiaDf.pivot(index='Origin', columns='Year', values='Migrants').reset_index()
indiaDf = indiaDf.sort_values(by = [1990.0, 1995.0, 2000.0, 2005.0, 2010.0, 2015.0, 2019.0], ascending =\
                              [False, False, False, False, False, False, False])
# Removing countries which have 0 migrants to India
indiaDf = indiaDf[(indiaDf[1990.0] > 0) & (indiaDf[1995.0] > 0) & (indiaDf[2000.0] > 0) & (indiaDf[2005.0] > 0)\
                  & (indiaDf[2010.0] > 0) & (indiaDf[2015.0] > 0) & (indiaDf[2019.0] > 0)]

# Creating function to plot grouped bar chart where qty parameter takes the most parameter to getting top 10 countries migrant to India
# Least will give top 10 countries with least migrants
def graphIndia(qty):
    if qty == "most":
        ax = indiaDf.head(10).plot(x='Origin',
                kind='bar',
                stacked=False,
                title="Top 10 Countries with most number of migrants to India",
                figsize=(10, 10))
        ax.set_ylabel("Number of Migrants")
    else:
        ax = indiaDf.tail(10).plot(x='Origin',
                kind='bar',
                stacked=False,
                title="Top 10 Countries with least number of migrants to India",
                figsize=(10, 10))
        ax.set_ylabel("Number of Migrants")

most = graphIndia("most")
least = graphIndia("least")

# Analyzing same information with different staked bar chart
def stackedIndia(qty):
    if qty == "most":
        category_names = indiaDf['Origin'].head(3).tolist()
        b = indiaDf.head(3)
    if qty == "least":
        category_names = indiaDf['Origin'].tail(3).tolist()
        b = indiaDf.tail(3)
    results = {
        '1990.0': b[1990.0].tolist(),
        '1995.0': b[2000.0].tolist(),
        '2005.0': b[2005.0].tolist(),
        '2010.0': b[2010.0].tolist(),
        '2015.0': b[2015.0].tolist(),
        '2019.0': b[2019.0].tolist()
    }


    def survey(results, category_names):

        labels = list(results.keys())
        data = np.array(list(results.values()))
        data_cum = data.cumsum(axis=1)
        category_colors = plt.colormaps['gist_ncar'](
            np.linspace(0.15, 0.85, data.shape[1]))

        fig, ax = plt.subplots(figsize=(9.2, 5))
        ax.invert_yaxis()
        ax.xaxis.set_visible(False)
        ax.set_xlim(0, np.sum(data, axis=1).max())
        plt.title("Migrants to India", loc='right')

        for i, (colname, color) in enumerate(zip(category_names, category_colors)):
            widths = data[:, i]
            starts = data_cum[:, i] - widths
            rects = ax.barh(labels, widths, left=starts, height=0.5,
                            label=colname, color=color)

            r, g, b, _ = color
            text_color = 'white' if r * g * b < 0.5 else 'darkgrey'
            ax.bar_label(rects, label_type='center', color=text_color)

        ax.legend(ncol=len(category_names), bbox_to_anchor=(0, 1),
                  loc='lower left', fontsize='small')

        return fig, ax


    survey(results, category_names)
    plt.show()

stackedMost = stackedIndia("most")
stakedLeast = stackedIndia("least")

print("\n --End of Analyzing--")