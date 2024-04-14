
import pandas as pd
import seaborn as sns

gasolina_df = pd.read_csv('gasolina.csv')
gasolina_graph = sns.lineplot(gasolina_df, x='dia', y='venda')
gasolina_graph.set(title='Vendas Diárias de Gasolina', xlabel='Dias', ylabel='Vendas (R$)')

fig = gasolina_graph.get_figure()
fig.savefig('gasolina.png')
