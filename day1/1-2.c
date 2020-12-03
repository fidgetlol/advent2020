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
    for(long j=i; j < len; j++) {
      if (nums[i] + nums[j] < 2020 &&
	  pool.count(2020-(nums[i]+nums[j]))!=0) {
	cout << (2020-(nums[i]+nums[j])) * nums[i] * nums[j] << endl;
	return 0;
      }
    }
  }

  return 0;
}
