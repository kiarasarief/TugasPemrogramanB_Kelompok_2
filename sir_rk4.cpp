#include <iostream>
#include <fstream>
#include <iomanip>

// Parameter model
const double beta = 1.63e-7;  // infection rate (contoh dari jurnal)
const double gamma = 0.125;   // recovery rate
const double N = 1e6;         // populasi total

// Fungsi turunan SIR
double dS(double S, double I) {
    return -beta * S * I;
}

double dI(double S, double I) {
    return beta * S * I - gamma * I;
}

double dR(double I) {
    return gamma * I;
}

int main() {
    // Inisialisasi variabel
    double S = N - 10;   // 10 orang awal terinfeksi
    double I = 10;
    double R = 0;

    double t = 0.0;
    double t_end = 160;     // hari
    double h = 1.0;         // langkah waktu (hari)

    // Buat file output
    std::ofstream file("sir_output.csv");
    file << "Hari,S,I,R\n";
    file << std::fixed << std::setprecision(2);

    // Simulasi RK4
    while (t <= t_end) {
        file << t << "," << S << "," << I << "," << R << "\n";

        // Hitung k1
        double k1_S = h * dS(S, I);
        double k1_I = h * dI(S, I);
        double k1_R = h * dR(I);

        // Hitung k2
        double k2_S = h * dS(S + 0.5 * k1_S, I + 0.5 * k1_I);
        double k2_I = h * dI(S + 0.5 * k1_S, I + 0.5 * k1_I);
        double k2_R = h * dR(I + 0.5 * k1_I);

        // Hitung k3
        double k3_S = h * dS(S + 0.5 * k2_S, I + 0.5 * k2_I);
        double k3_I = h * dI(S + 0.5 * k2_S, I + 0.5 * k2_I);
        double k3_R = h * dR(I + 0.5 * k2_I);

        // Hitung k4
        double k4_S = h * dS(S + k3_S, I + k3_I);
        double k4_I = h * dI(S + k3_S, I + k3_I);
        double k4_R = h * dR(I + k3_I);

        // Update nilai
        S += (k1_S + 2 * k2_S + 2 * k3_S + k4_S) / 6.0;
        I += (k1_I + 2 * k2_I + 2 * k3_I + k4_I) / 6.0;
        R += (k1_R + 2 * k2_R + 2 * k3_R + k4_R) / 6.0;

        // Update waktu
        t += h;
    }

    file.close();
    std::cout << "Simulasi selesai. Hasil disimpan ke 'sir_output.csv'.\n";

    return 0;
}
