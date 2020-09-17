To run the temporal relation extraction algorithm, 

1) uploda the i2b2 2012 dataset in the /corpus/i2b2 folder, and upload the pretrained BERT models in the /pretrained_bert_model folder.

2) run the data_process_i2b2.py to preprocess the data and create the input text file for training.

3) run_i2b2_bioBERT.py or run_i2b2_clinicalBERT.py to train the temporal relation extraction model.
