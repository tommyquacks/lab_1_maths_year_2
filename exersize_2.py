import pandas as pd 

def f(x):
    return x**4

def exact_deriv(x):
    return 4 * x**3

def approx_deriv(x, dx):
    return (f(x + dx) - f(x)) / dx

def abs_error(approx, exact):
    return abs(approx - exact)

def rel_error(approx, exact):
    return abs_error(approx, exact) / abs(exact)

# For x=1
exact1 = exact_deriv(1)
data1 = []
for j in range(3, 20):
    dx = 10**(-j)
    approx = approx_deriv(1, dx)
    ae = abs_error(approx, exact1)
    re = rel_error(approx, exact1)
    data1.append({
        'j': j,
        'Δx': dx,
        'Approx': approx,
        'Abs Error': ae,
        'Rel Error': re
    })

df1 = pd.DataFrame(data1)
df1.to_csv('derivative_table_x1.csv', index=False)  # Save to CSV file
print("Table for x=1 saved to 'derivative_table_x1.csv'")

# For x=10
exact10 = exact_deriv(10)
data10 = []
for j in range(3, 20):
    dx = 10**(-j)
    approx = approx_deriv(10, dx)
    ae = abs_error(approx, exact10)
    re = rel_error(approx, exact10)
    data10.append({
        'j': j,
        'Δx': dx,
        'Approx': approx,
        'Abs Error': ae,
        'Rel Error': re
    })

df10 = pd.DataFrame(data10)
df10.to_csv('derivative_table_x10.csv', index=False)  # Save to CSV file
print("Table for x=10 saved to 'derivative_table_x10.csv'")
