class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    productExceptSelf(nums: number[]): number[] {
        let l = nums.length
        let prefix = new Array(l).fill(1);
        let suffix = new Array(l).fill(1);
        for (let i = 1; i < l; i++)
        {
            prefix[i] = nums[i-1] * prefix[i-1]
            suffix[l-1-i] = nums[l-i] * suffix[l-i]
        }
        return prefix.map((x,i)=>x*suffix[i])
    }
}
