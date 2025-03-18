#include<iostream>
#include<vector>
using namespace std;

bool dfs(vector<vector<char>> board, string word, int i,int j, int index){
    if(index==word.length()) return true;
    if(i<0 || i>=board.size() || j<0 || j>=board.size() || board[i][j] != word[index]){
        return false;
    }
    
    char temp = board[i][j];
    board[i][j] = '#';

    bool found = dfs(board, word, i+1, j, index+1)||
                 dfs(board, word, i-1, j, index+1) ||
                 dfs(board, word, i, j+1, index+1) ||
                 dfs(board, word, i,j-1, index+1);
    
    board[i][j] = temp;
    return found;
}

bool exist(vector<vector<char>> board, string word)
{
    int index = 0;
    for(int i=0; i<board.size(); i++){
        for(int j=0; j<board[i].size(); j++){
            if(dfs(board, word, i, j, 0)){
                return true;
                } 
            }
        }
        return false;
}


int main(){
    vector<vector<char>> board = {{"A", "B", "C", "E"},
                                 {"S", "F", "C", "S"},
                                 {"A", "D", "E", "E"}};
    string word = "ABCCED"; 
    cout<<(exist(board, word) ? "True" : "False")<<endl;
    return 0;

}


/*
1. find the first letter
2. check for all adjacent blocks(left, right up, down)
3. if next letter found, letter is the next letter
4. continue until letter is the last letter
*/
