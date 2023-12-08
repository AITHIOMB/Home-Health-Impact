# Model Result Progress Notes

*these attempts were done with numerical categorical columns for state & city
*Only done on x input data predicting 'brainfog' symptom

Other Models to try
- SVM
- Random Forest 
- GBM 
- Neural Network 

# 1. SVC Molds 
Less than 60% Accuracy between all location and mold combos & 70-90% variance
## With Location 
- PCA done with numerical category locations
- PCA scale not adjusted
- non specified Hyperparameter
![Alt text](image-1.png)

    Results
- 90% variance {'C': 1, 'gamma': 0.1, 'kernel': 'rbf'}: 56%
![Alt text](image-5.png)
- 80% variance {'C': 1, 'gamma': 'scale', 'kernel': 'rbf'}: 56% accuracy 

## Without Location
- Depending on the results of this, we will determine if location matters, if so, we will do new PCA with adjustments 
Results
- 44% still bad, try a new model and check in with swagath over results
![Alt text](image-2.png)
Research Notes
- I need to use a non linear kernel since I did not see a linear trend 
- kernel options to try: polynomial, Radial, Sigmoid
- 'rbf' and 'poly' kernels work best 

# 2. Random Forest Mold
Less than 60% Accuracy between all location and mold combos & 70-90% variance 
## With Location
Inital Results
- 50% - 55% Accuracy
![Alt text](image-4.png)

Results with Hyperparameter tuning:
![Alt text](image-6.png)
Best Accuracy: 0.5895104895104895 <br>
Best parameters found: {'max_depth': 30, <br>
'min_samples_leaf': 2, <br> 
'min_samples_split': 5,<br>
 'n_estimators': 200}<br>
Confusion Matrix with Best Estimator:<br>
[[42 28]<br>
 [50 46]]

 Honing more in on n_estimator parameters, testing more 
 ![Alt text](image-7.png)
 odd, it went down but went back up when it raised, trying again

 it stays around 50s 

 Raising n_estimators: 
 200,500,1000 seems to go up? random all stays under 60%, around 50 - 58% range 

 Evaluating depth
seems to not have a consistent difference in performance. Pattern seems random 

Seems to not be a very fruitful model. Going to try out more



    
## Without Location
Results
- 50 - 54% Accuracy
- really not much difference between the two
![Alt text](image-3.png)

# 3. CNN 

# 4. GBM

