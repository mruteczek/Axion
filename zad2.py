import numpy as np

# Definujemy stany bazowe
ket0 = np.array([1,0],dtype= complex)
ket1 = np.array([1,0],dtype= complex)

# Definiujemy bramki
X = np.array([[0, 1], [1, 0]], dtype=complex)
Z = np.array([[1, 0], [0, -1]], dtype=complex)
H = 1 / np.sqrt(2) * np.array([[1, 1], [1, -1]], dtype=complex)
I = np.array([[1,0],[0,1]], dtype=complex)
CNOT = np.array(
    [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]], dtype=complex
)
def Ry(theta):
    return np.array(
        [
            [np.cos(theta / 2), -np.sin(theta / 2)],
            [np.sin(theta / 2), np.cos(theta / 2)],
        ],
        dtype=complex,
    )

hadamard =  H @ (H @ ket0)
print( f"ket0={ket0},hadamard={hadamard}")
 
#obwód bella według schematu z wykładu
bell =  CNOT @ (np.kron(I,H) @ np.kron(ket0,ket0))
print(bell)

def pomiarstanu(wektor):
  v0 = abs(wektor[0]) ** 2
  v1 = abs(wektor[1]) ** 2
  v2 = abs(wektor[2]) ** 2
  v3 = abs(wektor[3]) ** 2

  return (
      f"prawdopodobieństwo stanu 00={v0}, "
      f"prawdopodobieństwo stanu 11={v1}, "
      f"prawdopodobieństwo stanu 01={v2}, "
      f"prawdopodobieństwo stanu 10={v3}"
  )
print(pomiarstanu(bell))







