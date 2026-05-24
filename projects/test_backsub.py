# 1. Set environments
import powerxrd as xrd
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 2. Run the code
def test_backsub():
    # open file from our folder - recommend use pandas
    open_file = "../diff_data/sample.xy"

    try: # use pandas to read the file
        df = pd.read_csv(open_file, sep=r'\s+', header=None, comment='#')
        x = df[0].values
        y = df[1].values
        data = (x, y) # main data
    except Exception as e:
        print(f"error reading the file:{e}")
        print("check sample.xy")
        return None

    # 3. Load data into algorithm
    plt.plot(*data, label='sample-raw data')

    chart = xrd.Chart(*data)
    chart.emission_lines(xrange_Ka=[10, 20], show = True)

    # 4. Calculate background substraction
    backsub_data = chart.backsub() # powerxrd returns a tuple of (x, y corrected)
    plt.plot(*backsub_data, label='sample-backsub')
    plt.xlabel(r'2$\theta$ (degree)')
    plt.ylabel('intensity (a.u.)')
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.legend()
    plt.show

# 5. Return the data to save as the function
    return backsub_data

# 6. Run final function
sample_backsub = test_backsub()

# 7. save the data in csv or txt file
if sample_backsub is not None:
    export_data = np.column_stack((sample_backsub[0], sample_backsub[1]))

    np.savetxt("sample_backsub.csv", export_data, delimiter=",", header= "2q, intensity", comments="")
    