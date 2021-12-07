#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

int process(const vector<int>& numbers) {
  int num_incr = 0;
  for (int i = 3; i < numbers.size(); ++i) {
    int win1 = numbers[i - 3] + numbers[i - 2] + numbers[i - 1];
    int win2 = numbers[i - 2] + numbers[i - 1] + numbers[i];
    if (win2 > win1) {
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
