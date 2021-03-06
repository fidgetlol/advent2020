#include <iostream>
#include <unordered_set>
#include <vector>

using namespace std;

int main() {
  unordered_set<long> pool;
  vector<long> nums;
  long n, len = 0;

  while(cin >> n) {
    nums.push_back(n);
    pool.insert(n);
    len++;
  }

  for(long i=0; i < len; i++) {
    if (pool.count(2020-nums[i])!=0) {
      cout << (2020-nums[i]) * nums[i] << endl;
      break;
    }
  }

  return 0;
}
