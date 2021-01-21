package solved.baekjoon.step06;

import java.io.BufferedWriter;
import java.io.IOException;
import java.io.OutputStreamWriter;

public class Quiz4673 {
	
	/*
	 * 셀프 넘버는 1949년 인도 수학자 D.R. Kaprekar가 이름 붙였다. 양의 정수 n에 대해서 d(n)을 n과 n의 각 자리수를
	 * 더하는 함수라고 정의하자. 예를 들어, d(75) = 75+7+5 = 87이다.
	 * 
	 * 양의 정수 n이 주어졌을 때, 이 수를 시작해서 n, d(n), d(d(n)), d(d(d(n))), ...과 같은 무한 수열을 만들 수
	 * 있다.
	 * 
	 * 예를 들어, 33으로 시작한다면 다음 수는 33 + 3 + 3 = 39이고, 그 다음 수는 39 + 3 + 9 = 51, 다음 수는 51
	 * + 5 + 1 = 57이다. 이런식으로 다음과 같은 수열을 만들 수 있다.
	 * 
	 * 33, 39, 51, 57, 69, 84, 96, 111, 114, 120, 123, 129, 141, ...
	 * 
	 * n을 d(n)의 생성자라고 한다. 위의 수열에서 33은 39의 생성자이고, 39는 51의 생성자, 51은 57의 생성자이다. 생성자가 한
	 * 개보다 많은 경우도 있다. 예를 들어, 101은 생성자가 2개(91과 100) 있다.
	 * 
	 * 생성자가 없는 숫자를 셀프 넘버라고 한다. 100보다 작은 셀프 넘버는 총 13개가 있다. 1, 3, 5, 7, 9, 20, 31, 42,
	 * 53, 64, 75, 86, 97
	 * 
	 * 10000보다 작거나 같은 셀프 넘버를 한 줄에 하나씩 출력하는 프로그램을 작성하시오.
	 */
	/*
	 * keyword : 수열, 생성자
	 * 어떤 숫자(생성자)로 만들 수 있는 d(n)의 수열은 재귀적 호출로 볼 수 있다.
	 * 일단 이 문제에서의 생성자 개념을 나는 파라미터의 개념으로 도입했다.
	 * 파라미터로 인덱스가 생성숫자인지를 알리는 boolean타입의 배열과 숫자(생성자)를 받는다.
	 * 파라미터로 받은 숫자로 다음 수열을 생성하고,
	 * 재귀호출하여 파라미터로 만들어진 다음 수와 판단할 배열을 다시 넘겨준다.
	 * 재귀호출의 종료 판단기준은 받은 파라미터가 배열의 길이(셀프넘버를 구하려는 범위)를 벗어났는가로 설정한다.
	 * 이렇게 한 후 내가 원하는 범위값+1의 길이를 가지는 boolean타입 배열을 생성한다.
	 * 범위값에 +1을 해주는 이유는 인덱스와 셀프넘버를 맞춰주기 위함이다. 
	 */
	// 11652KB	112ms
	public static void d(int n, boolean[] isNotSelfNum) {
		if(n==0||n>isNotSelfNum.length) return;
		int result = n;
		while(n/10!=0) {
			result += n%10;
			n/=10;
		}
		result += n;
		if(result<isNotSelfNum.length) {
			isNotSelfNum[result]=true;
			d(result, isNotSelfNum);	
		}
	}
	
	public static void main(String[] args) throws IOException{

		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		boolean[] isNotSelfNum = new boolean[10001];
		// 초기값 false
		// true로 바뀌면 Self Number가 아니다
		// 걸러내는 방법은 수열을 생각
		// n, d(n), d(d(n)), d(d(d(n))), ... 재귀호출
		for(int i=1;i<isNotSelfNum.length;i++) {
			d(i,isNotSelfNum);
		}
		for(int i=1;i<isNotSelfNum.length;i++) {
			if(!isNotSelfNum[i]) {
				bw.write(i+"\n");
			}
		}
		
		bw.flush();
		bw.close();
		
	}

}
