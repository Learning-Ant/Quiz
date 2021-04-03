package solutions.programmers;

import java.util.HashSet;
import java.util.Set;

public class Solution {
    public static int[] solution(int[] lottos, int[] win_nums) {
        int[] answer = {6, 6};
        Set<Integer> l = new HashSet<Integer>();
        for(int i = 0; i < lottos.length; i++) {
        	l.add(lottos[i]);	
        }
        
        
        return answer;
    }
    
    public static void main(String[] args) {
		int[] lottos = {44, 1, 0, 0, 31, 25};
		int[] win_nums = {31, 10, 45, 1, 6, 19};
		
		int[] s = solution(lottos, win_nums);
		
		for(int i =0;i<s.length;i++) {
			System.out.println(s[i] + " ");
		}
	}
}