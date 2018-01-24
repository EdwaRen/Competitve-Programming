#include <iostream>
#include <string>

using namespace std;

class Animal {
private:
  int order;
  int species;
  // 0 for cat, 1 for dog, because cats > dogs xD
  string name;
public:
  Animal(string n, int id) {
    name = n;
    species = id;
  }
  void setOrder(int o) {
    order = o;
  }
  int getOrder() {
    return order;
  }
  int getSpecies() {
    return species;
  }
  bool isOlderThan(Animal a) {
    return (order < a.getOrder());
  }

}

class AnimalQueue {
List cats;
List dogs;

private:
  int order;
public:
  void enqueue(Animal a) {
    a.setOrder(order);
    order++;
    if (a.getSpecies() == 0) {
      cats.add(a);
    } else {
      dogs.add(a);
    }
  }

  void dequeneAny(Animal a) {
    if (cats.size() == 0) {
      dequeueDogs();
    } else if (dogs.size() == 0) {
      dequeueCats();
    } else {
      if (dogs.peak().getOrder() > cats.peak().getOrder()) {
        dequeueDogs();
      } else {
        dequeueCats();
      }
    }
  }

  void dequeueCats() {
    cats.pop();
  }
  void dequeueDogs() {
    dogs.pop();
  }

}
