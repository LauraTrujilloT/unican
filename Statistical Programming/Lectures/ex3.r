data <- read.table("dataR1.dat", header=TRUE)

genderFac <- factor(data[,3])
genderFac

genders <- levels(genderFac)
