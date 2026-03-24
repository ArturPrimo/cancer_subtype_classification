#install.packages("BiocManager")
#BiocManager::install("TCGAbiolinks")
#install.packages("DT")
#install.packages("rlang")
#update.packages(ask = FALSE)

library(TCGAbiolinks)
library(DT)

subtypes <- PanCancerAtlas_subtypes()
DT::datatable(
  data = subtypes,
  filter = 'top',
  options = list(scrollX = TRUE, keys = TRUE, pageLength = 5),
  rownames = FALSE
)

write.csv(subtypes, "data/cancer_subtypes.csv", row.names = FALSE)