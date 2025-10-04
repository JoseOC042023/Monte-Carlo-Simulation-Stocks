import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



File_Name = "APPL_GS_MSFT_CAT_5_Year_Close_Price_Data - Static Data.csv"
StockData = pd.read_csv(File_Name)
StockData = StockData.ffill()

StockHead = StockData.columns
N_firms = 4#len(StockHead)-1

date_column_name = StockHead[0]
target_date_str = '4/4/2025'
mask = (StockData[date_column_name] == target_date_str)
Start_2025_index= StockData[mask].index[0]

end_date_str = '10/3/2025'
mask_end = (StockData[date_column_name] == end_date_str)
end_2025_index= StockData[mask_end].index[0]

path_steps = end_2025_index-Start_2025_index

#print(column_data_types)
#print(StockData.head())

#2025_price
ogP_2025 = StockData.iloc[Start_2025_index, 1:N_firms+1].astype(float).to_numpy()
#print(ogP_2025)

iterations = 10**3

#create a data frame for log returns.
LogReturns = StockData.iloc[1:Start_2025_index,1:N_firms+1].astype(float)
row,col = LogReturns.shape




#Cycle Through for log returns.
for i in range (col):
    for j in range(row -1):
        LogReturns.iloc[j,i] = np.log((LogReturns.iloc[j+1,i]) / (LogReturns.iloc[j,i]))

LogReturns = LogReturns.iloc[:-1,:]

#varinace & avg returns daily
average_returns = LogReturns.mean().values
sd_returns = np.sqrt(np.var(LogReturns.values, axis =0))


#simple GBM, V(t1) = v(t) *(1+ u + sd*N(0,1))
#exp GBM, V(t1) = v(t)*e^( (u-.5*sd^2)*dt + sd*sqrt(dt)*N(0,1) )

def GBM(mean,P1, sd, steps, iterations):
    #vectorized exponetial GBM
    dt = 1
    Z = np.random.normal(0, 1, (steps-1, iterations))
    drift = (mean - 0.5 * sd**2)*dt
    diffusion = sd * np.sqrt(dt) * Z
    log_returns = drift + diffusion
    log_paths = np.vstack([np.zeros(iterations), log_returns.cumsum(axis=0)])
    paths = P1 * np.exp(log_paths)
    return paths
    
    #simple GBM
    '''
    dataFrame_M= np.zeros((rows,iterations))
    it_N_data = np.zeros(rows)
    it_N_data[0] = P1
    for j in range (iterations):     
        for i in range (1,rows):
            CurGBM = it_N_data[i-1]*(1+mean+sd*np.random.normal(0,1))
            it_N_data[i] = (CurGBM)
        dataFrame_M[:,j]= (it_N_data)
    
    return dataFrame_M
    '''
        


StockDataGBM = np.zeros((N_firms, path_steps, iterations))
for i in range (N_firms):
    StockDataGBM[i] = GBM(average_returns[i], ogP_2025[i], sd_returns[i], path_steps, iterations) 

end_price = StockDataGBM[:,-1,:]
avgReturn = end_price / ogP_2025[:, None] - 1

end_price_avg = (np.mean(end_price, axis =1))
var95__end_returns = np.quantile(avgReturn, 0.05, axis=1)



custom_colors = ['blue', 'red', 'green', 'purple', 'orange'] 
data_viz_GBM_AVG = np.zeros((N_firms,path_steps))
data_viz_GBM_SD_P = np.zeros((N_firms,path_steps))
data_viz_GBM_SD_N = np.zeros((N_firms,path_steps))
data_viz_95VaR = np.zeros((N_firms,path_steps))

Start =0
fig,ax=plt.subplots(1, 4, figsize=(12, 5))
for i in range (Start,N_firms):
    data_viz_GBM_AVG[i,:] = np.mean(StockDataGBM[i,:,:], axis=1)
    data_viz_95VaR[i,:] = np.quantile(StockDataGBM[i,:,:],.05, axis = 1) 
    data_viz_GBM_SD_P[i,:] = np.sqrt(np.var(StockDataGBM[i,:,:], axis=1)) + data_viz_GBM_AVG[i,:]
    data_viz_GBM_SD_N[i,:] = -np.sqrt(np.var(StockDataGBM[i,:,:], axis=1)) + data_viz_GBM_AVG[i,:]
    
    
    
    ax[i].plot(data_viz_95VaR[i,:],label = "VaR 95% Path GBM",color=custom_colors[1])
    ax[i].plot(data_viz_GBM_AVG[i],color=custom_colors[2], label ="AVG P Path GBM")
    ax[i].plot(data_viz_GBM_SD_P[i],color=custom_colors[0],label ="SD Path GBM")
    ax[i].plot(data_viz_GBM_SD_N[i],color=custom_colors[0] )
    
    
    price_data_to_plot = StockData.iloc[Start_2025_index:end_2025_index,i+1]
    ax[i].plot(price_data_to_plot.values, label="Actual P Path", color=custom_colors[3])
    
    ax[i].legend(loc='upper left', fontsize=9)
    ax[i].set_xlabel(f"{StockHead[i+1]}")
    
    
ax[0].set_ylabel("Mean Stock Price ($)")
fig.suptitle('Daily Mean, SD, VaR 95% GBM Paths and Actual Daily Stock Price Path', fontsize=16, fontweight='bold')


fig,ax=plt.subplots(1, 4, figsize=(12, 5))
for i in range (Start,N_firms):
    ax[i].plot(StockDataGBM[i,:,:])
    ax[i].set_xlabel(f"{StockHead[i+1]}")
fig.suptitle("Firms Daily GBM Paths")
ax[0].set_ylabel("Mean Stock Price ($)")

plt.show()

