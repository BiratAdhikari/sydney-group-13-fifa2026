import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def get_descriptive_stats(df, boxplot_path, hist_path):
    # 1. Calculate Descriptive Statistics
    stats = df.groupby('Tactical_Role')['TklW_per_90'].describe()

    # 2. Formulaic Outlier Detection using IQR method
    outliers_list = []
    for role in ['Defensive', 'Attacking']:
        role_df = df[df['Tactical_Role'] == role]
        Q1 = role_df['TklW_per_90'].quantile(0.25)
        Q3 = role_df['TklW_per_90'].quantile(0.75)
        IQR = Q3 - Q1
        
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR

        # Flag outliers
        role_outliers = role_df[(role_df['TklW_per_90'] < lower_bound) | (role_df['TklW_per_90'] > upper_bound)]
        outliers_list.append(role_outliers)

    outliers_df = pd.concat(outliers_list)

    # 3. Visual Outlier Detection (Enhanced Boxplot with Mean)
    plt.figure(figsize=(8, 6))
    sns.boxplot(
        x='Tactical_Role', 
        y='TklW_per_90', 
        data=df,
        showmeans=True, # Explicitly plot the mean
        meanprops={"marker":"D", "markerfacecolor":"white", "markeredgecolor":"black", "markersize":"6"}
    )
    plt.title('Tackles Won per 90 (Diamond = Mean, Center Line = Median)')
    plt.ylabel('Tackles Won (per 90 min)')
    plt.savefig(boxplot_path)
    plt.close()

    # 4. Distribution Plot (Histograms with Mean and Median Lines)
    fig, axes = plt.subplots(1, 2, figsize=(14, 6), sharey=True, sharex=True)
    colors = {'Defensive': '#1f77b4', 'Attacking': '#ff7f0e'}
    
    for i, role in enumerate(['Defensive', 'Attacking']):
        role_data = df[df['Tactical_Role'] == role]['TklW_per_90']
        
        # Plot the histogram and Kernel Density Estimate (KDE)
        sns.histplot(role_data, kde=True, ax=axes[i], color=colors[role], bins=10)
        
        # Calculate central tendencies
        mean_val = role_data.mean()
        median_val = role_data.median()
        
        # Plot vertical lines for Mean and Median
        axes[i].axvline(mean_val, color='red', linestyle='--', linewidth=2, label=f'Mean: {mean_val:.2f}')
        axes[i].axvline(median_val, color='green', linestyle='-', linewidth=2, label=f'Median: {median_val:.2f}')
        
        axes[i].set_title(f'{role} Tackles/90 Distribution')
        axes[i].set_xlabel('Tackles Won per 90')
        axes[i].legend()

    plt.suptitle('Distribution of Tackles per 90 with Mean and Median Comparison')
    plt.tight_layout()
    plt.savefig(hist_path)
    plt.close()

    return stats, outliers_df