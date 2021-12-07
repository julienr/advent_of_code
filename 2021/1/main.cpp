#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

int process(const vector<int>& numbers) {
  int num_incr = 0;
  for (int i = 1; i < numbers.size(); ++i) {
    if (numbers[i] > numbers[i - 1]) {
      num_incr++;
    }
  }
  return num_incr;
}

int main () {
  ifstream file("input");

  vector<int> numbers;
  string line;
  while (getline(file, line)) {
    numbers.push_back(atoi(line.c_str()));
  }

  cout << process(numbers) << endl;

  return EXIT_SUCCESS;
}
