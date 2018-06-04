#include <iostream>
#include <string>

using namespace std;

bool isMatchAnswer(string s, string p) {
    // if (p.empty())    return s.empty();
    //
    // if ('*' == p[1])
    //     // x* matches empty string or at least one character: x* -> xx*
    //     // *s is to ensure s is non-empty
    //     return (isMatch(s, p.substr(2)) || !s.empty() && (s[0] == p[0] || '.' == p[0]) && isMatch(s.substr(1), p));
    // else
    //     return !s.empty() && (s[0] == p[0] || '.' == p[0]) && isMatch(s.substr(1), p.substr(1));

}

bool isMatch(string s, string p) {
  if (p.empty()) {
    return s.empty();
  }


  if (p[1] == '*') {
    return (  isMatch(s, p.substr(2)) || !s.empty() && (s[0] == p[0] || p[0] == '.')   &&  isMatch(s.substr(1), p) );
  } else {
    return ( (!s.empty() && isMatch(s.substr(1), p.substr(1)) && ((s[0] == p[0]) ||p[0] == '.' ) ) );
  }
}

int main() {
  int a = isMatch("aceer", "ace*.");
  // string a = "ADSdASD"
  cout << a << endl;
  return 0;
}
