/**
 * @param {number} n
 * @return {number}
 */
var integerBreak = function (n) {
    if (n == 2)
        return 1;

    if (n == 3)
        return 2;

    let totalPow = Math.floor((n + 2) / 3);
    let twoPow = (3 - (n % 3)) % 3;
    let threePow = totalPow - twoPow;

    return Math.pow(3, threePow) * Math.pow(2, twoPow);
};
