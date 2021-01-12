package solved.baekjoon.step01;

import java.io.BufferedWriter;
import java.io.IOException;
import java.io.OutputStreamWriter;

public class Quiz10718 {

	public static void main(String[] args) throws IOException{

		/*
		 * ACM-ICPC 인터넷 예선, Regional, 그리고 World Finals까지 이미 2회씩 진출해버린 kriii는 미련을 버리지 못하고
		 * 왠지 모르게 올 해에도 파주 World Finals 준비 캠프에 참여했다.
		 * 
		 * 대회를 뜰 줄 모르는 지박령 kriii를 위해서 격려의 문구를 출력해주자.
		 */
		/*
		 * 앞서 풀었던 Quiz2557에서 StringBuffer를 이용한 방법으로
		 * StringBuffer클래스의 객체 sb에 "강한친구 대한육군"을 저장하고 두번 출력한다.
		 * 이때 for문을 이용하면 원하는 수만큼 가능하긴하지만 해당 문제는 두 줄만 출력하면 되니
		 * 바로 객체에 저장하면서 출력해본다.
		 * 11500KB 72ms
		 */
		StringBuffer sb = new StringBuffer("강한친구 대한육군");
		sb.append(System.lineSeparator());
		sb.append("강한친구 대한육군");
		sb.trimToSize();
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		bw.write(sb.toString());
		bw.flush();
		bw.close();
	}

}
