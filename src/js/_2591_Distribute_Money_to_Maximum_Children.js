/**
 * @param {number} money
 * @param {number} children
 * @return {number}
 */
var distMoney = function (money, children) {
    money -= children;

    if (money < 0)
        return -1;

    let childrenWith8 = Math.floor(money / 7);

    if (childrenWith8 == children && money % 7 == 0)
        return children;

    if (childrenWith8 == children - 1 && money % 7 == 3)
        return children - 2;

    if (childrenWith8 < children - 1)
        return childrenWith8;

    return children - 1;
};
