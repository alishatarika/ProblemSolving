class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {

       vector<int> target1;
    vector<int> target2;

    for (int i = 0; i < nums.size() -1; i++)
    {
      for(int j=i+1;j<nums.size();j++)
        if (nums[i] + nums[j] == target)
        {
            
            target1.push_back(i);
            target1.push_back(j);
            
            return target1;
        }
    }
    return target1;
}
};