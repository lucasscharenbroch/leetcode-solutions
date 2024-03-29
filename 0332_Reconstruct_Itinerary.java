// DFS and Backtracking
class Solution {
    public List<String> findItinerary(List<List<String>> tickets) {
        tickets.sort((t1, t2) -> { // sort tickets by to-airport, lexographically
            return t1.get(1).compareTo(t2.get(1));
        });
            
        ArrayList<String> order = new ArrayList<>(); // order of itinerary
        boolean[] used = new boolean[tickets.size()];
        
        HashMap<String, List<Integer>> connections = new HashMap<>(); // (airport) : {ticket ids that are from airport}
        
        // populate connections with directed edges
        for(int i = 0; i < tickets.size(); i++) {
            String from = tickets.get(i).get(0);
            if(connections.get(from) == null) connections.put(from, new ArrayList<>());
            connections.get(from).add(i);
        }
        
        dfs(tickets, order, used, "JFK", connections); // we assume that this returns true and correctly fills order
        return order;
    }
    
    boolean dfs(List<List<String>> tickets, List<String> order, boolean[] used, String current, 
                     HashMap<String, List<Integer>> connections) {
        if(order.size() == used.length) {
            order.add(current);
            return true;
        }
        
        if(connections.get(current) == null) return false;
        for(Integer ticket : connections.get(current)) { // since tickets is sorted, this will greedily choose
                                                         // the lowest ticket, lexographically
            if(!used[ticket]) {
                used[ticket] = true;
                order.add(tickets.get(ticket).get(0));
                if(dfs(tickets, order, used, tickets.get(ticket).get(1), connections)) return true;
                order.remove(order.size() - 1);
                used[ticket] = false;
            }
        }
        
        return false;
    }
}

// Eulerian Path
class Solution {
    public List<String> findItinerary(List<List<String>> tickets) {
        HashMap<String, PriorityQueue<String>> outEdges = new HashMap<>();
        // use dfs to find an Eulerian path; use priority queues to explore edges in lexographical order
        
        for(List<String> ticket : tickets) { // populate outEdges
            String from = ticket.get(0);
            String to = ticket.get(1);
            
            outEdges.putIfAbsent(from, new PriorityQueue<>());
            outEdges.get(from).add(to);
        }
        
        LinkedList<String> solution = new LinkedList<>();
        findEulerianPath("JFK", outEdges, solution);
        return solution;
    }
    
    private void findEulerianPath(String current, HashMap<String, PriorityQueue<String>> outEdges,
                                  LinkedList<String> result) {
        
        // depth-first explore outgoing edges until the node "gets stuck"
        if(outEdges.get(current) != null) {
            while(!outEdges.get(current).isEmpty()) {
                findEulerianPath(outEdges.get(current).poll(), outEdges, result);
            }
        }
        
        // when the node is "stuck", it can be appended to the front of the solution
        result.add(0, current);
    }
}
