class Solution {
    private void dfs(List<List<Integer>> rooms, boolean[] visited, int idx) {
        if (visited[idx])
            return;

        visited[idx] = true;

        for (int i = 0; i < rooms.get(idx).size(); i++)
            dfs(rooms, visited, rooms.get(idx).get(i));
    }

    public boolean canVisitAllRooms(List<List<Integer>> rooms) {
        boolean[] visited = new boolean[rooms.size()];

        dfs(rooms, visited, 0);

        for (int i = 0; i < visited.length; i++)
            if (!visited[i])
                return false;

        return true;
    }
}
