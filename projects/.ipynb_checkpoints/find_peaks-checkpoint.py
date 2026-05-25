# set environments
import matplotlib.pyplot as plt
import pandas as pd
import powerxrd as xrd

# find peaks (within a certain peak height tolerance)
def test_allpeaks():
    file_path = "../diff_data/sample_backsub.csv"

    try:
        df = pd.read_csv(file_path, sep=r",", header=None, comment="#")
        df[0] = pd.to_numeric(df[0], errors='coerce')
        df[1] = pd.to_numeric(df[1], errors='coerce')
        df = df.dropna()
        x = df[0].values
        y = df[1].values
        data = (x, y)

    except Exception as e:
        print(f'error reading file:{e}')
        return
        
    chart = xrd.Chart(*data)

    # Running data from test_backsub
    chart.backsub(tol=1, show=False)

    # Smootting data with a 10-point moving average to eliminate recursion-triggering noise
    chart.x, chart.y = chart.mav(n=10)
    
    # Peaks finding of the smoothed data
    chart.allpeaks(tols=(0.11, 1.0), verbose=True, show=True)
    plt.xlabel(r"2$\theta$ (degree)")
    plt.ylabel('intensity (a.u.)')
    plt.title("Scherrer Calculation")
    plt.savefig("scherrer calculation.svg.svg", bbox_inches='tight')
    
    plt.figure(figsize=(11, 5))
    plt.plot(*data, label='sample-backsub')
    chart.allpeaks(tols=(0.11, 1.0), verbose=True, show=True)
    plt.xlabel(r"2$\theta$ (degree)")
    plt.ylabel('intensity (a.u.)')
    plt.title("test_backsub vs Scherrer Calculation")
    plt.grid(alpha=0.5, linestyle='--')
    plt.savefig("test_backsub vs scherrer calculation.svg.svg", bbox_inches='tight')
    plt.show()

    
test_allpeaks()