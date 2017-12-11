wells <- read.csv("https://raw.githubusercontent.com/melans/shale/master/shaledata.csv")
d <- wells[,4:28];
head(d)

pc <- princomp(d, cor = TRUE, scores = TRUE)
summary(pc);
# plot(pc);
# biplot(pc);

# loadings(pc)
#
# dim(pc)
