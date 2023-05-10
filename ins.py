import numpy as np
import scipy

# cek versi NumPy dan SciPy
print("Versi NumPy:", np.__version__)
print("Versi SciPy:", scipy.__version__)

# cek persyaratan versi NumPy oleh SciPy
print("Persyaratan versi NumPy oleh SciPy:", scipy.__numpy_version__)

# upgrade NumPy ke versi yang sesuai
pip install numpy>=1.16.5,<1.23.0 --upgrade

# cek versi NumPy setelah diupgrade
print("Versi NumPy setelah diupgrade:", np.__version__)