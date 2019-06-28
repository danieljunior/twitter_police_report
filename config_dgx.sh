apt update
apt install nano
apt install python3-pip
pip3 install conda
#curl -O https://repo.continuum.io/archive/Anaconda3-5.0.1-Linux-x86_64.sh
#bash Anaconda3-5.0.1-Linux-x86_64.sh
pip3 install pandas
#conda create -n allennlp python=3.6
#source activate allennlp
pip3 install allennlp
#allennlp test-install
export SRL_TRAIN_DATA_PATH=/workspace/twitter_police_report/data/train/train_file_0.conll
export SRL_VALIDATION_DATA_PATH=/workspace/twitter_police_report/data/validation/validation_file_0.conll
rm -r output_path/
mv /usr/local/lib/python3.6/dist-packages/allennlp/data/dataset_readers/semantic_role_labeling.py /usr/local/lib/python3.6/dist-packages/allennlp/data/dataset_readers/semantic_role_labeling_original.py
cp semantic_role_labeling.py /usr/local/lib/python3.6/dist-packages/allennlp/data/dataset_readers/semantic_role_labeling.py
allennlp train elmo_srl_options.jsonet --serialization-dir output_path
#pip install -U spacy
#pip install config/pt_core_news_sm-2.1.0.tar.gz
