data <- read.table("dataR1.dat", header=TRUE)
heights <- data[,2]

mymean <- function(x){
  res = sum(x) / length(x)
  return(res)
}

meanh <- mymean(heights)
meanh

meanR <- mean(heights)
meanR
