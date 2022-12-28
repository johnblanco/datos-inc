import pandas as pd


def plot_records_by_year(df, departments, from_year):
    df2 = df[(df.year > from_year) & (df.Departamento.isin(departments))].copy()
    years = df2.year.sort_values().unique()
    data = {}
    for d in departments:
        df3 = df2[df2.Departamento == d].copy()
        data[d] = df3.year.value_counts()
    df2 = pd.DataFrame(data, index=years)
    df2.plot.line(title="Cantidad de ofrecimientos por Departamento", xticks=years)


def plot_surface_by_year(df, departments, from_year):
    df2 = df[(df.year > from_year) & (df.Departamento.isin(departments))].copy()
    years = df2.year.sort_values().unique()
    data = {}
    for d in departments:
        df3 = df2[df2.Departamento == d].copy()
        data[d] = df3.groupby(by='year').sum(numeric_only=True)["Superficie total(ha)"]
    df2 = pd.DataFrame(data, index=years)
    df2.plot.line(title="Hectarias ofrecidas por Departamento", xticks=years)
