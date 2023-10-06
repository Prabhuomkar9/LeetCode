/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function (nums) {
    let ans = nums[0], count = 0;

    for (let num of nums) {
        if (count == 0)
            ans = num;

        if (ans == num)
            count++;
        else
            count--;
    }

    return ans;
};
