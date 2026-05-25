# Noise reduction through a running average
def test_mav():
    open_file = "../diff_data/sample_backsub.csv"

    try:
        df = pd.read_csv(open_file, sep=r",", header=None, comment="#")
        df[0] = pd.to_numeric(df[0], errors='coerce')
        df[1] = pd.to_numeric(df[1], errors='coerce')
        df = df.dropna()
        x = df[0].values
        y = df[1].values
        data = (x, y)

    except Exception as e:
        print(f'error reading file:{e}')
        return

    chart= xrd.Chart(*data)

    # Add backsub as base line
    chart.backsub(tol =1, show=False)

    # set point for moving average size
    n = 10

    # Plot original noisy data and after reduction
    plt.plot(chart.x, chart.y, label ='noisy', color='salmon')
    plt.plot(*chart.mav(n), label= 'after reduction', lw =1.2)
    plt.xlabel(r"2$\theta$ (degree)")
    plt.grid(alpha=0.5, linestyle='--')
    plt.legend()
    plt.savefig("Noise reduction.svg", bbox_inches = 'tight')
    plt.show()
    
test_mav()
    