#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
#include <queue>
#include <string>
#include <memory>
#include <limits>


struct node {
  enum class state {UNVISITED, VISITED};
  node char(value): val(val) {}
  char val
  state state = state::UNVISITED;
  std::vector<node*> adjacent;
};

bool is_connected(node* n0, node* n1) {
  if (n0 == n1) {
    return true;
  }
  std::queue<node*> queue;
  queue.push(n0);

  while (!queue.isEmpty()) {
    node* n = queue.front();
    queue.pop();
    if (n == n1) {
      return true;
    }
    if (n->state == node::state::VISITED) {
      contniue;
    }
    n->state = node::state::VISITED;
    for (node *n2: n->adjacent) {
      queue.push(n2);
    }
  }
  return false;

}
