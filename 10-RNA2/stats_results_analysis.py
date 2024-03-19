import pandas as pd
import numpy as np
import seaborn as sns

STATS_PATH = r"/groups/pupko/yairshimony/CompLabNGS/10-RNA2/stats_results.csv"

stats_df = pd.read_csv(STATS_PATH)

# Q7
filtered_genes = stats_df.loc[(stats_df['log2FoldChange'] > 1) & (stats_df['padj'] < 0.05)]
print(f"Q7: {len(filtered_genes)}")

# Q8
stats_df['-log10pvalue'] = -np.log10(stats_df['padj'])
plot = sns.scatterplot(data=stats_df, x='log2FoldChange', y='-log10pvalue')
fig = plot.get_figure()
fig.savefig("volcanot_plot.png")

# Q9 + Q10 + Q11
genes_expressed_higher_in_s288c = stats_df.loc[(stats_df['log2FoldChange'] > 1) & (stats_df['padj'] < 0.01)]
genes_expressed_higher_in_rm11 = stats_df.loc[(stats_df['log2FoldChange'] < 1) & (stats_df['padj'] < 0.01)]
s288c_higher = len(genes_expressed_higher_in_s288c)
rm11_higher = len(genes_expressed_higher_in_rm11)
de_genes = s288c_higher + rm11_higher

print(f"There are {de_genes} DE genes, of them {rm11_higher} are expressed higher in rm11 and {s288c_higher} are expressed higher in s288c.")