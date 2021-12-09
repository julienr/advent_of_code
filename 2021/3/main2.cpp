#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <utility>
#include <cmath>

using namespace std;

string filter(const vector<string>& numbers, bool most_common) {
  vector<string> remaining(numbers.begin(), numbers.end());
  int bit = 0;
  while (remaining.size() > 1) {
    int num_0 = 0;
    int num_1 = 0;
    for (const string& s: remaining) {
      if (s[bit] == '0') {
        num_0++;
      } else {
        num_1++;
      }
    }
    char filter;
    if (num_1 >= num_0) {
      filter = most_common ? '1' : '0';
    } else {
      filter = most_common ? '0' : '1';
    }

    vector<string> tmp;
    for (const string& s: remaining) {
      if (s[bit] == filter) {
        tmp.push_back(s);
      }
    }
    bit++;
    remaining = tmp;
  }
  return remaining[0];
}

int binary_to_decimal(const string& number) {
  int out = 0;
  for (int i = 0; i < number.size(); ++i) {
    if (number[i] == '1') {
      out += 1 << (number.size() - i - 1);
    }
  }
  return out;
}


int main () {
  ifstream file("input");

  vector<string> numbers;
  vector<pair<int, int>> counts;
  string line;
  while (getline(file, line)) {
    if (counts.empty()) {
      counts.resize(line.size(), {0, 0});
    }
    for (int i = 0; i < line.size(); ++i) {
      if (line[i] == '0') {
        counts[i].first += 1;
      } else {
        counts[i].second += 1;
      }
    }
    numbers.push_back(line);
  }

  string oxygen = filter(numbers, true);
  string co2 = filter(numbers, false);

  cout << "oxygen: " << oxygen << " " << binary_to_decimal(oxygen) << endl;
  cout << "co2: " << co2 << " " << binary_to_decimal(co2) << endl;
  cout << binary_to_decimal(oxygen) * binary_to_decimal(co2) << endl;

  return EXIT_SUCCESS;
}
