class Solution {
    public int[] successfulPairs(int[] spells, int[] potions, long success) {
        int i = 0;
        int[] ans = new int[spells.length];

        Arrays.sort(potions);

        for(int spell : spells){
            int l = 0, r = potions.length - 1;

            while(l <= r){
                int m = l + (r - l) / 2;
                long product = (long)spell * potions[m];

                if(product < success)
                    l = m + 1;
                else
                    r = m - 1;
            }

            ans[i++] = potions.length - l;
        }

        return ans;
    }
}
