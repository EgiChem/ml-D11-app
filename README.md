# ML-D11-app

Prediction of self-diffusion of polar/non-polar, spherical/non-spherical, and hydrogen-bonding molecules in liquids, compressed gases or supercritical fluids.

The AARD achieved by the model in the test set was 9.06 %.

The machine learning models were trained with a database of 5551 experimental data points from over 216 systems. For more information check the following papers:

## Installation

1. Download this repository by clicking `Code` > `Download ZIP`. Unzip the folder.

2. Install Python. We recommend a installing the [Anaconda Distribution](https://www.anaconda.com/download) or [Miniconda](https://docs.conda.io/projects/miniconda/en/latest/miniconda-install.html).

3. Open the Anaconda Prompt and change the directory to where you extracted the repository files: `cd path/to/folder`.

3. Create a `conda` virtual environment using the provided `environment.yml` file: `conda env create -f environment.yml`

4. Activate the environment with: `conda activate ml`.

5. You can now use the models following instructions bellow either in a `.py` script file or in a Jupyter Notebook (already provided in the environment by running `jupyter lab`).

## Usage

Call the program and provide the properties:

1. Temperature (K)
2. Critical volume (cm3/mol)
3. Critical temperature (K)
4. Density (g/cm3)
5. Acentric factor



To use the `ML-D11` model:
```python
from ml_D11 import ML_D11

model=ML_D11()

model.predict(temp=[112.25], crit_vol=[99.2], crit_temp=[190.4], dens=[0.4222], acent_fact=[0.011])
# Output: array([4.7065659e-05])
```

The outputed D11 values are in cm2/s.

More usage examples are provided in the [`examples.ipynb`](examples.ipynb) file.

