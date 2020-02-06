library(RSNNS)
library(NeuralNetTools)
#load example from file choose 1 to 6
load(file="muestra6.rda")
nc=5
trai=training
Values <- trai[,1:nc-1]
Targets <- trai[,nc]
# test/train change ratio if you want
trai <- splitForTrainingAndTest(Values, Targets, ratio=0.15)
str(trai)
# size defines the topology size=n one hidden with n neurons, size=c(n,m,s), three layers with n,m,s
# outputActFunc, activation function
# learnFunc learning type with learnFuncParams defining the parameter(s) i.e. learning rate, momentum
# maxit number of iterations
#http://www.ra.cs.uni-tuebingen.de/SNNS/UserManual/node52.html
model <- mlp(trai$inputsTrain,trai$targetsTrain,size=c(20,20),
             inputsTest = trai$inputsTest, targetsTest = trai$targetsTest,
             outputActFunc = "Act_Logistic",
#             learnFunc = "Std_Backpropagation",learnFuncParams = c(0.1),
             learnFunc = "BackpropMomentum",learnFuncParams = c(0.1,0.1),
#             learnFunc = "SCG", learnFuncParams = c(0.1),
              maxit = 1000)
summary(model)
plotnet(model)
readline(prompt="Press [enter] to continue")
plotIterativeError(model)
readline(prompt="Press [enter] to continue")
sum(model$fitted.values[Targets==0]>0.5)
plotROC(model$fitted.values,Targets)
readline(prompt="Press [enter] to continue")
attributes(model)
hist(model$fitted.values[Targets==0],col=rgb(1,0,0,0.3))
hist(model$fitted.values[Targets==1],col=rgb(0,0,1,0.3),add=T)
readline(prompt="Press [enter] to continue")
readline(prompt="Press [enter] to continue")
par(mfrow = c(2, 2),     # 2x2 layout
    oma = c(0, 0, 0, 0), # two rows of text at the outer left and bottom margin
    mar = c(1, 1, 0, 0), # space for one row of text at ticks and to separate plots
    mgp = c(2, 1, 0),    # axis label at 2 rows distance, tick labels at 1 row
    xpd = NA)            # allow content to protrude into outer margin (and beyond)
plot(trai$inputsTest[,1],predict(model,trai$inputsTest),xlab="",ylab="")
plot(trai$inputsTest[,2],predict(model,trai$inputsTest),xlab="",ylab="")
plot(trai$inputsTest[,3],predict(model,trai$inputsTest),xlab="",ylab="")
plot(trai$inputsTest[,4],predict(model,trai$inputsTest),xlab="",ylab="")
readline(prompt="Press [enter] to continue")
par(mfrow=c(1,1))
dev.off()
