
# coding: utf-8

# In[4]:

#load Graphlab Create
import graphlab


# In[6]:

#load housing sales data
sales = graphlab.SFrame('C:/Users/root/Documents/GitHub/Python-Scripts/ML1/home_data.gl/')





# In[7]:

sales


# In[8]:

###Explore data for housing sales
graphlab.canvas.set_target('ipynb')
sales.show(view="Scatter Plot", x="sqft_living", y="price")




# In[9]:

#Creation of regression model sqft_living to price
train_data,test_data = sales.random_split(.8,seed=0)


# In[10]:

#Build regression model
sqft_model = graphlab.linear_regression.create(train_data, target='price', features=['sqft_living'])


# In[11]:

print test_data['price'].mean()


# In[12]:

print sqft_model.evaluate(test_data)


# In[14]:

#Illustrate predictions
import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')
plt.plot(test_data['sqft_living'], test_data['price'],'.',test_data['sqft_living'],sqft_model.predict(test_data),'-')


# In[15]:

sqft_model.get('coefficients')


# In[17]:

#Feature exploration within the dataset
myfeatures=['bedrooms', 'bathrooms','sqft_living','sqft_lot','floors','zipcode']
sales[myfeatures].show()


# In[18]:

sales.show(view='BoxWhisker Plot', x='zipcode', y='price')


# In[19]:

#Create regression model based on more features
myfeatures_model = graphlab.linear_regression.create(train_data,target='price', features=myfeatures)


# In[20]:

print myfeatures


# In[21]:

print sqft_model.evaluate(test_data)
print myfeatures_model.evaluate(test_data)


# In[24]:

#Apply models to predict prices on houses (3 houses)
house1 = sales[sales['id']=='5309101200']
house1


# In[25]:

<img src="house-5309101200.jpg">


# In[26]:

print house1['price']


# In[27]:

print sqft_model.predict(house1)


# In[31]:

#Prediction for house 2
house2 = sales[sales['id']=='1925069082']
print house2


# In[32]:

house2


# In[33]:

print sqft_model.predict(house2)


# In[35]:

print myfeatures_model.predict(house2)


# In[36]:

#Predict third house
bgates = {'bedrooms':[8], 
              'bathrooms':[25], 
              'sqft_living':[50000], 
              'sqft_lot':[225000],
              'floors':[4], 
              'zipcode':['98039'], 
              'condition':[10], 
              'grade':[10],
              'waterfront':[1],
              'view':[4],
              'sqft_above':[37500],
              'sqft_basement':[12500],
              'yr_built':[1994],
              'yr_renovated':[2010],
              'lat':[47.627606],
              'long':[-122.242054],
              'sqft_living15':[5000],
              'sqft_lot15':[40000]}


# In[39]:

print myfeatures_model.predict(graphlab.SFrame(bgates))


# In[ ]:



