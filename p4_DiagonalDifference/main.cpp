#include <iostream>
#include <vector>
#include <cmath> 

int diagonalDifference(const std::vector<std::vector<int>> & arr) {
    int n = arr.size();
    int primary_diagonal_sum = 0;
    int secondary_diagonal_sum = 0;

    for (int i = 0; i < n; ++i) {
        // Summing the primary diagonal: arr[i][i]
        primary_diagonal_sum += arr[i][i];
        // Summing the secondary diagonal: arr[i][n - 1 - i]
        secondary_diagonal_sum += arr[i][n - 1 - i];
    }
    return std::abs(primary_diagonal_sum - secondary_diagonal_sum);
}

int main() {
    int n;
    std::cout<<"Enter Number Of Row and Columns Of  matrix\n";
    std::cin >> n;
    std::vector<std::vector<int>> arr(n, std::vector<int>(n));

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            std::cout<<"arr["<<i<<"]["<<j<<"]"<<"=";
            std::cin >> arr[i][j];
        }
    }

    int result = diagonalDifference(arr);
    std::cout << "Result= "<<result << std::endl;

    return 0;
}