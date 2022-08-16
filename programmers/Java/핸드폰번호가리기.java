package com.programmers.java;

class 핸드폰번호가리기 {
    public String solution(String phone_number) {

        char[] arr = phone_number.toCharArray();

        for(int i=0; i<arr.length-4; i++)
            arr[i] = '*';

        return new String(arr);
    }
}