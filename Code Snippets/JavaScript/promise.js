var myfunct = function(var1, var2) {

  return new Promise(function(resolve, reject) {
    if (var1 == var2) {
      resolve("var1 = var2");
    } else {
      reject(Error("it broke"));
    }
  })


}

myfunct("Hi", "Hi").then(function(result) {
  console.log(result);
}).catch(function(result) {
  console.log(result + "error");
});
