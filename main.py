from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from sklearn.datasets import fetch_california_housing

LEAKAGE_CORR_THRESHOLD = 0.95
STRONG_CORR_THRESHOLD = 0.5

console = Console()

dataset = fetch_california_housing(as_frame=True)
df = dataset.frame

target = dataset.target.name
features = dataset.feature_names


def section(title):
    console.print()
    console.rule(f"[bold cyan]{title}")


def corr_style(value):
    color = "green" if value > 0 else "red"
    if abs(value) >= STRONG_CORR_THRESHOLD:
        return f"bold {color}"
    return color


console.print(Panel.fit("[bold]California Housing[/bold] — data exploration", style="magenta"))

section("Preview")
preview = Table(header_style="bold")
for column in df.columns:
    style = "bold yellow" if column == target else None
    preview.add_column(column, justify="right", style=style, header_style=style)
for _, row in df.head().iterrows():
    preview.add_row(*(f"{value:g}" for value in row))
console.print(preview)
console.print(f"Rows: [bold]{df.shape[0]}[/bold]  Columns: [bold]{df.shape[1]}[/bold]")

section("Target")
console.print(f"Target column: [bold yellow]{target}[/bold yellow]")
stats = Table(show_header=False)
stats.add_column(style="bold")
stats.add_column(justify="right")
for name, value in df[target].describe().items():
    stats.add_row(name, f"{value:g}")
console.print(stats)

section("Features")
feature_table = Table(header_style="bold")
feature_table.add_column("Feature")
feature_table.add_column("Type", style="dim")
for feature in features:
    feature_table.add_row(feature, str(df[feature].dtype))
console.print(feature_table)

section("Missing values")
missing = df.isna().sum()
missing_table = Table(header_style="bold")
missing_table.add_column("Column")
missing_table.add_column("Missing", justify="right")
for column, count in missing.items():
    style = "bold red" if count else "green"
    missing_table.add_row(column, f"[{style}]{count}[/{style}]")
console.print(missing_table)

# A feature that almost perfectly correlates with the target may be
# derived from it, which would leak the answer into the model.
section("Correlation with target")
corr = df[features].corrwith(df[target]).sort_values(key=abs, ascending=False)
corr_table = Table(header_style="bold")
corr_table.add_column("Feature")
corr_table.add_column("Correlation", justify="right")
for feature, value in corr.items():
    style = corr_style(value)
    corr_table.add_row(feature, f"[{style}]{value:+.3f}[/{style}]")
console.print(corr_table)

suspicious = corr[corr.abs() >= LEAKAGE_CORR_THRESHOLD]
if suspicious.empty:
    console.print(
        f"[green]No features with |corr| >= {LEAKAGE_CORR_THRESHOLD}: no obvious leakage[/green]"
    )
else:
    console.print(f"[bold red]Possible leakage (|corr| >= {LEAKAGE_CORR_THRESHOLD}):[/bold red]")
    for feature, value in suspicious.items():
        console.print(f"  [red]{feature}: {value:+.3f}[/red]")

section("Duplicates")
duplicates = df.duplicated().sum()
style = "bold red" if duplicates else "green"
console.print(f"Duplicate rows: [{style}]{duplicates}[/{style}]")
