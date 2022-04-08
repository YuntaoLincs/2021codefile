// 问题描述：Given an integer array nums, return true if 
//any value appears at least twice in the array, and return 
//false if every element is distinct.

// Constraints:
// 1 <= nums.length <= 10^5
// -10^9 <= num[i] <= 10^9
// 做前思路:先排序，再比较各个位置的数字大小
// 结果：有思路但不知道怎么开始
// 下面为答案解析
//int cmp(const void* _a, const void* _b) { # 
//    int a = *(int*)_a, b = *(int*)_b;
//    return a - b;
//}
//
//bool containsDuplicate(int* nums, int numsSize) { 
//    qsort(nums, numsSize, sizeof(int), cmp); # 排序
//    for (int i = 0; i < numsSize - 1; i++) {
//        if (nums[i] == nums[i + 1]) {
//            return true;
//        }
//    }
//    return false;
//}
//
bool containsDuplicate(int* nums, int numsSize){

}
