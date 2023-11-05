class Solution {
    public int getWinner(int[] arr, int k) {
        int curr = arr[0], count = 0;

        for (int i = 1; i < arr.length; i++, count++) {
            if (count == k)
                break;

            if (arr[i] > curr) {
                curr = arr[i];
                count = 0;
            }
        }

        return curr;
    }
}
