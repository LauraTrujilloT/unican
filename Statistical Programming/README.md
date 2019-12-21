 [R Intro](venus.ifca.unican.es/Rintro)

Professor: Maite Ceballos

# R : First steps

- `R` is suited for statistics and it's available for all the platforms and also in continuing development.

- It's case sensitive.
- **Help** in R: `help()`
- To cite `citation()`. It's **mandatory** to cite R in all projects, hw, etc.

For **install a package** $\rightarrow$ `conda install -c r "NAME OF PACKAGE"`

## Data structure
`R` is an OOP.

### Types:
- Vectors (1D)
- Matrices (2D)
- Arrays
- Factors
- Lists
- Data Frames (Tables)
- Functions

## Vectors
There are several ways to assign values to a variable:

```python
a = 1
a <- 1
1 -> a
assign("a",1)
```

To generate a vector with several numeric values:

```python
a <- c(10,11,15,19)
#assign four values to a vector
#using the concatenate command
```
To generate a sequence:

```python
2:10 #Last number used

seq(from=n1,to=n2,by=n3)

help("seq")

seq(from=1,to=50,by=10)

#If we need to know which are the objects we're working
ls()
```

### Logical Vectors

```python
a <- seq(1:10)

b <- (a>5) #b logical vector
```

### Character Vectors

```python
a <- "This is an example"
paste("the value of x is". x)
```

### Matrix




# Data Reading and Writting
Files such `.dat` and `.csv`.


```python
gal <- read.table("galaxies.dat", header=TRUE)

```


# Functions `function`

```python
stddev <- function(x) {
  res = sqrt(sum((x - mean(x))^2) / (length(x) - 1))
  return(res)
}
```

> Homework = En el apartado R Intro ver GRAPHS. Intentar Exercise 5 AirQuality (cargar tabla con attach)

# Graphs

Basic functions `plot(x,y)` and `hist(x)`. Tho plotting process will then be:

```python
pdf(myfile.pdf, width=10, height=7.1)
potsctipt(myfile.ps)
plot(x,y)
dev.off() #close device
```

Some commands:

`plot` $\rightarrow$ makes scatterplots or other R-objects plots.

`abline` $\rightarrow$ add straight line

`lines` $\rightarrow$ add connected line segments

`segments` $\rightarrow$ add disconnected line segments

`points` $\rightarrow$ add points

`arrows` $\rightarrow$ add arrows

`polygon` $\rightarrow$ add polygon

`text` $\rightarrow$ add text labels

`title` $\rightarrow$ add labels for x,y axes, title, subtitle, outer margin

`axis` $\rightarrow$ modify axes ticks and labels

## Histograms
`freq` number of time of something happening. (It's the height of the bar). If `FALSE` plot won't be higher than 1.

## Scatter plots
`plot(x,y)` or `plot(y~x)`
An example:
```python
par(mfrow=c(2,2))
plot(z$Day,z$Ozone,col="red",
  xlab="Days of May",ylab="Ozone Levels",pch=5)
plot(y,x,col=rgb(0,0.5,0.5,0.8), xlab="Month",ylab=)
```
![alt text](c.png)

# Statistics
R containts a very comprehensive library with statistical functions including the most common distributions.

If I want the density function of the gaussian distribution `dgaussian(x, mean = 0, sd = 1,...)`

### Random numbers
To ensure reproducibility, it's important to set the random number seed when performing simulations `set.seed()`

example: `rnorm(n, mean = 0, sd = 1)`

> HW : exercise 6

# Settings

### Change size of plots

```python
library(repr)
options(repr.plot.width = 4, repr.plot.height = 4)
```

### Change number of decimal digits
```python
options(digits=22)
```
