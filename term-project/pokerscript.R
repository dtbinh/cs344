setwd("~/cs344/term-project")
set.seed(1234567890)

library("grid")
library("MASS")
library("neuralnet")

trainset <- read.csv("training.csv")
testset <- read.csv("testing.csv")

classnet <- neuralnet(CLASS ~ S1+C1+S2+C2+S3+C3+S4+C4+S5+C5, trainset, hidden = 5, lifesign = "minimal", linear.output = FALSE, threshold = 0.4)
plot(classnet, rep = "best")

temp_test <- subset(testset, select = c("S1", "C1", "S2", "C2", "S3", "C3", "S4", "C4", "S5", "C5"))
classnet.results <- compute(classnet, temp_test)

results <- data.frame(actual = testset$CLASS, prediction = classnet.results$net.result)
results$prediction <- round(results$prediction)
results[100:115, ]