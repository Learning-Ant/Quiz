package unsolved.baekjoon.step01;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Quiz2447 {

	private static BufferedWriter bw = null;
	
	public static void star(int n) throws IOException {
		bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringBuffer sb = new StringBuffer();
		// 첫 줄
		
		
		bw.write(sb.toString());
		bw.flush();
		bw.close();
	}

	public static void main(String[] args) throws IOException{

		/*
		 * 재귀적인 패턴으로 별을 찍어 보자. N이 3의 거듭제곱(3, 9, 27, ...)이라고 할 때, 크기 N의 패턴은 N×N 정사각형
		 * 모양이다. 크기 3의 패턴은 가운데에 공백이 있고, 가운데를 제외한 모든 칸에 별이 하나씩 있는 패턴이다.
		 *   ***
		 *   * *
		 *   ***
		 * N이 3보다 클 경우, 크기 N의 패턴은 공백으로 채워진 가운데의 (N/3)×(N/3) 정사각형을 크기 N/3의 패턴으로 둘러싼 형태이다.
		 */
		/*
		 * 방법 생각 
		 * 결국 바둑판식의 2차원 배열로 생각할 수 있다.
		 * n이 27일 경우 한 변의 길이가 9인 사각형이 3x3의 2차원 배열로 구성되어있는 경우이며
		 * 	    9일 경우 한 변의 길이가 3인 사각형이 3x3의 2차원 배열로 구성되어있고,
		 * 	    3일 경우 한 변의 길이가 1인 사각형(*)이 3x3의 2차원 배열로 구성되어있으며,
		 * 각각의 배열에서 a_11=(1,1)의 요소는 " "를 가지는 경우이다.
		 * 
		 * 결국 (1,1)의 요소는 모두 " "를 가지게끔 메소드를 구성하면 된다.
		 * 이를 판단할 매개변수를 받아서 생각해야할 것 같다.(boolean타입)
		 * 
		 * 여기서 필요한 매개변수는 최소 3개가 넘을 것이다.
		 * 2차원 배열이므로 몇번째 행인지, 몇번째 열인지를 알아낼 매개변수,
		 * 공백이 들어가는 요소인지를 판단할 boolean 매개변수,
		 * 배열 한 변의 길이를 받아줄 매개변수...
		 * 
		 * 최소 4개가 넘는구나.
		 * 
		 * 일단 좀 더 생갹해봐야 할 것 같다.
		 */
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		star(Integer.parseInt(br.readLine()));
		br.close();
	}

}
