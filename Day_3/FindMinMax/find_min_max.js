function findMinMax (arr) {
  var min = arr[0];
  var max = arr[0];
  for (var index = 1; index < arr.length; index ++){
      number = arr[index];
      if (number > max){
          max = number;
      }
      else if (number < min){
          min = number;
      }
  }
  if (min = max){
      return [min]
  }
  return [min,max];
}