* [PHT_Data](https://github.com/CaspervanAarle/PHT_Synth_Data_Gen)
* [PHT_Server](https://github.com/CaspervanAarle/PHT_Server) 
* [PHT_Node](https://github.com/CaspervanAarle/PHT_Node) (You are here)

# PHT_Node

This repository is part of the Personal Health Train Locker Thesis. This PHT_Node implements part of a Federated Learning algorithm to apply Regression. Aggregators and Classifiers can be altered easily. Due to the need for simulating numerous Personal Data Stores (PDS), importing big libraries is omitted. A semi-privacy-preserving Homomorphic Encrypted Standardization method and AdaGrad is included for better convergence.



## Usage

### Homomorphic Encryption
Before deploying this software to real distributed environment, be sure to share the same public and private keys over the PDS's. It automatically generates with ```main.py``` and ```experiment.py```.

### Deploy

### Local Experiment Deploy

This project uses local Python Sockets as a form of communication. The PHT Node is the Locker containing some information. The central PHT Server can connect to multiple PHT Nodes, receiving requests and sending them back to the server.




### Generator
To generate multiple lockers (100?) as a simulation tool

To be implemented

See the [PHT_Data](https://github.com/CaspervanAarle/PHT_Synth_Data_Gen) to generate sample data
