#define UP 0
#define RIGHT 1
#define DOWN 2
#define LEFT 3

#include <iostream>
#include <queue>
#include <vector>

using namespace std;


extern bool swap(int dir);

int directions[4][2] = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};

struct info {
    int board[5][5];
    int empty_x, empty_y;
    vector<int> solution;
    int callCnt;

    info(int b[5][5], int x, int y, vector<int> s, int cnt) 
        : empty_x(x), empty_y(y), solution(s), callCnt(cnt) {
            for (int i = 0; i < 5; ++i) {
                for (int j = 0; j < 5; ++j) {
                    board[i][j] = b[i][j];
                }
            }
        }
};

bool isTarget(int board[5][5], int pattern[3][3])
{
    for (int i=0, r=1; i < 3; i++, r++)
        for( int j=0, c=1; i < 3; j++, c++)
            if(pattern[i][j] != board[r][c])    return false;

    return true;
}

int (*localSwap(int board[5][5], int i, int j, int dir))[5] {
    // i, j: 빈칸 좌표

    int r = i + directions[dir][0];
    int c = j + directions[dir][1];

    int tmp = board[r][c];
    board[r][c] = 0;
    board[i][j] = tmp;

    return board;
}

void solve(int board[5][5], int pattern[3][3], int callCntLimit) 
{
    int i = 0, j = 0;
    for(i; i < 5; i++)
        for(j; j < 5; j++)
            if (board[i][j] == 0)
                break;
    

    queue<info> q;
    vector<int> v;
    v.clear();
    info first(board, i, j, v, 0);
    q.push(first);

    vector<int> ans;
    while(!q.empty())
    {
        info current = q.front();
        q.pop();

        if(isTarget(current.board, pattern)){
            ans = current.solution;
            break;
        }
        for(int dir = 0; dir < 4; dir++)
        {
            int nx = current.empty_x + directions[dir][0];
            int ny = current.empty_y + directions[dir][1];

            if(nx >= 0 && nx < 5 && ny >= 0 && ny < 5 && current.callCnt < callCntLimit)
            {
                int (*nextBoard)[5] = localSwap(board, current.empty_x, current.empty_y, dir);
                vector<int> nextSolution = current.solution;
                nextSolution.push_back(dir);
                info nextState(nextBoard, nx, ny, nextSolution, current.callCnt++);
                q.push(nextState);
            }
        }
        
    }

    for(auto& dir: ans) {
        swap(dir);
    }
    
}