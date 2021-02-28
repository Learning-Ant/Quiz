package solved.baekjoon.step08;

import java.util.Scanner;

public class Quiz2839 {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		int sugar = sc.nextInt();
		int fiveKilos = sugar/5;	// 5키로로 다 묶음
		sugar%=5;	// 남은 양으로  초기화
		int threeKilos = 0;	// 일단 3키로 0개
		while(fiveKilos>=0) {	// 5키로짜리 소진될때까지
			if(sugar%3==0) {	// 3키로로 나누어 떨어지면
				threeKilos=sugar/3;	// 3키로짜리 계산
				sugar%=3;	// 0저장
				break;
			}
			fiveKilos--;	// 한개 풀고
			sugar+=5;		// 푼 만큼 다시 플러스
		}
		System.out.println(sugar==0?threeKilos+fiveKilos:-1);
		sc.close();
	}

}
