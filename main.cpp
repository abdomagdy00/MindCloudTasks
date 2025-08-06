#include <iostream>
#include <algorithm>

int main() {
    // Read the number of available digits
    int k2, k3, k5, k6;
    std::cout<<"Enter The Number Of K2\n";
    std::cin >> k2 ;
    std::cout<<"Enter The Number Of K3\n";
    std::cin>> k3 ;
    std::cout<<"Enter The Number Of K5\n";
    std::cin>> k5 ;
    std::cout<<"Enter The Number Of K6\n";
    std::cin>> k6;

    long long total_sum = 0;
    int num_256 = std::min({k2, k5, k6});
    total_sum += num_256 * 256;

    // Update the count of digit 2, as it was used to form 256s
    k2 -= num_256;
    int num_32 = std::min(k2, k3);
    total_sum += num_32 * 32;
    std::cout<<"-------------------\n";
    std::cout <<"Total Sum= " << total_sum << std::endl;

    return 0;
}