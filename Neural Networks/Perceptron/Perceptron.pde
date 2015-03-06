class Perceptron {
  float[] weights;
  Perceptron(int n){
    weights = new float[n];
    for(int i = 0; i < weights.length; i++){
      weights[i] = random(-1, 1);
    }
  }
  int feedforward(float[] inputs){
  	float sum = 0;
  	for(int i = 0 i < weights.length; i++){
  		sum += inputs[i] * weights[i];
  	}
  	return activate(sum);
  }
  int activate(float sum){
  	if(sum > 0) return 1;
  	else return -1;
  }
}
