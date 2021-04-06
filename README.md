* [PHT_Synth_Data_Gen](https://github.com/CaspervanAarle/PHT_Synth_Data_Gen)
* [PHT_Server](https://github.com/CaspervanAarle/PHT_Server) 
* [PHT_Node](https://github.com/CaspervanAarle/PHT_Node) (You are here)

# PHT_Node

This repository is part of the Personal Health Train Locker Thesis. 



### Manual
This project uses Python Sockets as a form of communication. The PHT Node is the Locker containing some information. The central PHT Server can connect to multiple PHT Nodes, receiving requests and sending them back to the server.

In ```main.py```, change the IP ADDRESS to localhost for local testing or you ipv4 default gateway for network connections.

When running locally, every node needs a different port to which it can bind a socket. When running on multiple devices, this is not necessary, but change the ip address accordingly.

```python src/main.py```

setting a new config:

port: the port where the central aggregator can connect to.

csv_location: location of the data (e.g. "C:\path\to\dataset\1.csv")

See the [PHT_Synth_Data_Gen](https://github.com/CaspervanAarle/PHT_Synth_Data_Gen) to generate a sample


### Generator

To be implemented
