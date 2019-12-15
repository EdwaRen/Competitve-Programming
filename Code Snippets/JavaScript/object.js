let obj = function() {
  let i = 0;
  return {
    setI(k) {
      i = k;
    },
    getI(k) {
      return i;
    }
  }

}

let a = obj();
a.setI(2);
console.log(a.getI());
