// 순열 구합니다.
// 순열을 순회합니다.
//      최대 던전 수를 구합니다.
//      max = Math.max(max, "최대 던전 수");
// max를 반환합니다.

import java.util.*;

class Solution {
    private void permutations(ArrayList<Integer> list, int k, int[][] dungeons, int size, int depth, int count, boolean[] visited) {
        if (size == depth) {
            list.add(count);
            return;
        }
        
        for (int i = 0; i < dungeons.length; i++) {
            if (visited[i]) continue;
            if (dungeons[i][0] > k) {
                list.add(count);
                continue;
            }
            visited[i] = true;
            permutations(list, k - dungeons[i][1], dungeons, size, depth + 1, count + 1, visited);
            visited[i] = false;
        }
    }
    
    public int solution(int k, int[][] dungeons) {
        ArrayList<Integer> countList = new ArrayList<>(){{
            add(0);
        }};
        boolean[] visited = new boolean[dungeons.length];
        permutations(countList, k, dungeons, dungeons.length, 0, 0, visited);
        
        return Collections.max(countList);
    }
}