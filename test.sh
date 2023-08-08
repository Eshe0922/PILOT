# python run.py \
#     --output_dir=./saved_models/Devign \
#     --model_type=roberta \
#     --tokenizer_name=microsoft/codebert-base \
#     --model_name_or_path=microsoft/codebert-base \
#     --do_test\
#     --train_data_file=./data/data_preprocessed/Devign/train.txt \
#     --eval_data_file=./data/data_preprocessed/Devign/valid.txt \
#     --test_data_file=./data/data_preprocessed/Devign/test.txt \
#     --seed 123456  2>&1 | tee test_Devign.log 

# python run.py \
#     --output_dir=./saved_models/Fan \
#     --model_type=roberta \
#     --tokenizer_name=microsoft/codebert-base \
#     --model_name_or_path=microsoft/codebert-base \
#     --do_test\
#     --train_data_file=./data/data_preprocessed/Fan/train.txt \
#     --eval_data_file=./data/data_preprocessed/Fan/valid.txt \
#     --test_data_file=./data/data_preprocessed/Fan/test.txt \
#     --seed 123456  2>&1 | tee test_Fan.log 

python run.py \
    --output_dir=./saved_models/Reveal \
    --model_type=roberta \
    --tokenizer_name=microsoft/codebert-base \
    --model_name_or_path=microsoft/codebert-base \
    --do_test\
    --train_data_file=./data/data_preprocessed/Reveal/train.txt \
    --eval_data_file=./data/data_preprocessed/Reveal/valid.txt \
    --test_data_file=./data/data_preprocessed/Reveal/test.txt \
    --seed 123456  2>&1 | tee test_Reveal.log 