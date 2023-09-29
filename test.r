#install.packages("AER")
#install.packages("plm")
library("AER")
library("plm") #panel linear models     


data("CigarettesSW")
str(CigarettesSW)

#pdata.frame transforma os dados em dados em painel
cigarros.p <- pdata.frame(CigarettesSW, index = c("state", "year"))
str(cigarros.p)

reg <- plm(packs ~ income + price, data = cigarros.p, model = "within")
summary(reg)

#plotando os resíduos with color red
plot(reg$residuals, col = "#3ab34a")
