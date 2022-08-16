package com.programmers.java;


public class x만큼간격이있는n개의숫자 {
    public long[] solution(int x, int n) {
        long[] answer = {};
        // answer에 n개 만큼의 리스트를 넣어야해서 answer의 크기를 n으로
        answer = new long[n];

        for(int i=0; i<n; i++) {
            // x는 ing형,  answer는 long이기때문에 형변환
            answer[i] = (long)x * (i+1);
        }
        return answer;
    }
}
/*
 - 다른 풀이
 class Solution {
    public static long[] solution(int x, int n) {
        long[] answer = new long[n];
        answer[0] = x;

        for (int i = 1; i < n; i++) {
            answer[i] = answer[i - 1] + x;
        }

        return answer;

    }
}
 */