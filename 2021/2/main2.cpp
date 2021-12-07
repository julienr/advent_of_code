#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

vector<string> Split(string input, string delim) {
  vector<string> out;
  size_t pos = 0;
  std::string token;
  while ((pos = input.find(delim)) != std::string::npos) {
    token = input.substr(0, pos);
    out.push_back(token);
    input.erase(0, pos + delim.length());
  }
  out.push_back(input);
  return out;
}


int main () {
  ifstream file("input");

  int pos = 0, depth = 0, aim = 0;

  vector<int> numbers;
  string line;
  while (getline(file, line)) {
    auto v = Split(line, " ");
    string command = v[0];
    int amount = atoi(v[1].c_str());
    if (command == "forward") {
      pos += amount;
      depth += aim * amount;
    } else if (command == "up") {
      aim -= amount;
    } else if (command == "down") {
      aim += amount;
    }
  }
  cout << "result: " << pos * depth << endl;

  return EXIT_SUCCESS;
}
