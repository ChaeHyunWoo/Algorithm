package com.programmers.java;

import java.util.Scanner;

public class 직사각형별찍기 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // 사용자한테 2개의 수를 입력받는다.
        int a = sc.nextInt(); // a는 가로 * 개수
        int b = sc.nextInt(); // b는 세로 * 개수

        for(int i=0; i<b; i++) {
            for(int j=0; j<a; j++) {
                System.out.print("*");
            }
            System.out.println();
        }

    }
}
