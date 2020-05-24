#pragma once
#include<iostream>
#include<vector>//벡터를 사용하기위해 선언이 필요
using namespace std;
class attendance //attendance라는 클래스 생성
{
public:
	attendance(); //생성함수
	~attendance(); //소거함수
	void menu(); //메뉴를 선택하는 메서드
	void week(); //출석할 주차를 입력하는 메서드 
	void studentid2(); //출석할 주차 입력후 학번을 입력하여 출석할수있게 만드는 메서드
	void add();//학번을 추가하기위해 만든 메서드
private:
	vector<vector<int>> mat;//출석을 표시할 이차원 벡터(TABLE) 선언
	vector<string> studentid;//학번을 저장할 1차원 벡터 선언
	int col;// 이차원벡터(TABLE)의 세로(주차)
	int row;// 이차원 벡터(TABLE)의 가로(각 학번에 해당하는 위치 값)
};