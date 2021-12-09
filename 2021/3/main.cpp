#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <utility>
#include <cmath>

using namespace std;

int main () {
  ifstream file("input");

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
  }

  int gamma = 0;
  int epsilon = 0;
  for (int i = 0; i < counts.size(); ++i) {
    int v = (counts[i].second > counts[i].first) ? 1 : 0;
    if (v == 1) {
      gamma += 1 << (counts.size() - i - 1);
    } else {
      epsilon += 1 << (counts.size() - i - 1);
    }
    cout << "gamma: " << gamma << endl;
  }
  cout << gamma << endl;
  cout << epsilon << endl;
  cout << "result: " << gamma * epsilon << endl;

  return EXIT_SUCCESS;
}
