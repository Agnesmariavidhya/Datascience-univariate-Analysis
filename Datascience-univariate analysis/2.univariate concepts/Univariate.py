class Univariate():
    def QuanQual(dataset):
        quan=[]
        qual=[]
        for columnName in dataset.columns:
            #print(columnName)
            if (dataset[columnName].dtype==object):
                #print("qual")
                qual.append(columnName)
            else:
                #print("quan")
                quan.append(columnName)
        return quan, qual
        
    def Univariate(quan,dataset):
        descriptive=pd.DataFrame(index=["Mean","Median","Mode","Q1:25%","Q2:50%","Q3:75%","99%"         ,"Q4:100%","IQR","1.5rule","Lesser","Greater","Min","Max"],columns=quan)
        for columnName in quan:
            descriptive.loc["Mean",columnName]=dataset[columnName].mean()
            descriptive.loc["Median",columnName]=dataset[columnName].median()
            descriptive.loc["Mode",columnName]=dataset[columnName].mode()[0]
            descriptive.loc["Q1:25%",columnName]=dataset.describe()[columnName]["25%"]
            descriptive.loc["Q2:50%",columnName]=dataset.describe()[columnName]["50%"]
            descriptive.loc["Q3:75%",columnName]=dataset.describe()[columnName]["75%"]
            descriptive.loc["99%",columnName]=np.percentile(dataset[columnName],99)
            descriptive.loc["Q4:100%",columnName]=dataset.describe()[columnName]["max"]
            descriptive.loc["IQR",columnName]=descriptive.loc["Q3:75%",columnName]-descriptive.loc["Q1:25%",columnName]
            descriptive.loc["1.5rule",columnName]=1.5*descriptive.loc["IQR",columnName]
            descriptive.loc["Lesser",columnName]=descriptive.loc["Q1:25%",columnName]-descriptive.loc["1.5rule",columnName]
            descriptive.loc["Greater",columnName]=descriptive.loc["Q3:75%",columnName]+descriptive.loc["1.5rule",columnName]
            descriptive.loc["Min",columnName]=dataset[columnName].min()
            descriptive.loc["Max",columnName]=dataset[columnName].max()
        return descriptive 
    
    def outliers_columnName(dataset):
        lesser=[]
        greater=[]
        for columnName in quan:
            if (descriptive.loc["Min",columnName]<descriptive.loc["Lesser",columnName]):
                lesser.append(columnName)
            if (descriptive.loc["Max",columnName]>descriptive.loc["Greater",columnName]):
                greater.append(columnName)
        return lesser,greater

    def Replacement_outliers():
        for columnName in lesser:
            dataset.loc[dataset[columnName] < descriptive.loc["Lesser", columnName], columnName] = descriptive.loc["Lesser", columnName]
        for columnName in greater:
            dataset.loc[dataset[columnName] > descriptive.loc["Greater", columnName], columnName] = descriptive.loc["Greater", columnName]
        return
    
    def Freq_Table(columnName,dataset):
        Freq_Table=pd.DataFrame(columns=["Unique_values","Frequency","Relative_Frequency","cumulative_Frequency"])
        Freq_Table["Unique_values"]=dataset[columnName].value_counts().index
        Freq_Table["Frequency"]=dataset[columnName].value_counts().values
        Freq_Table["Relative_Frequency"]=Freq_Table["Frequency"]/103
        Freq_Table["cumulative_Frequency"]=Freq_Table["Relative_Frequency"].cumsum()
        return Freq_Table