croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
word = input()

for i in croatia:
    word = word.replace(i, "*")
print(len(word))


# +여담
# c언어 풀이

# #include<stdio.h>
# #include<string.h>
# int CountString(char* param, int len) {
# 	int count = 0;

# 	for (int k = 0; k < len; k++) {
# 		if (param[k] == 'c') {
# 			if (param[k + 1] == '=' || param[k + 1] == '-') {
# 				k++;
# 			}
# 		}
# 		else if (param[k] == 'd') {
# 			if (param[k + 1] == 'z' && param[k + 2] == '=') {
# 				k += 2;
# 			}
# 			else if (param[k + 1] == '-') {
# 				k++;
# 			}
# 		}
# 		else if ((param[k] == 'l' || param[k] == 'n') && param[k + 1] == 'j') {
# 			k++;
# 		}
# 		else if ((param[k] == 's' || param[k] == 'z') && param[k + 1] == '=') {
# 			k++;
# 		}
# 		count++;
# 	}
# 	return count;
# }

# int main(void) {
# 	char str[101];
# 	int length, result;

# 	scanf("%s", str);
# 	length = strlen(str);

# 	result = CountString(str, length);

# 	printf("%d", result);

# 	return 0;
# }

## 파이썬 라이브러리를 적극 활용합시다