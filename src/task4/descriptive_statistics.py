import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def generate_sot_descriptive_summary(df, boxplot_path, hist_path):
    stats = df.groupby('Possession_Style')['SoT%'].describe()

    outliers_list = []
    for style in ['High Possession (>55%)', 'Low/Mid Possession (<=55%)']:
        style_df = df[df['Possession_Style'] == style]
        Q1 = style_df['SoT%'].quantile(0.25)
        Q3 = style_df['SoT%'].quantile(0.75)
        IQR = Q3 - Q1
        
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR

        role_outliers = style_df[(style_df['SoT%'] < lower_bound) | (style_df['SoT%'] > upper_bound)]
        outliers_list.append(role_outliers)

    outliers_df = pd.concat(outliers_list)

    # Generate Boxplot
    plt.figure(figsize=(8, 6))
    sns.boxplot(
        x='Possession_Style', y='SoT%', data=df, showmeans=True,
        meanprops={"marker":"D", "markerfacecolor":"white", "markeredgecolor":"black", "markersize":"6"}
    )
    plt.title('Shot on Target % by Possession Style (Diamond = Mean)')
    plt.ylabel('Shot on Target Percentage (%)')
    plt.savefig(boxplot_path)
    plt.close()

    # Generate Histograms
    fig, axes = plt.subplots(1, 2, figsize=(14, 6), sharey=True, sharex=True)
    colors = {'High Possession (>55%)': '#1f77b4', 'Low/Mid Possession (<=55%)': '#ff7f0e'}
    
    for i, style in enumerate(['High Possession (>55%)', 'Low/Mid Possession (<=55%)']):
        style_data = df[df['Possession_Style'] == style]['SoT%']
        sns.histplot(style_data, kde=True, ax=axes[i], color=colors[style], bins=10)
        
        mean_val = style_data.mean()
        median_val = style_data.median()
        
        axes[i].axvline(mean_val, color='red', linestyle='--', linewidth=2, label=f'Mean: {mean_val:.1f}%')
        axes[i].axvline(median_val, color='green', linestyle='-', linewidth=2, label=f'Median: {median_val:.1f}%')
        axes[i].set_title(f'{style} SoT% Distribution')
        axes[i].set_xlabel('Shot on Target %')
        axes[i].legend()

    plt.suptitle('Distribution of Shot Accuracy with Mean/Median Comparison')
    plt.tight_layout()
    plt.savefig(hist_path)
    plt.close()

    return stats, outliers_df