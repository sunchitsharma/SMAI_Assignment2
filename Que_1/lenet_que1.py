from keras.models import Sequential
from keras.layers.convolutional import Convolution2D
from keras.layers.convolutional import MaxPooling2D
from keras.layers.core import Activation
from keras.layers.core import Flatten
from keras.layers.core import Dense

class LeNet:
	def build(width, height, depth, classes, weightPath=None):
		model = Sequential()


		# Making 1st conv layer :: Layer ==> Pool

		model.add(Convolution2D(20, 5, 5, border_mode-"same",input_shape=(depth,height,width)))
		# ^ 20 : Conv Filters :: Filter Size : 5 X 5
		model.add(Activation("relu"))
		model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))


		# Making 2nd conv layer :: Layer ==> Pool

		model.add(Convolution2D(50, 5, 5, border_mode="same"))
		model.add(Activation("relu"))
		model.add(MaxPooling2D(pool_size=(2,2), strides=(2,2)))


		# Adding Fully Connected Layers

		model.add(Flatten())
		model.add(Dense(500))
		model.add(Activation("relu"))

		# Adding Softmax Classifier

		model.add(Dense(classes))
		model.add(Activation("softmax"))

		# Check for pre_given weight files : if not train 

		if weightPath is not None:
			mode.load_weights(weightPath)

		return model

		