# PILOT
# When Less is Enough: Positive-Unlabeled Learning Model for Vulnerability Detection
## Introducion

Automated code vulnerability detection has gained increasing attention in recent years. The deep learning (DL)-based methods, which implicitly learn vulnerable code patterns, have proven effective in vulnerability detection. The performance of DL-based methods usually relies on the quantity and quality of labeled data. However, the current labeled data are generally automatically collected, such as crawled from human-generated commits, making it hard to ensure the quality of the labels. Prior studies have demonstrated that the non-vulnerable code (i.e., negative labels) tends to be unreliable in commonly-used datasets, while vulnerable code (i.e., positive labels) is more determined. Considering the large numbers of unlabeled data in practice, it is necessary and worth exploring to leverage the positive data and large numbers of unlabeled data for more accurate vulnerability detection.

In this paper, we focus on the Positive and Unlabeled (PU) learning problem for vulnerability detection and propose a novel model named PILOT, i.e., PositIve and unlabeled Learning mOdel for vulnerability deTection. PILOT only learns from positive and unlabeled data for vulnerability detection. It mainly contains two modules: (1) A distance-aware label selection module, aiming at generating pseudo-labels for selected unlabeled data, which involves the inter-class distance prototype and progressive fine-tuning; (2) A mixed-supervision representation learning module to further alleviate the influence of noise and enhance the discrimination of representations. Extensive experiments in vulnerability detection are conducted to evaluate the effectiveness of PILOT based on real-world vulnerability datasets. The experimental results show that PILOT outperforms the popular weakly supervised methods by 2.78%-18.93% in the PU learning setting. Compared with the state-of-the-art methods, PILOT also improves the performance of 1.34%-12.46% in F1 score metrics in the supervised setting. In addition, PILOT can identify 23 mislabeled from the FFMPeg+Qemu dataset in the PU learning setting based on manual checking.

## Dataset
To investigate the effectiveness of PILOT, we adopt three vulnerability datasets from these paper:

* Fan et al. [1]: https://drive.google.com/file/d/1-0VhnHBp9IGh90s2wCNjeCMuy70HPl8X/view?usp=sharing

* Reveal [2]: https://drive.google.com/drive/folders/1KuIYgFcvWUXheDhT--cBALsfy1I4utOyF

* FFMPeg+Qemu [3]: https://drive.google.com/file/d/1x6hoF7G-tSYxg8AFybggypLZgMGDNHfF

The three datasets are stored in the "dataset" directory as zips, each zip containing three files: "train.txt" "valid.txt" "test.txt".

## Environment Setup

    pip install torch
    pip install transformers
    pip install numpy
    pip install gdown
    pip install tqdm
    pip install pickle
    pip install sklearn
    pip install pandas
    pip install tokenizers
    
## Running the model

If you want to run the model quickly, you can execute the following command:

    run PILOT.sh

If you want to fine-tune the parameters of each step of the model, you can execute the following command:

* For Initial fine-tuning in Inter-class Distance Prototype:

        python run.py \
            --output_dir=./saved_models/train_1 \
            --model_type=roberta \
            --tokenizer_name=microsoft/codebert-base \
            --model_name_or_path=microsoft/codebert-base \
            --do_train_1\
            --labels_file=./data/data_result/ \
            --label_ratio  0.3 \
            --train_data_file=./data/data_preprocessed/train.txt \
            --eval_data_file=./data/data_preprocessed/valid.txt \
            --test_data_file=./data/data_preprocessed/test.txt \
            --epoch 5 \
            --block_size 512 \
            --train_batch_size 32 \
            --eval_batch_size 64 \
            --learning_rate 2e-5 \
            --max_grad_norm 1.0 \
            --evaluate_during_training \
            --seed 123456  2>&1 | tee train1.log 

* For Selection of High-quality Negative (HN) samples in Inter-class Distance Prototype:

        python run.py \
            --output_dir=./saved_models/train_1 \
            --model_type=roberta \
            --tokenizer_name=microsoft/codebert-base \
            --model_name_or_path=microsoft/codebert-base \
            --do_step1\
            --labels_file=./data/data_result/ \
            --label_ratio  0.3 \
            --train_data_file=./data/data_preprocessed/train.txt \
            --eval_data_file=./data/data_preprocessed/valid.txt \
            --test_data_file=./data/data_preprocessed/test.txt \
            --epoch 5 \
            --P_num 10018 \
            --N_num 11836 \
            --block_size 512 \
            --train_batch_size 32 \
            --eval_batch_size 64 \
            --learning_rate 2e-5 \
            --max_grad_norm 1.0 \
            --evaluate_during_training \
            --seed 123456  2>&1 | tee step1.log 

* For First step in Progressive Fine-tuning:

        python run.py \
            --output_dir=./saved_models/train_2 \
            --model_type=roberta \
            --tokenizer_name=microsoft/codebert-base \
            --model_name_or_path=microsoft/codebert-base \
            --do_train_2\
            --labels_file=./data/data_result/ \
            --label_ratio  0.3 \
            --train_data_file=./data/data_preprocessed/train.txt \
            --eval_data_file=./data/data_preprocessed/valid.txt \
            --test_data_file=./data/data_preprocessed/test.txt \
            --epoch 5 \
            --block_size 512 \
            --train_batch_size 32 \
            --eval_batch_size 64 \
            --learning_rate 2e-5 \
            --max_grad_norm 1.0 \
            --evaluate_during_training \
            --seed 123456  2>&1 | tee train2.log 

* For Second step in Progressive Fine-tuning:

        python run.py \
            --output_dir=./saved_models/train_2 \
            --model_type=roberta \
            --tokenizer_name=microsoft/codebert-base \
            --model_name_or_path=microsoft/codebert-base \
            --do_train_iterative\
            --labels_file=./data/data_result/ \
            --label_ratio  0.3 \
            --train_data_file=./data/data_preprocessed/train.txt \
            --eval_data_file=./data/data_preprocessed/valid.txt \
            --test_data_file=./data/data_preprocessed/test.txt \
            --epoch 5 \
            --P_num 10018 \
            --N_num 11836 \
            --block_size 512 \
            --train_batch_size 32 \
            --eval_batch_size 64 \
            --learning_rate 2e-5 \
            --max_grad_norm 1.0 \
            --evaluate_during_training \
            --seed 123456  2>&1 | tee train_iterative.log

* For Mixed-supervision representation learning module：

        python run.py \
            --output_dir=./saved_models/Model_add/train_3 \
            --model_type=roberta \
            --tokenizer_name=microsoft/codebert-base \
            --model_name_or_path=microsoft/codebert-base \
            --do_train_3\
            --labels_file=./data/data_result/ \
            --label_ratio  0.3 \
            --train_data_file=./data/data_preprocessed/train.txt \
            --eval_data_file=./data/data_preprocessed/valid.txt \
            --test_data_file=./data/data_preprocessed/test.txt \
            --epoch 5 \
            --block_size 512 \
            --train_batch_size 32 \
            --eval_batch_size 64 \
            --learning_rate 2e-5 \
            --max_grad_norm 1.0 \
            --evaluate_during_training \
            --seed 123456  2>&1 | tee train3.log

* Tips:
  
|Dataset|P_num|N_num|
|:----: |:----:|:----:|
|Fan|8736|150908|
|Reveal|1760|18187|
|FFMPeg+Qemu|10018|11836|


## Test the model

You can download the models by executing the following command or by visiting the following site：

    gdown https://drive.google.com/uc?id=10UtMoa_3WE-w8jtWeocMm4OSlue51TTj

    https://drive.google.com/file/d/10UtMoa_3WE-w8jtWeocMm4OSlue51TTj/view?usp=drive_link

If you want to test the model quickly, you can execute the following command:

    run test.sh

## References
[1] Jiahao Fan, Yi Li, Shaohua Wang, and Tien Nguyen. 2020. A C/C++ Code Vulnerability Dataset with Code Changes and CVE Summaries. In The 2020 International Conference on Mining Software Repositories (MSR). IEEE.

[2] Saikat Chakraborty, Rahul Krishna, Yangruibo Ding, and Baishakhi Ray. 2020. Deep Learning based Vulnerability Detection: Are We There Yet? arXiv preprint arXiv:2009.07235 (2020).

[3] Yaqin Zhou, Shangqing Liu, Jingkai Siow, Xiaoning Du, and Yang Liu. 2019. Devign: Effective vulnerability identification by learning comprehensive program semantics via graph neural networks. In Advances in Neural Information Processing Systems. 10197–10207.
