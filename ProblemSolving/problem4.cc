class Solution
{
public:
    void quicksort(vector<int> &nums, int first, int last)
    {
        int i, j, pivot, temp;
        if (first < last)
        {
            pivot = first;
            i = first;
            j = last;
            while (i < j)
            {
                while (nums[i] <= nums[pivot] && i < last)
                    i++;
                while (nums[j] > nums[pivot])
                    j--;
                if (i < j)
                {
                    temp = nums[i];
                    nums[i] = nums[j];
                    nums[j] = temp;
                }
            }
            temp = nums[pivot];
            nums[pivot] = nums[j];
            nums[j] = temp;
            quicksort(nums, first, j - 1);
            quicksort(nums, j + 1, last);
        }
    }
    int arrayPairSum(vector<int> &nums)
    {
        int sum = 0;
        quicksort(nums, 0, nums.size() - 1);

        for (int i = 0; i < nums.size(); i = i + 2)
        {
            sum = sum + nums[i];
        }

        return sum;
    }
};