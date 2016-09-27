import java.util.Arrays;
import java.util.Vector;
import org.opencv.core.Core;
import org.opencv.core.CvType;
import org.opencv.core.Mat;
import org.neuroph.core.NeuralNetwork;
import org.neuroph.nnet.MultiLayerPerceptron;
import org.neuroph.util.TransferFunctionType;
import org.neuroph.core.data.DataSet;
import org.neuroph.core.data.DataSetRow;

public class Main {
	
	public static void main( String[] args ) {
		
		double[] input;
		double[] output;
		        
		System.out.println( "Hello World, I'm going to start the neuroph test\n" );
		// create training set (logical XOR function)
		DataSet trainingSet = createDataset( 4 , 2 );//create a dataset with 3 input and 1 output
		
		//add xor gate like input
		input = new double[] { 0 , 0 , 0.8 , 1 };
		output = new double[] { 0 , 1 };
		trainingSet = addRow( trainingSet , input , output );
		
		input = new double[] { 0.1 , 0.2 , 0.9 , 0.95 };
		output = new double[] { 0 , 1 };
		trainingSet = addRow( trainingSet , input , output );
		
		input = new double[] { 0.99 , 0.73 , 0.2 , 0.3 };
		output = new double[] { 1 , 0 };
		trainingSet = addRow( trainingSet , input , output );
		
		input = new double[] { 0.95 , 0.88 , 0.01 , 0 };
		output = new double[] { 1 , 0 };
		trainingSet = addRow( trainingSet , input , output );
		
		// create multi layer perceptron
		MultiLayerPerceptron myMlPerceptron = createMLPerceptron( 4 , 3 , 2 );
		
		// learn the training set
		myMlPerceptron.learn(trainingSet);
	
		System.out.println("I'm still working here, and mlt has learned now");

		// test perceptron
		System.out.println("Testing trained neural network");
		testNeuralNetwork(myMlPerceptron, trainingSet);

	/*	// save trained neural network
		myMlPerceptron.save("myMlPerceptron.nnet");

		// load saved neural network
		NeuralNetwork loadedMlPerceptron = NeuralNetwork.createFromFile("myMlPerceptron.nnet");

		// test loaded neural network
		System.out.println("Testing loaded neural network");
		testNeuralNetwork(loadedMlPerceptron, trainingSet);
	 */
	}
	
	private static MultiLayerPerceptron createMLPerceptron ( int input , 
			int layers , int output)
	{
		MultiLayerPerceptron mlp = new MultiLayerPerceptron( 
				TransferFunctionType.SIGMOID , input , layers , output );
		return mlp;
	}
	
	private static DataSet addRow ( DataSet ds , double[] inputs , double[] outputs )
	{
		System.out.print( "input: [" );
		for( int i = 0; i < inputs.length ; i++ )
		{
			System.out.print( inputs[i] + "; " );
		}
		System.out.print( "] outputs: [" );
		for( int i = 0; i < outputs.length ; i++ )
		{
			System.out.print( outputs[i] + "; " );
		}
		System.out.println("]");
		ds.addRow( new DataSetRow( inputs , outputs ) );
		return ds;
	}
	
	private static DataSet createDataset( int input , int output )
	{
		DataSet ds = new DataSet( input , output );
		return ds;
	}
	
	public static void testNeuralNetwork(NeuralNetwork nnet, DataSet testSet) {

		for(DataSetRow dataRow : testSet.getRows()) {
		nnet.setInput(dataRow.getInput());
		nnet.calculate();
		double[ ] networkOutput = nnet.getOutput();
		System.out.print("Input: " + Arrays.toString(dataRow.getInput()) );
		System.out.println(" Output: " + Arrays.toString(networkOutput) );
		}

	}



}
