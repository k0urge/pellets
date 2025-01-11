import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

DATA_PATH = 'data/monthly_prices.csv'
COLUMN_LABELS = ["Date", "price for 3 tonnes", "price for 5 tonnes", "price for 8 tonnes", "price for 17 tonnes", "average price"]
IMAGE_DIR = 'docs/images'


def load_data(filepath):
    df = pd.read_csv(filepath, header=None, parse_dates=[0])
    df.columns = COLUMN_LABELS
    return df


def plot_data(df, start_date=None, end_date=None, title="Pellet Price Over Time", save_path=None):
    if start_date and end_date:
        df = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]

    plt.figure(figsize=(12, 6))
    for col, label in zip(df.columns[1:], COLUMN_LABELS[1:]):
        plt.plot(df['Date'], df[col], label=label)

    if start_date and end_date:
        # Get the min and max of the filtered data for y-axis adjustment
        min_value = df.iloc[:, 1:].min().min()
        max_value = df.iloc[:, 1:].max().max()

        # Round y-axis limits to the nearest hundreds
        y_min = np.floor(min_value / 10) * 10
        y_max = np.ceil(max_value / 10) * 10

        plt.xlim(start_date, end_date)
        plt.ylim(y_min, y_max)

    # Set plot labels and title
    plt.xlabel('Date')
    plt.ylabel('CHF/tonne')
    plt.title(title)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()

    if save_path:
        plt.savefig(save_path)
        plt.close()


def main():
    df = load_data(DATA_PATH)

    # Plot the overall data
    plot_data(df, title="Pellet Price Over Time", save_path=f'{IMAGE_DIR}/plot.png')

    # Plot the yearly data
    min_year = df['Date'].dt.year.min()
    max_year = df['Date'].dt.year.max()
    for year in range(min_year, max_year + 1):
        start_date = pd.to_datetime(f'{year}-01-01')
        end_date = pd.to_datetime(f'{year}-12-01')
        plot_data(df, start_date=start_date, end_date=end_date, title=f'Pellet Price Over Time - {year}',
                  save_path=f'{IMAGE_DIR}/plot-{year}.png')


if __name__ == "__main__":
    main()
