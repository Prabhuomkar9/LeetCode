class Solution {
    public int maxArea(int[] height) {
        int water = 0, width = height.length - 1, volume;
        int l = 0, r = width;

        while (l < r) {
            if (height[l] < height[r])
                volume = height[l++] * width--;
            else
                volume = height[r--] * width--;

            if (volume > water)
                water = volume;
        }

        return water;
    }
}
