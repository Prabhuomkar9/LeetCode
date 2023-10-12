/**
 * *********************************************************************
 * // This is the MountainArray's API interface.
 * // You should not implement it, or speculate about its implementation
 * *********************************************************************
 *
 * int get(MountainArray *, int index);
 * int length(MountainArray *);
 */

int findInMountainArray(int target, MountainArray *mountainArr)
{
    int len = length(mountainArr);
    int l = 1, r = len - 2, peak = -1;

    while (l <= r)
    {
        int m = (l + r) / 2;
        int prevVal = get(mountainArr, m - 1);
        int currVal = get(mountainArr, m);
        int nextVal = get(mountainArr, m + 1);

        if (prevVal < currVal && currVal > nextVal)
        {
            if (currVal == target)
                return m;
            peak = m;
            break;
        }
        else if (prevVal < currVal && currVal < nextVal)
            l = m + 1;
        else
            r = m - 1;
    }

    l = 0;
    r = peak - 1;

    while (l <= r)
    {
        int m = (l + r) / 2;
        int currVal = get(mountainArr, m);

        if (currVal == target)
            return m;
        else if (currVal < target)
            l = m + 1;
        else
            r = m - 1;
    }

    l = peak + 1;
    r = len - 1;

    while (l <= r)
    {
        int m = (l + r) / 2;
        int currVal = get(mountainArr, m);

        if (currVal == target)
            return m;
        else if (currVal < target)
            r = m - 1;
        else
            l = m + 1;
    }

    return -1;
}
