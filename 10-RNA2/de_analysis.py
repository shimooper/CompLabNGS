import pandas as pd
import seaborn as sns

from pydeseq2.dds import DeseqDataSet
from pydeseq2.default_inference import DefaultInference
from pydeseq2.ds import DeseqStats

COUNTS_PATH = r"/groups/pupko/yairshimony/CompLabNGS/10-RNA2/data/counts.tsv"
COLUMNS_TO_USE = ['Geneid', 'RM11_RNA-seq_rep1.bam', 'RM11_RNA-seq_rep2.bam',	'RM11_RNA-seq_rep3.bam', 'S288C_RNA-seq_rep1.bam', 'S288C_RNA-seq_rep2.bam', 'S288C_RNA-seq_rep3.bam']

SAMPLE_INFO_PATH = r"/groups/pupko/yairshimony/CompLabNGS/10-RNA2/data/sample_info.tsv"

counts_matrix = pd.read_csv(COUNTS_PATH, delimiter='\t', skiprows=1, usecols=COLUMNS_TO_USE)
counts_matrix.set_index('Geneid', inplace=True)
counts_matrix_filtered = counts_matrix[(counts_matrix >= 10).any(axis=1)]

print(f'#transcripts before filtering: {len(counts_matrix)}, #transcripts after filtering: {len(counts_matrix_filtered)}')

plot = sns.clustermap(counts_matrix.corr())
plot.savefig("samples_clustermap.png")

sample_info_df = pd.read_csv(SAMPLE_INFO_PATH, delimiter='\t')
sample_info_df.set_index('sample', inplace=True)

inference = DefaultInference(n_cpus=8)
dds = DeseqDataSet(
    counts=counts_matrix_filtered.T,
    metadata=sample_info_df,
    design_factors=['batch', 'strain'],
    refit_cooks=True,
    inference=inference
)

dds.deseq2()

stats_results = DeseqStats(dds, inference=inference)
print(stats_results.summary())
stats_results.results_df.to_csv("stats_results.csv")