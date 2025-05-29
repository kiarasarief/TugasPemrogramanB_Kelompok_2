import pandas as pd
import matplotlib.pyplot as plt

# Baca data CSV hasil simulasi SIR
data = pd.read_csv('sir_output.csv')

# Konfigurasi default tampilan
# plt.style.use('seaborn-darkgrid') # Style ini sudah tidak valid di versi matplotlib baru
plt.style.use('seaborn-v0_8-darkgrid')  # Menggunakan style yang kompatibel
plt.rcParams.update({'font.size': 10})

# Grafik 1: Susceptible
plt.figure(figsize=(10, 5))
plt.plot(data['Hari'], data['S'], label='Susceptible (S)', color='blue')
plt.title('Figure 4.1 - Susceptible Population over Time')
plt.xlabel('Hari')
plt.ylabel('Jumlah Individu')
plt.legend()
plt.tight_layout()
plt.savefig('figure_4_1_susceptible.png', dpi=300)

# Grafik 2: Infected
plt.figure(figsize=(10, 5))
plt.plot(data['Hari'], data['I'], label='Infected (I)', color='red')
plt.title('Figure 4.3 - Infected Population over Time')
plt.xlabel('Hari')
plt.ylabel('Jumlah Individu')
plt.legend()
plt.tight_layout()
plt.savefig('figure_4_3_infected.png', dpi=300)

# Grafik 3: Recovered
plt.figure(figsize=(10, 5))
plt.plot(data['Hari'], data['R'], label='Recovered (R)', color='green')
plt.title('Figure 4.5 - Recovered Population over Time')
plt.xlabel('Hari')
plt.ylabel('Jumlah Individu')
plt.legend()
plt.tight_layout()
plt.savefig('figure_4_5_recovered.png', dpi=300)

# Grafik 4: Gabungan S, I, R
plt.figure(figsize=(10, 5))
plt.plot(data['Hari'], data['S'], label='S (Susceptible)', color='blue')
plt.plot(data['Hari'], data['I'], label='I (Infected)', color='red')
plt.plot(data['Hari'], data['R'], label='R (Recovered)', color='green')
plt.title('Figure 4.7 - SIR Model Curve (RK4 Method)')
plt.xlabel('Hari')
plt.ylabel('Jumlah Individu')
plt.legend()
plt.tight_layout()
plt.savefig('figure_4_7_sir_combined.png', dpi=300)

# Grafik 5: Subplot gabungan
fig, axs = plt.subplots(3, 1, figsize=(10, 9), sharex=True)

axs[0].plot(data['Hari'], data['S'], color='blue')
axs[0].set_title('Susceptible (S)')

axs[1].plot(data['Hari'], data['I'], color='red')
axs[1].set_title('Infected (I)')

axs[2].plot(data['Hari'], data['R'], color='green')
axs[2].set_title('Recovered (R)')
axs[2].set_xlabel('Hari')

for ax in axs:
    ax.set_ylabel('Jumlah')

plt.suptitle('Figure 4.12 - Subplot of S, I, and R (RK4)', fontsize=14)
plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig('figure_4_12_subplots.png', dpi=300)

plt.show()
