package com.programmers.java;

public class 행렬의덧셈 {
    public int[][] solution(int[][] arr1, int[][] arr2) {
        int[][] answer = {};
        // arr1의 행과 열의 길이만큼 초기화 -> arr1와 arr2 행렬 크기는 같아서 arr2써도 된다.
        answer = new int[arr1.length][arr1[0].length];

        // arr1 배열 행의 길이만큼 반복문을 돌림. (행번 = i)
        for(int i=0; i<arr1.length; i++)
            // arr1 배열의 i행의 열의 길이만큼 반복문 돌림 (열번 = j)
            for(int j=0; j<arr1[i].length; j++)
                // 행번호,열번호를 이용해 같은 위치끼리 덧셈
                answer[i][j] = arr1[i][j] + arr2[i][j];
        return answer;
    }
}