package solved.baekjoon.step03;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.LinkedList;
import java.util.Queue;

public class Quiz2739 {

	public static void main(String[] args) throws IOException{
		
		// N을 입력받은 뒤, 구구단 N단을 출력하는 프로그램을 작성하시오. 출력 형식에 맞춰서 출력하면 된다.

		// Queue는 FIFO(First In First Out)
		// 그렇게 큰 의미는 없지만 Queue를 활용해서 풀어본다.
		
		Queue<Integer> que = new LinkedList<Integer>();
		for(int i = 0 ; i<9 ; i++) {
			que.add(i+1);
		}
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int dan = Integer.parseInt(br.readLine());
		
		for (int i = 0, size = que.size(); i<size; i++) {
			bw.write(dan+" * "+que.peek()+" = "+(dan*que.peek())+"\n");
			que.remove();
		}
		
		// 위와 같은 방식은 아니지만 Stack의 특성을 이용해서도 풀 수 있다.
		// Stack의 특성은 LIFO(Last In First Out)이므로
		// Stack에 데이터를 주입할 때 가장 먼저 나와야 하는 데이터를 가장 마지막에 넣어준 후
		// 같은 방식으로 하나씩 뽑고, 제거하면서 출력하면 문제의 조건에 부합한다.
		
		// 큐를 쓰지않고 하면 더욱 간단히 해결할 수 있다.
		
		int dan2 = Integer.parseInt(br.readLine());
		for (int i=1;i<10;i++) {
			System.out.println(dan2+" * "+i+" = "+(dan2*i));
			// bw.write(dan2+" * "+i+" = "+(dan2*i)+"\n");
		}
		bw.flush();
		bw.close();
		br.close();
		
	}

}
