# FarmGBM12

## Overview
FarmGBM12 simulates 1D Brownian Motion and plots displacement over time for the D400 Research Computing course.

## Installation
Ensure Python is installed. Install packages with:
```bash
pip install -r requirements.txt
```

## Usage
1. Clone the repository:
    ```bash
    git clone https://github.com/Farmer122/farmgbm12.git
    ```
2. Navigate to the project directory:
    ```bash
    cd farmgbm12
    ```

## Example:

```python
from farmgbm12.GeometricBrownian import pygbm

y0 =1.0
mu = 0.05
sigma = 0.2
T = 1.0
N = 100


simulator = pygbm(y0, mu, sigma, T, N)

simulator.simulate()
simulator.plot()
```

## Contributing
Fork the repository and submit a pull request.

## License
MIT License.

## Contact
Questions? Contact Jamal Lawal at jamallawal1000@gmail.com
