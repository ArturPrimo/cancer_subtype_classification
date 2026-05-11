install.packages("BiocManager")
BiocManager::install("TCGAbiolinks")
install.packages("DT")
install.packages("rlang")
update.packages(ask = FALSE)

library(TCGAbiolinks)
library(DT)
library(SummarizedExperiment)

subtypes <- PanCancerAtlas_subtypes()
DT::datatable(
  data = subtypes,
  filter = 'top',
  options = list(scrollX = TRUE, keys = TRUE, pageLength = 5),
  rownames = FALSE
)

query.exp.hg38 <- GDCquery(
  project = "TCGA-BRCA", 
  # project = "TCGA-COAD", 
  # project = "TCGA-PRAD", 
  data.category = "Transcriptome Profiling", 
  data.type = "Gene Expression Quantification", 
  workflow.type = "STAR - Counts"
)

GDCdownload(query.exp.hg38)

expdat <- GDCprepare(
  query = query.exp.hg38,
  save = TRUE, 
  save.filename = "exp_brca.rda"
  # save.filename = "exp_coad.rda"
  # save.filename = "exp_prad.rda"
)

expr_matrix <- assay(expdat)
expr_df <- as.data.frame(expr_matrix)
fileName <- "tcga_brca.csv"
# fileName <- "tcga_coad.csv"
# fileName <- "tcga_prad.csv"
write.csv(expr_df, file=fileName, row.names=T, quote=F)