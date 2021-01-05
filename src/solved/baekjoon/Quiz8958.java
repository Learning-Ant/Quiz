package solved.baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Quiz8958 {

	public static void main(String[] args) {

		/*
		 * "OOXXOXXOOO"와 같은 OX퀴즈의 결과가 있다. O는 문제를 맞은 것이고, X는 문제를 틀린 것이다. 문제를 맞은 경우 그 문제의
		 * 점수는 그 문제까지 연속된 O의 개수가 된다. 예를 들어, 10번 문제의 점수는 3이 된다.
		 * 
		 * "OOXXOXXOOO"의 점수는 1+2+0+0+1+0+0+1+2+3 = 10점이다.
		 * 
		 * 	OX퀴즈의 결과가 주어졌을 때, 점수를 구하는 프로그램을 작성하시오.
		 * 
		 * 	첫째 줄에 테스트 케이스의 개수가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 길이가 0보다 크고 80보다 작은 문자열이 주어진다.
		 * 
		 *  문자열은 O와 X만으로 이루어져 있다.
		 *  
		 *  예시)
		 *  5
		 *	OOXXOXXOOO
		 *	OOXXOOXXOO
		 * 	OXOXOXOXOXOXOX
		 *	OOOOOOOOOO
		 *	OOOOXOOOOXOOOOX
		 *
		 *	출력)
		 *	10
		 *	9
		 *	7
		 *	55
		 *	30
		 */
		
		/*
		 * 풀이 생각 
		 * delimiter가 "X"인 문자열인 경우라고 생각하면, 각각의 케이스들을 X로 토큰화시켜주고, 해당 토큰의 길이를 구하여
		 * 1~length까지를 등차수열의 합으로 구해준 후 각 토큰의 총합을 구하면 해당 문자열의 점수에 해당한다.
		 */
		
		BufferedReader br = null;
		int testCase = 0;
		int[] sumList = null;
		try {
			br = new BufferedReader(new InputStreamReader(System.in));
			testCase = Integer.parseInt(br.readLine());
			sumList = new int[testCase];
			for(int i = 0 ; i<testCase ; i++) {
				String str = br.readLine();
				StringTokenizer st = new StringTokenizer(str,"X");
				int sum = 0;
				while(st.hasMoreTokens()) {
					int n = st.nextToken().length();
					sum += n*(n+1)/2;
				}
				sumList[i] = sum;
			}
		} catch (IOException e) {
			e.printStackTrace();
		} finally {
			try {
				if (br!=null) br.close();
			} catch (IOException e) {
				e.printStackTrace();
			}
		}
		for (int i = 0 ; i<sumList.length ; i++) {
			System.out.println(sumList[i]);
		}

	}

}
