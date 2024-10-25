class Solution {
    private double dfs(String u, String v, Map<String, Map<String, Double>> graph, Set<String> seen) {
        if (graph.get(u).containsKey(v))
            return graph.get(u).get(v);

        for (Map.Entry<String, Double> entry : graph.get(u).entrySet()) {
            String key = entry.getKey();
            double value = entry.getValue();

            if (seen.contains(key))
                continue;

            seen.add(u);
            double val = dfs(key, v, graph, seen);
            seen.remove(u);
            if (val > 0)
                return value * val;
        }

        return -1.0;
    }

    public double[] calcEquation(List<List<String>> equations, double[] values, List<List<String>> queries) {
        Map<String, Map<String, Double>> graph = new HashMap<>();

        for (int i = 0; i < values.length; i++) {
            String u = equations.get(i).get(0), v = equations.get(i).get(1);

            if (!graph.containsKey(u))
                graph.put(u, new HashMap<>());

            if (!graph.containsKey(v))
                graph.put(v, new HashMap<>());

            graph.get(u).put(v, values[i]);
            graph.get(v).put(u, 1 / values[i]);
        }

        List<Double> ans = new ArrayList<>();

        for (int i = 0; i < queries.size(); i++) {
            String u = queries.get(i).get(0), v = queries.get(i).get(1);

            if (!graph.containsKey(u) || !graph.containsKey(v)) {
                ans.add(-1.0);
            } else {
                Set<String> seen = new HashSet<>();
                ans.add(dfs(u, v, graph, seen));
            }
        }

        double[] resultArray = new double[ans.size()];

        for (int i = 0; i < ans.size(); i++)
            resultArray[i] = ans.get(i);

        return resultArray;
    }
}
