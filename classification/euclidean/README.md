# Euclidean Distance

## How does it work?
The Euclidean Distance classifier requires a Parameterization to be set up. When passing a new text, It gets all the vectors for each article of our train set. These have already been created in the setup step of the parameterizer. It then creates a new vector for the new text and determines the closest distance to the existing vectors. We assume the same topic as whihever articles vector is closest to our text.

## How do we use it?
Make sure to set up a parameterizer first. We do not need to worry about which one, as the parameterization interface will handle the communication between classifier and parameterizer. Then we simply call `evaluate` with the training articles and the new text.