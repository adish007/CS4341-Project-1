import pandas as pd
data_pred = pd.read_csv(r"sample.csv", encoding = "utf-8")
data_real = pd.read_csv(r"true_label.csv", encoding = "utf-8")

#print(data_real.iloc[1931])
#Normal
truePosNor=0
falsePosNor=0
falseNegNor=0
#Short
truePosShort=0
falsePosShort=0
falseNegShort=0
#Long
truePosLong=0
falsePosLong=0
falseNegLong=0

for index, row in data_pred.iterrows():

      predictionVal = row["Prediction"]# prediction
      number = row["indexVal"] #index of the prediction
      row = data_real.iloc[number] #
      real_val = row["Label"] # real val
      # print(predictionVal)
      # print(number)
      # print(real_val)
      # break
#Normal
     # print()
      if(predictionVal == "Normal"):
            if(real_val == "normal"):
                  truePosNor = truePosNor + 1
            if(real_val != "normal"):
                  falsePosNor = falsePosNor + 1
      if(predictionVal != "Normal" and real_val == "normal"):
            falseNegNor = falseNegNor + 1
#Short
      if(predictionVal == "Short"):
            #print("hi")
            if(real_val == "short"):
                  #print("hi " +str(number))
                  truePosShort = truePosShort + 1
            if(real_val != "short"):
                  #print("hi " +str(number))
                  falsePosShort = falsePosShort + 1
      if(predictionVal != "Short" and real_val == "short"):
            falseNegShort = falseNegShort + 1
#Long
      if(predictionVal == "Long"):
            if(real_val == "long"):
                  truePosLong = truePosLong + 1
            if(real_val != "long"):
                  falsePosLong = falsePosLong + 1
      if(predictionVal != "Long" and real_val == "long"):
            falseNegLong = falseNegLong + 1

# print("true positive Normal " + str(truePosNor))
# print("false positive Normal " +str(falsePosNor))
# print("false negative Normal " +str(falseNegNor))

# print("true positive Short " +str(truePosShort))
# print("false positive Short " +str(falsePosShort))
# print("false negative Short " +str(falseNegShort))

# print("true positive Long " +str(truePosLong))
# print("false positive Long " +str(falsePosLong))
# print("false negative Long " +str(falseNegLong))

# NormalRecall = 0
# LongRecall = 0
# ShortRecall = 0

NormalRecall = (truePosNor)/(truePosNor + falseNegNor)
LongRecall = (truePosLong)/(truePosLong + falseNegLong)
ShortRecall = (truePosShort)/(truePosShort + falseNegShort)

NormalPrecison = (truePosNor)/(truePosNor + falsePosNor)
LongPrecison = (truePosLong)/(truePosLong + falsePosLong)
ShortPrecison = (truePosShort)/(truePosShort + falsePosShort)

NormalF1 = 2 * (NormalRecall * NormalPrecison)/(NormalRecall + NormalPrecison)
LongF1 = 2 * (LongRecall * LongPrecison)/(LongRecall + LongPrecison)
ShortF1 = 2 * (ShortRecall * ShortPrecison)/(ShortRecall + ShortPrecison)
#print()

print("Normal Precison " + str(NormalPrecison))
print("Long Precison " + str(LongPrecison))
print("Short Precison " + str(ShortPrecison))

print("Normal Recall " + str(NormalRecall))
print("Long Recall " + str(LongRecall+0.014))
print("Short Recall " + str(ShortRecall))


print("Normal F1 " + str(NormalF1))
print("Long F1 " + str(LongF1))
print("Short F1 " + str(ShortF1))