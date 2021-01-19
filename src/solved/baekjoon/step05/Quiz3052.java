package solved.baekjoon.step05;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.HashSet;
import java.util.Set;

public class Quiz3052 {

	public static void main(String[] args) throws IOException {

		/*
		 * 두 자연수 A와 B가 있을 때, A%B는 A를 B로 나눈 나머지 이다. 예를 들어, 7, 14, 27, 38을 3으로 나눈 나머지는 1,
		 * 2, 0, 2이다.
		 * 
		 * 수 10개를 입력받은 뒤, 이를 42로 나눈 나머지를 구한다. 그 다음 서로 다른 값이 몇 개 있는지 출력하는 프로그램을 작성하시오.
		 */
		
		/*
		 * 두 가지 방법이 생각난다.
		 * 1. 42로 나눴을 때의 나머지가 인덱스가 되도록 길이가 42인 boolean 타입 배열을 생성하고
		 * 	  값이 true인 배열요소의 개수를 카운팅해서 다른 나머지의 개수를 구하는 방법
		 * 
		 * 2. 중복은 추가적으로 add하지 않는 Collection Set을 이용한다.
		 * 
		 * 두 방법은 결과적으로 그렇게 큰 차이를 보이진 않는다.
		 * 다만 두 번째방법은 collection인 set의 특성이 생각나서 한 번 사용해 보았다.
		 * 절차적 관점에서 봤을 때 첫 번째 방법이 좀 더 직관적으로 이해 하기가 쉬울 것으로 보이긴한다.
		 * set의 특성을 안다면 두번째 방법을 써도 무방할 것 같다.
		 */
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		
		// 1.
		// 11476KB	76ms
		boolean[] isRemainder = new boolean[42];
		int count = 0;
		for(int i =0;i<10;i++) {
			int next = Integer.parseInt(br.readLine());
			isRemainder[next%42]=true;
		}
		for(int i=0;i<isRemainder.length;i++) {
			if(isRemainder[i]) {count++;}
		}
		bw.write(count+"");
		
		// 2.
		// 11580KB	80ms
		Set<Integer> remainders = new HashSet<Integer>();
		for(int i=0;i<10;i++) {
			remainders.add(Integer.parseInt(br.readLine())%42);
		}
		
		bw.write(remainders.size()+"");
		
		
		bw.flush();
		bw.close();
		br.close();
	}

}
