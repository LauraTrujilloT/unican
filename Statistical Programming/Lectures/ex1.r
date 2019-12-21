options(stringAsFactors=FALSE)

t1 <- data.frame(Names=c("Joe","Mary","Tom","Jen"),
  Heights=c(1.65, 1.70, 1.75, 1.60),Gender=c("Male","Female","Male","Female"))

write.table(t1, file="dataR1.dat")

rm(t1)
t1 <- read.table("dataR1.dat", header=TRUE)
heights <- t1[ ,2]
heights
