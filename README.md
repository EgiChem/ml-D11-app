# ML-D11-app

Prediction of self-diffusion of polar/non-polar, spherical/non-spherical, and hydrogen-bonding molecules in liquids, compressed gases or supercritical fluids.


The machine learning models were trained with a database of 5551 experimental data points from over 216 systems.

## Available models

The AARD achieved by the models ML5-D11 and ML8-D11 in the test set were 9.06 % and 7.14 %, respectively.

| Model            | Input parameters required                                                                    |
|------------------|----------------------------------------------------------------------------------------------|
| `ML5-D11`     | temperature, critical volume, critical temperature, density and acentric factor                                                   |
| `ML8-D11`   | temperature, critical volume, critical temperature, density, acentric factor, pressure  and substance identifier (SMILES)                                                   |
                                  


## Installation

1. Download this repository by clicking `Code` > `Download ZIP`. Unzip the folder.

2. Install Python. We recommend a installing the [Anaconda Distribution](https://www.anaconda.com/download) or [Miniconda](https://docs.conda.io/projects/miniconda/en/latest/miniconda-install.html).

3. Open the Anaconda Prompt and change the directory to where you extracted the repository files: `cd path/to/folder`.

3. Create a `conda` virtual environment using the provided `environment.yml` file: `conda env create -f environment.yml`

4. Activate the environment with: `conda activate ml`.

5. You can now use the models following instructions bellow either in a `.py` script file or in a Jupyter Notebook (already provided in the environment by running `jupyter lab`).

## Usage

To use the `ML5-D11` model:
Call the program and provide the properties:

1. Temperature (K)
2. Critical volume (cm3/mol)
3. Critical temperature (K)
4. Density (g/cm3)
5. Acentric factor

To use the `ML8-D11` model:
Call the program and provide the properties:

1. Temperature (K)
2. Critical volume (cm3/mol)
3. Critical temperature (K)
4. Density (g/cm3)
5. Acentric factor
6. Pressure (bar)
7. Substance identifier (SMILES)

To use the `ML5-D11` model:
```python
from ml_D11 import ML5_D11

model=ML5_D11()

model.predict(temp=[112.25], crit_vol=[99.2], crit_temp=[190.4], dens=[0.4222], acent_fact=[0.011])
# Output: array([4.7065659e-05])
```

To use the `ML-D11` model:


```python
from ml_D11 import ML8_D11

model=ML8_D11()

model.predict(temp=[112.25], crit_vol=[99.2], crit_temp=[190.4], dens=[0.4222], acent_fact=[0.011], press=[8.61], smiles=['C'])

# Output: array([4.71234228e-05])
```

The outputed D11 values are in cm2/s.

More usage examples are provided in the [`examples.ipynb`](examples.ipynb) file.

