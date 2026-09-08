import matplotlib.pyplot as plt
import scipy.stats as stats
import seaborn as sns
import pandas as pd

def descriptive_statistics(starters, non_starters, hist_path, box_path, table_path="figures/task3/t_table.png", *args):
    # Detect exact column name
    col = next((c for c in ['fouls_per_90', 'Fouls_90', 'Fls_90', 'Fls/90', 'Fouls/90', 'Fls'] if c in starters.columns), None)

    if not col:
        raise KeyError(f"Could not find fouls column. Available columns: {list(starters.columns)}")

    s_fouls = starters[col].dropna()
    ns_fouls = non_starters[col].dropna()

    df_combined = pd.DataFrame({
        'Fouls': pd.concat([s_fouls, ns_fouls], ignore_index=True),
        'Group': ['Starters'] * len(s_fouls) + ['Non-Starters'] * len(ns_fouls)
    })

    palette = {'Starters': '#1f77b4', 'Non-Starters': '#ff7f0e'}

    # 1. Histogram
    plt.figure(figsize=(8, 5))
    plt.hist(s_fouls, alpha=0.7, label='Starters', color='#1f77b4')
    plt.hist(ns_fouls, alpha=0.7, label='Non-Starters', color='#ff7f0e')
    plt.title('Histogram of Fouls/90')
    plt.xlabel('Fouls per 90 Minutes')
    plt.ylabel('Number of Players')
    plt.legend()
    plt.tight_layout()
    plt.savefig(hist_path)
    plt.close()

    # 2. Boxplot
    plt.figure(figsize=(8, 5))
    sns.boxplot(data=df_combined, x='Group', y='Fouls', palette=palette, hue='Group', legend=False)
    plt.title('Boxplot of Fouls/90 - Starters vs Non-Starters')
    plt.xlabel('')
    plt.ylabel('Fouls per 90 Minutes')
    plt.tight_layout()
    plt.savefig(box_path)
    plt.close()

    # 3. Generate t-Distribution Summary Table Image
    fig, ax = plt.subplots(figsize=(7, 3))
    ax.axis('off')
    ax.axis('tight')

    table_data = [
        ['Metric', 'Starters', 'Non-Starters'],
        ['Sample Size (n)', f"{len(s_fouls)}", f"{len(ns_fouls)}"],
        ['Mean (Fouls/90)', f"{s_fouls.mean():.4f}", f"{ns_fouls.mean():.4f}"],
        ['Std Dev (s)', f"{s_fouls.std():.4f}", f"{ns_fouls.std():.4f}"],
        ['Std Error (SE)', f"{stats.sem(s_fouls):.4f}", f"{stats.sem(ns_fouls):.4f}"]
    ]

    table = ax.table(cellText=table_data, loc='center', cellLoc='center')
    table.auto_set_font_size(False)
    table.set_fontsize(11)
    table.scale(1.2, 1.6)

    # Style header row
    for (row, col_idx), cell in table.get_celld().items():
        if row == 0:
            cell.set_text_props(weight='bold', color='white')
            cell.set_facecolor('#2c3e50')
        else:
            cell.set_facecolor('#f8f9fa' if row % 2 == 0 else '#ffffff')

    plt.title('t-Distribution / Descriptive Statistics Summary', pad=10, weight='bold')
    plt.tight_layout()
    plt.savefig(table_path, bbox_inches='tight', dpi=300)
    plt.close()

    return starters.describe(), non_starters.describe()
