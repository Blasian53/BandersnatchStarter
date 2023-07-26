from altair import Chart, Tooltip


def chart(df, x, y, target) -> Chart:
    graph = Chart(
        data=df,
        title=f"{y} by {x} for {target}",
        background='#686665',
        height=500,
        width=500,
    ).configure_title(
        fontSize=24
    ).mark_circle(size=100).encode(
        x=x,
        y=y,
        color=target,
        tooltip=Tooltip(df.columns.to_list())
    )
    return graph