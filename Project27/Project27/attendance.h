#pragma once
#include<iostream>
#include<vector>//���͸� ����ϱ����� ������ �ʿ�
using namespace std;
class attendance //attendance��� Ŭ���� ����
{
public:
	attendance(); //�����Լ�
	~attendance(); //�Ұ��Լ�
	void menu(); //�޴��� �����ϴ� �޼���
	void week(); //�⼮�� ������ �Է��ϴ� �޼��� 
	void studentid2(); //�⼮�� ���� �Է��� �й��� �Է��Ͽ� �⼮�Ҽ��ְ� ����� �޼���
	void add();//�й��� �߰��ϱ����� ���� �޼���
private:
	vector<vector<int>> mat;//�⼮�� ǥ���� ������ ����(TABLE) ����
	vector<string> studentid;//�й��� ������ 1���� ���� ����
	int col;// ����������(TABLE)�� ����(����)
	int row;// ������ ����(TABLE)�� ����(�� �й��� �ش��ϴ� ��ġ ��)
};