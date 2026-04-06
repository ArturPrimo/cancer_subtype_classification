#install.packages("BiocManager")
#BiocManager::install("TCGAbiolinks")
#install.packages("DT")
#install.packages("rlang")
#update.packages(ask = FALSE)

setwd("C:/Users/artur/OneDrive/Documents/VT/Junior/Spring/ECE4424/cancer_subtype_classification")

library(TCGAbiolinks)
library(DT)

subtypes <- PanCancerAtlas_subtypes()
DT::datatable(
  data = subtypes,
  filter = 'top',
  options = list(scrollX = TRUE, keys = TRUE, pageLength = 5),
  rownames = FALSE
)

dir.create("data", showWarnings = FALSE, recursive = TRUE)

write.csv(subtypes, "data/cancer_subtypes.csv", row.names = FALSE)