class Solution {
    public String predictPartyVictory(String senate) {
        int rAlive = 0, dAlive = 0;
        Queue<Character> guys = new LinkedList<>();

        for (char guy : senate.toCharArray()) {
            guys.add(guy);
            if (guy == 'R')
                rAlive++;
            else
                dAlive++;
        }

        int rToKill = 0, dToKill = 0;
        while (rAlive > 0 && dAlive > 0) {
            char currentGuy = guys.remove();
            if (currentGuy == 'R') {
                if (rToKill > 0) {
                    rToKill--;
                    rAlive--;
                } else {
                    dToKill++;
                    guys.add(currentGuy);
                }
            } else {
                if (dToKill > 0) {
                    dToKill--;
                    dAlive--;
                } else {
                    rToKill++;
                    guys.add(currentGuy);
                }
            }
        }

        if (rAlive > 0)
            return "Radiant";
        else
            return "Dire";
    }
}
