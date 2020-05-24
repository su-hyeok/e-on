#include "attendance.h"
attendance::attendance() {
	mat = vector<vector<int>>(15, vector<int>(5,-1)); //��ü�� �����Ǹ鼭 ��������� ������ ����(�⼮ǥ=TABLE)
	studentid = vector<string> {"2017001","2017002","2017003","2017004","2017005"}; // �й��� �ʱ⿡ �Ҵ�� ���� ���� 
	menu(); //�޴��޼��� ȣ��
}
attendance::~attendance() {
	cout << "�Ұ��Լ� ���" << endl;
}
void attendance::week() {
	do {
		cout << "�⼮�� ������ �Է��ϼ���: ";
		cin >> col;
		if (col > 0 && col < 16) {
			studentid2(); //0<����<16 �ϰ�쿡�� �⼮�Ҽ��ִ� �޼��带ȣ��
			cout << "�⼮�� �Ϸ��Ͽ����ϴ�." << endl;
		}
		else {
			col = 0; //�ش����� �� �ƴҰ�� 0������ ����
		}

	} while (!col);
}
void attendance::studentid2() {
	for (int i = 0; i < studentid.size(); i++) {
		if (mat[col - 1][i] != -1){
			break; //�ش� ������ �й��� �⼮���°� -1�� �ƴҰ�� Ż��
		}
		if (i == studentid.size() - 1) {
			fill(mat[col - 1].begin(), mat[col - 1].end(), 0); // �ش������� �⼮���°� ���� -1��� �⼮���¸� ���� 0���� �ٲ�
		}
	}
	string number; //�й��� �Է¹��� ���� ����
	do
	{
		cout << "�й��� �Է��ϼ���(q �Է½� ���̻� �й��Է� �ȹ���): ";
		cin >> number;
		string i; //�Է¹��� �й��� �⼮���� �й��� ������ ���� ����
		row = 0;
		for (string i : studentid) 
		{
			if (number == i) {
				mat[col - 1][row] = 1; //�Է¹��� �й��� �⼮���� �й��� ���ؼ� ������ �⼮���¸� 1�� �ٲ�
				break;
			}
			row += 1;
			if (number != "q" && row == studentid.size()) {
				cout << "�������� �ʴ� �й��Դϴ�." << endl; //�Է¹��� �й��� q�� �ƴϸ鼭 �� �й��� �ش��ϴ� ��ġ���� ������ ũ�Ⱑ �ɰ��
			}

		}
	} while (number != "q");
}
void attendance::add() {
	string student; //�߰��� �й��� ���� ���� ����
	do
	{
		cout << "�߰��� �й��� �Է��ϼ���(q �Է½� ���̻� �߰����� ����): ";
		cin >> student;
		if (student == "q") {
			break; //q�Է½� Ż��
		}
		else{
			cout << "�й� �߰��� �Ϸ��߽��ϴ�." << endl;
		}
		studentid.push_back(student); //���� �ȿ� ���ο� �й��� �߰���
		for (int i = 0; i < 16; i++) {
			mat[i].push_back(-1); //�߰��� �й��� 15���� ������ �⼮���¸� -1�� ����
		}
	} while (student !="q");

}

void attendance::menu() {
	int num ; //�޴� ��ȣ�� �Է¹��� ���� ����
	do 
	{
		cout << "�⼮�� ���α׷�" << endl;
		cout << "\t"<<"MENU"<<endl;
		cout << "1.�⼮�ϱ�" << endl;
		cout << "2.�⼮�� ���� Ȯ���ϱ�" << endl;
		cout << "3.�й��߰��ϱ�" << endl;
		cout << "4.���α׷� ����" << endl;
		cout << "�޴��� �Է��ϼ���: ";
		cin >> num;
		switch (num)
		{
		case 1:
			week(); //week()�޼��� ����
			break;
		case 2:
			cout << "�⼮�� Ȯ���� ������ �Է��ϼ���: ";
			cin >> col;
			for (int i = 0; i < studentid.size(); i++){
				cout << studentid[i] << "\t"; //�Է� �Ǿ��ִ� �й��� ���
			}
			cout<< endl;
			for (int j = 0; j < studentid.size(); j++) {
				cout << mat[col - 1][j] << "\t"; //�� �й��� �⼮ ���� ���
			}
			cout << endl;
			break;
		case 3:
			add(); //add()�޼��� ����

		case 4:
			cout << "�⼮�� ���α׷��� �����մϴ�" << endl;
			return;
		default:
			num = 0;
		}
	} while (!num);
	menu(); //����Լ� ����
}