setwd("~/cs344/term-project")
set.seed(1234567890)

library("grid")
library("MASS")
library("neuralnet")

trainset <- read.csv("training.csv")
testset <- read.csv("testing.csv")

classnet <- neuralnet(CLASS.8+CLASS.4+CLASS.2+CLASS.1 ~ S1.2+S1.1+C1.8+C1.4+C1.2+C1.1+S2.2+S2.1+C2.8+C2.4+C2.2+C2.1+S3.2+S3.1+C3.8+C3.4+C3.2+C3.1+S4.2+S4.1+C4.8+C4.4+C4.2+C4.1+S5.2+S5.1+C5.8+C5.4+C5.2+C5.1, trainset, hidden = 17, lifesign = "full", threshold = 0.01)

png(filename = "nnet.png")
plot(classnet, rep = "best")
dev.off()

temp_test <- subset(testset, select = c("S1.2", "S1.1", "C1.8", "C1.4", "C1.2", "C1.1", "S2.2", "S2.1", "C2.8", "C2.4", "C2.2", "C2.1", "S3.2", "S3.1", "C3.8", "C3.4", "C3.2", "C3.1", "S4.2", "S4.1", "C4.8", "C4.4", "C4.2", "C4.1", "S5.2", "S5.1", "C5.8", "C5.4", "C5.2", "C5.1"))
classnet.results <- compute(classnet, temp_test)

results <- data.frame(actual8= testset$CLASS.8, actual4 = testset$CLASS.4, actual2 = testset$CLASS.2, actual1 = testset$CLASS.1, prediction = classnet.results$net.result)
results$prediction.4 <- round(results$prediction.4)
results$prediction.3 <- round(results$prediction.3)
results$prediction.2 <- round(results$prediction.2)
results$prediction.1 <- round(results$prediction.1)

write.csv(results, "results.csv")
