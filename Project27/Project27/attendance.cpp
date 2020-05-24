#include "attendance.h"
attendance::attendance() {
	mat = vector<vector<int>>(15, vector<int>(5,-1)); //객체가 생성되면서 만들어지는 이차원 벡터(출석표=TABLE)
	studentid = vector<string> {"2017001","2017002","2017003","2017004","2017005"}; // 학번이 초기에 할당된 벡터 생성 
	menu(); //메뉴메서드 호출
}
attendance::~attendance() {
	cout << "소거함수 사용" << endl;
}
void attendance::week() {
	do {
		cout << "출석할 주차를 입력하세요: ";
		cin >> col;
		if (col > 0 && col < 16) {
			studentid2(); //0<주차<16 일경우에만 출석할수있는 메서드를호출
			cout << "출석을 완료하였습니다." << endl;
		}
		else {
			col = 0; //해당조건 이 아닐경우 0값으로 설정
		}

	} while (!col);
}
void attendance::studentid2() {
	for (int i = 0; i < studentid.size(); i++) {
		if (mat[col - 1][i] != -1){
			break; //해당 주차의 학번의 출석상태가 -1이 아닐경우 탈출
		}
		if (i == studentid.size() - 1) {
			fill(mat[col - 1].begin(), mat[col - 1].end(), 0); // 해당주차의 출석상태가 전부 -1경우 출석상태를 전부 0으로 바꿈
		}
	}
	string number; //학번을 입력받을 변수 선언
	do
	{
		cout << "학번을 입력하세요(q 입력시 더이상 학번입력 안받음): ";
		cin >> number;
		string i; //입력받은 학번과 출석부의 학번을 비교해줄 변수 선언
		row = 0;
		for (string i : studentid) 
		{
			if (number == i) {
				mat[col - 1][row] = 1; //입력받은 학번과 출석부의 학번을 비교해서 같으면 출석상태를 1로 바꿈
				break;
			}
			row += 1;
			if (number != "q" && row == studentid.size()) {
				cout << "존재하지 않는 학번입니다." << endl; //입력받은 학번이 q가 아니면서 각 학번에 해당하는 위치값이 벡터의 크기가 될경우
			}

		}
	} while (number != "q");
}
void attendance::add() {
	string student; //추가할 학번을 받을 변수 선언
	do
	{
		cout << "추가할 학번을 입력하세요(q 입력시 더이상 추가하지 않음): ";
		cin >> student;
		if (student == "q") {
			break; //q입력시 탈출
		}
		else{
			cout << "학번 추가를 완료했습니다." << endl;
		}
		studentid.push_back(student); //벡터 안에 새로운 학번을 추가함
		for (int i = 0; i < 16; i++) {
			mat[i].push_back(-1); //추가한 학번의 15주차 까지의 출석상태를 -1로 만듬
		}
	} while (student !="q");

}

void attendance::menu() {
	int num ; //메뉴 번호를 입력받을 변수 선언
	do 
	{
		cout << "출석부 프로그램" << endl;
		cout << "\t"<<"MENU"<<endl;
		cout << "1.출석하기" << endl;
		cout << "2.출석한 주차 확인하기" << endl;
		cout << "3.학번추가하기" << endl;
		cout << "4.프로그램 종료" << endl;
		cout << "메뉴를 입력하세요: ";
		cin >> num;
		switch (num)
		{
		case 1:
			week(); //week()메서드 실행
			break;
		case 2:
			cout << "출석을 확인할 주차를 입력하세요: ";
			cin >> col;
			for (int i = 0; i < studentid.size(); i++){
				cout << studentid[i] << "\t"; //입력 되어있는 학번들 출력
			}
			cout<< endl;
			for (int j = 0; j < studentid.size(); j++) {
				cout << mat[col - 1][j] << "\t"; //각 학번의 출석 상태 출력
			}
			cout << endl;
			break;
		case 3:
			add(); //add()메서드 실행

		case 4:
			cout << "출석부 프로그램을 종료합니다" << endl;
			return;
		default:
			num = 0;
		}
	} while (!num);
	menu(); //재귀함수 실행
}