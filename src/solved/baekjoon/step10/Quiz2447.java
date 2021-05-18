package solved.baekjoon.step10;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Quiz2447 {

	public static void setStar(char[][] stars, int x, int y, int size) {
		if(size == 1) {
			stars[x][y] = '*';
			return;
		}
		
		int a = size / 3;
		
		for(int i = 0; i < 3; i++) {
			for(int j = 0; j < 3; j++) {
				if(i * j != 1)
					setStar(stars, x + i * a, y + j * a, a);
			}
		}
	}
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int size = Integer.parseInt(br.readLine());
		char stars[][] = new char[size][size];
		
		for(int i = 0; i < stars.length; i++) {
			for(int j = 0; j < stars.length; j++) {
				stars[i][j] = ' ';
			}
		}
		
		setStar(stars, 0, 0, size);
		
		for(int i = 0; i < stars.length; i++) {
			for(int j = 0; j < stars[i].length; j++) {
				bw.write(stars[i][j]);
			}
			bw.write("\n");
		}
		
		
		bw.flush();
		bw.close();
		br.close();
	}

}
