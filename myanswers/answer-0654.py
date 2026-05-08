import pandas as pd


def resumir_frecuencias(df, grupo_col, evento_col):

    def agg_group(g):

        vc = g[evento_col].value_counts()

        max_count = vc.max()

        dominante = sorted(
            vc[vc == max_count].index
        )[0]

        return pd.Series({
            'total_eventos': len(g),
            'tipos_distintos': g[evento_col].nunique(),
            'evento_dominante': dominante,
            'pct_dominante': round(
                max_count / len(g) * 100,
                2
            ),
        })

    output = (
        df.groupby(grupo_col)
        .apply(agg_group)
        .reset_index()
        .sort_values(
            'total_eventos',
            ascending=False
        )
        .reset_index(drop=True)
    )

    output['total_eventos'] = output[
        'total_eventos'
    ].astype(int)

    output['tipos_distintos'] = output[
        'tipos_distintos'
    ].astype(int)

    return output