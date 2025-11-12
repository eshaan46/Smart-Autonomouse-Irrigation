# Libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
import joblib

# Variables
epochs = 50
i = 0

# Functions
def load_dataset(path):
    df = pd.read_csv(path)
    x = df.drop(['water_required_liters'],axis = 1).values
    y = df['water_required_liters'].values
    return x, y
def split_dataset(x,y,ts,rs):
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=ts, random_state=rs)
    return x_train, x_test, y_train, y_test
def model_train(model,x,y):
    model.fit(x,y)
    y_pred = model.predict(x)
    model_score = model.score(x,y)
    return y_pred, model_score
def model_evaluate(model,x,y):
    y_pred = model.predict(x)
    model_score = model.score(x,y)
    return y_pred, model_score
    
# Main
x,y = load_dataset('precision_irrigation_dataset.csv')
x_train, x_test, y_train, y_test = split_dataset(x,y,0.3,0)
model = GradientBoostingRegressor(random_state=0,warm_start=True,n_estimators=20,learning_rate=0.05)

y_train_pred, train_score = model_train(model,x_train,y_train)
print(f'Initial Train Score: {train_score}')

while i < epochs+1:
    model.n_estimators += 10
    #model.learning_rate += 0.001
    y_train_pred, train_score = model_train(model,x_train,y_train)
    print(f'Epoch: {i} | Train Score: {train_score}')
    i += 1

y_test_pred, test_score = model_evaluate(model,x_test,y_test)
print(f'Test Score: {test_score}') 
joblib.dump(model, 'sai_model.pkl')   