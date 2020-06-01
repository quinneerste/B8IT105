# READ THE COMMITS FILE
# Assuming the current working directory is set to read the commits.csv file
# Otherwise use setwd('Complete dir here') or if using rstudio cloud,
# upload the .csv by going to Files in the Environment section and selecting the
# Upload option and select the file commits.csv.
# Then proceed to...

commits <- read.csv('commits.csv')
# Note the summary of 422 obv. and 8 variables in 'Environment'
# to show successful read and all rows and columns are read.

#*****DATA ORIENTATION AND ATTRIBUTES#
# Confirm the class of the data set is a data frame
class(commits)

# Review the first six lines and headings of the file and get an overall summary
# of the data set, note the frequency of changes per day and the range, mean and median of the number of comments
head(commits)
summary(commits)

# To show the unique values/ attributes of each data column
unique_vals <- lapply(commits, unique)
View(unique_vals)

# Example of showing unique names of one characteristic - Programmers only
unique_vals[["Programmer"]]
#*****

install.packages("MASS")
library(MASS)
#***** ANALYSIS OF COMMENTS
# To return the MEAN, MEDIAN, RANGE, total NUMBER of COMMENTS, and MODE (respectively) 
mean(commits$Number.of.Comment.Lines)
median(commits$Number.of.Comment.Lines)
range(commits$Number.of.Comment.Lines)
sum(commits$Number.of.Comment.Lines) # returns the sum of all comments, not just 422 comment lines
# R doesn't have a function for mode: 
# Create a function for mode
getmode <- function(v) {
  uniqv <- unique(v)
  uniqv[which.max(tabulate(match(v, uniqv)))]
}
# Define the data set to calculate mode and show value
v <- commits$Number.of.Comment.Lines
print(getmode(v))

# SIMPLE HISTOGRAM showing the FREQUENCY OF NUMBER OF COMMENT LINES
hist(commits$Number.of.Comment.Lines, main="Frequency of number \n of comment lines", xlab = "Number of Comment Lines", ylab = "Frequency", col = 4)

# Use the library (Mass) for analysis
library(MASS)
# Show the NUMBER OF COMMENTS BY PROGRAMMER, broken down BY NUMBER OF COMMENT LINES
# Examine the RELATIONSHIP BETWEEN PROGRAMMER AND NUMBER OF COMMENT LINES - Chi-squared test 
ProgComments = table(commits$Programmer, commits$Number.of.Comment.Lines)
chisq.test(ProgComments)
ProgComments
summary(ProgComments)

# Show the NUMBER OF COMMENTS MADE PER DAY OF THE WEEK, broken down by the
# BY NUMBER OF COMMENT LINES
# Examine the RELATIONSHIP BETWEEN DAYS OF THE WEEK AND THE NUMBER OF COMMENT LINES - Chi-squared test 
DayComments = table(commits$Day, commits$Number.of.Comment.Lines)
chisq.test(DayComments)
DayComments
summary(DayComments)


#*****
#***** ANALYSIS OF PROGRAMMERS
#PROGRAMMERS CHANGES
# Show the NUMBER OF CHANGES PER PROGRAMMER
summary(commits$Programmer)


# SIMPLE PIE CHART showing the NUMBER OF CHANGES PER PROGRAMMER - manual method, with grouping "Other"
slices <- c(24, 9, 7, 152, 191, 26, 13)
lbls1 <- c("Domain", "ajon002", "Freddie", "Jimmy","Thomas","Vincent", "Other")
pie(slices, labels = slices, main="Number of Changes \n Per Programmer", col = rainbow(length(slices)), cex = 0.6)
legend("bottomleft", lbls1, cex = 0.65,
       fill = rainbow(length(slices)))

# PIE CHART showing THE PROPORTION OF CHANGES BY PROGRAMMER - automated method
summary(commits$Programmer)
my_table <- table(commits$Programmer)
lbls2 <- paste(names(my_table), "\n", my_table, sep = "")
pie(my_table, labels = lbls2[0], main="Proportion of Changes \n By Programmer", col = rainbow(length(my_table)))
legend("bottomleft", lbls, cex = 0.32,
       fill = rainbow(length(my_table)))

# Show the NUMBER OF CHANGES BY PROGRAMMER, broken out BY DAY
# Examine the RELATIONSHIP BETWEEN PROGRAMMER AND DAYS OF THE WEEK - Chi-squared test 
ProgDays = table(commits$Programmer, commits$Day)
chisq.test(ProgDays)
ProgDays
summary(ProgDays)


# PIE CHART showing THE NUMBER OF CHANGES BY DAY OF THE WEEK
summary(commits$Day)
my_table_Days <- table(commits$Day)
lbls3 <- paste(names(my_table_Days), "\n", my_table_Days, sep = "")
pie(my_table_Days, labels = lbls3, main="Number of changes by \n day of the week", col=rainbow(length(lbls3)), cex = 0.8) 



if (!require("RColorBrewer")) {
  install.packages("RColorBrewer")
  library(RColorBrewer)
}

# STACKED BAR CHART showing CHANGES BY DAY OF THE WEEK, BROKEN DOWN BY PROGRAMMER
table_2 <- table(commits$Programmer, commits$Day)
barplot(table_2, xlab="Day of the week", main = "Changes by Day of the Week, \n
Broken Down by Programmer", col = brewer.pal(10,"Set3"))
legend("topright", rownames(table_2), cex = 0.3,
       fill = brewer.pal(10,"Set3"))
         