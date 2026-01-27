import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg') # Use non-interactive backend

class Dashboard:
    @staticmethod
    def plot_mtm(df, filename="mtm_dashboard.png"):
        """
        Plots the MTM profit/loss of positions as a bar chart.
        """
        if df.empty:
            print("No positions to plot.")
            return

        plt.figure(figsize=(10, 6))
        colors = ['green' if x >= 0 else 'red' for x in df['m2m']]
        plt.bar(df['tradingsymbol'], df['m2m'], color=colors)

        plt.title('Mark to Market (MTM) Profit/Loss')
        plt.xlabel('Instrument')
        plt.ylabel('MTM (INR)')
        plt.xticks(rotation=45)
        plt.grid(axis='y', linestyle='--', alpha=0.7)

        plt.tight_layout()
        plt.savefig(filename)
        plt.close()
        print(f"Dashboard saved to {filename}")
