void setup(){
  float[] inputs = {12, 4};
  float[] weights = {0.5, -1};
  float sum = 0;
  for(int i = 0; i < inputs.length; i++){
  	sum += inputs[i] * weights[i];	
  }
  println("Sum = " + sum);
}