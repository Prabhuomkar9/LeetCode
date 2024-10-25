/**
 * @param {number[]} nums
 * @return {number}
 */
var numIdenticalPairs = function (nums) {
    const seen = new Map();
    var ans = 0;

    for (let num of nums) {
        if (seen.has(num))
            seen.set(num, seen.get(num) + 1);
        else
            seen.set(num, 0);
        ans += seen.get(num);
    }

    return ans;
};
