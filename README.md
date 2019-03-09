# Road_Damage_Detection__Accelerometer_Data
Severity of damage in roads is really important for taking right measures to fix it. A road can be deemed bad for several reasons
* Potholes
* Uneven coverage of old potholes with cement or road tar mixture
* Muddy and rocky settlement on the road

## Data Collection
Data was collected by us on our own. We used the app *sensor labs* which lets you access your mobile’s sensors and then has the option to record and export the recorded data in csv.  We used the recorded data from *accelerometer*.

An accelerometer is an electromechanical device used to measure acceleration forces. The *piezoelectric effect* is the most common form of accelerometer and uses microscopic crystal structures that become stressed due to accelerative forces. These crystals create a voltage from the stress, and the accelerometer interprets the voltage to determine velocity and orientation.

Typical accelerometers are made up of multiple axes, two to determine most two-dimensional movement with the option of a third for 3D positioning. Most smartphones typically make use of three-axis models, and thus smartphone accelerometer is the smart choice as it will help you measure the sudden jerks and movement changes in one of these 3 axis.

We collected the data while riding a bike, we kept the bike speed constant at 30 m/s. We roamed in and around Electronic City,  Bangalore.  The dataset contains signal data from 14 different roads like ISBR road, Wipro village road, BSNL road etc.  To rank the roads, we used a scoring scale from 0 to 10 with 0 being the worst road and 10 being the best. Scores were assigned using the images we took for each road and the bike riding experience.

/*Collecting your own data is fun, try it sometimes :)*/

## Approach
We need to identify sudden changes in the x, y and z axis of the accelerometers to identify bumps and potholes on the roads. 

We can take magnitude of all the axis for a better insight and trim out the length of the signal to a standard length. * We then remove the gravitational acceleration from our data by removing the average. This should work as ‘g’ is constant. We then apply a moving average filter to smoothen out the signal. This helps us identify the peaks easily as it will remove erroneous fluctuations. 
After calculating the moving average values, we will observe some peaks in the signal data. 

We will then set a threshold level which is our reference point for peak detection. Any data point above this threshold value would be considered a pothole/broken road etc, meaning bad road conditions. This threshold value is max/2 and min/2 . Any value more than max/2 and less than min/2 are labeled as perfect peaks which will help us rank the roads based on the damage. 

Depending on the number of peak values which are above our threshold, we’ll rank our roads. We see that the peak distribution plot is very similar to the inverse of our road ranks (because the better the rank, the better the road) 

So what we infer is that accelerometer data can properly capture the disturbances in the roads. 

The threshold level and peak-count value to ranking can be adjusted to match the labels we assigned to our raw data but adjusting these values manually isn’t a very intelligent way of analyzing signals, so we’ll let a ML model like linear regression do it. 

## Training
We split our data into train and test data. The data contains name of the road and the corresponding rank. We use a basic regression model like LinearRegression to predict road ranks with the help of peak counts. On training, we get a **logarithmic loss of around 0.56**, which is actually pretty decent given the mode of data collection. 







