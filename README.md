* [PHT_Data](https://github.com/CaspervanAarle/PHT_Synth_Data_Gen)
* [PHT_Server](https://github.com/CaspervanAarle/PHT_Server) 
* [PHT_Node](https://github.com/CaspervanAarle/PHT_Node) (You are here)

# PHT_Node

This repository is part of the Personal Health Train Locker Thesis. This PHT_Node implements part of a Federated Learning algorithm to apply Regression. Aggregators and Classifiers can be altered easily. Due to the need for simulating numerous Personal Data Stores (PDS), importing big libraries is omitted. A semi-privacy-preserving Homomorphic Encrypted Standardization method and AdaGrad is included for better convergence.



## Usage

### Homomorphic Encryption
Before deploying this software to real distributed environment, be sure to share the same public and private keys over the PDS's. It automatically generates with ```main.py``` and ```experiment.py```. This encryption is only used for sharing prescriptive statistics

### Deploy
Like the PHT_Server, the PHT_Node also requires a 'config' and a 'learnconfig' file. Both are imported by an instance of a PDS. The 'config' file defines the data location of that specific locker and states at which port it must be hosted.
```
{
  "config_name": "locker_1", 
  "host_port": "5050", 
  "csv_location": "C:\\Users\\Casper\\...\\readmission_hospital_federated\\1.csv"}
```
The 'learnconfig' file contains the features that need to be included in the learning process and the regressor type to be used. The same values must also reside in the 'learnconfig' file in the PHT_Server.
```
{
	"config_name": "experiment4",
	"var_list": ["time_in_hospital",	"num_lab_procedures",	"num_procedures",	"num_medications",	"number_outpatient",	"number_emergency",	"number_inpatient",	"number_diagnoses"],
	"target_list":	["readmitted"],
	"regressor": "LogReg"
}
```

### Local Experiment Deploy
The ```experiment.py``` file can generate many lockers, by generating different 'config' files that define different dat and a different deployment port, and by using the same 'learnconfig' file.



See the [PHT_Data](https://github.com/CaspervanAarle/PHT_Synth_Data_Gen) to generate sample data
