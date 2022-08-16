package com.programmers.java;

class 평균구하기 {
    public double solution(int[] arr) {
        double sum = 0;

        for (int i=0; i<arr.length; i++)
            sum += arr[i];

        return sum/arr.length;
    }
}

/*
Array에 있는 평균을 구하는 메서드 사용 - (Array.stream이 곧 IntStream이다.)
 - But stream이라 속도가 느림
class Solution {
    public double solution(int[] arr) {
        return Array.stream(arr).average().getAsDouble();
    }
}
*/
