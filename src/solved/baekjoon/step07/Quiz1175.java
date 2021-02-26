package solved.baekjoon.step07;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Quiz1175 {
	// value중 원하는 값을 가진 key값 반환하기
		public static <K,V> K getKey(Map<K,V> map, V value) {
			for(K key : map.keySet()) {
				if(value.equals(map.get(key))) {
					return key;
				}
			}
			
			return null;
		}
		
		// 원하는 value를 가진 key들이 여러개 있을 수 있으니 List로 반환
		public static List<Character> getKeys(Map<Character,Integer> map ,Integer value) {
			List<Character> keys = new ArrayList<Character>();
			for (Character key : map.keySet()) {
				if(value.equals(map.get(key))) {
					keys.add(key);
				}
			}
			return keys;
		}
		
		// value 값 중 에서 가장 큰 값을 반환
		public static int getMaxValue(Map<Character, Integer> map) {
			int max = 0;
			for(Character key : map.keySet()) {
				if ( max < map.get(key)) {
					max = map.get(key);
				}
			}
			return max;
		}
		
		public static void main(String[] args) throws Exception{
			BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
			char[] charArray = br.readLine().toUpperCase().toCharArray();
			HashMap<Character, Integer> map = new HashMap<>();
			for(int i = 0 ; i < charArray.length ; i++) {
				if(!map.containsKey(charArray[i])) {
					map.put(charArray[i], 1);
				} else {
					map.put(charArray[i], map.get(charArray[i])+1);
				}
			}
			
			int max = getMaxValue(map);
			List<Character>	keys = getKeys(map, max);
			if (keys.size()!=1) {
				System.out.println("?");
			} else {
				System.out.println(keys.get(0));
			}
		}

}
