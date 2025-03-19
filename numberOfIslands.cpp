/*
Given a binary 2D matrix of size n*m, 
find the number of islands. A group of connected 1s forms an island.
1. if 1 found, run a different function to [look for adjacent 1's and hash all]
2. island count+=1 and move ahead for all the 1's  
*/
#include<iostream>
#include<vector>
using namespace std;
bool isSafe(vector<vector<char>>& grid, int r, int c,vector<vector<bool>>& visited){
    int row = grid.size();
    int col = grid[0].size();

    return(r>=0) && (r<row) && (c>=0) && (c<col) && (grid[r][c] == '1' && grid[r][c] != visited[r][c]); 
};

void dfs(vector<vector<char>>& grid, int r, int c, vector<vector<bool>>& visited){
    vector<int> rNbr = {-1, -1, -1, 0, 0, 1, 1, 1};
    vector<int> cNbr = {-1, 0, 1, -1, 1, -1, 0, 1};

    visited[r][c] = true;
    for(int k=0; k<8; ++k){
        int newR = r + rNbr[k];
        int newC = c + cNbr[k];
        if(isSafe(grid, newR, newC, visited)){
            dfs(grid, newR, newC, visited);
        }
    }
};
int numIslands(vector<vector<char>>& grid){
    int row = grid.size();
    int col = grid[0].size();

    vector<vector<bool>> visited(row, vector<bool>(col, false));

    int count = 0;
    for(int r=0; r<row; ++r){
        for(int c=0; c<col; ++c){
            if(grid[r][c] == '1' && !visited[r][c]) {
                dfs(grid, r, c, visited);
                ++count;
            }
        }
    }
    return count;
};
int main(){
    vector<vector<char>> grid = {{'1', '1'},
                              {'1', '1'}};
    cout<<numIslands(grid)<<endl;
    return 0;
}