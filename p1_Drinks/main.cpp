#include <iostream>
#include <iomanip>

int main() {
    int n;
    std::cout<<"Enter Number Of n\n";
    std::cin >> n;

    double sum_of_percentages = 0.0;
    for (int i = 0; i < n; ++i) {
        double p;
        std::cout<<"Enter percentage["<<i+1<<"] \n";
        std::cin >> p;
        sum_of_percentages += p;
    }

    double final_percentage = sum_of_percentages / n;
    
    std::cout << std::fixed << std::setprecision(12) << final_percentage << std::endl;

    return 0;
}