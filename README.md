# PILOT
# When Less is Enough: Positive-Unlabeled Learning Model for Vulnerability Detection
## Introducion

## Dataset
To investigate the effectiveness of PUVD, we adopt three vulnerability datasets from these paper:

* Fan et al. [1]: https://drive.google.com/file/d/1-0VhnHBp9IGh90s2wCNjeCMuy70HPl8X/view?usp=sharing

* Reveal [2]: https://drive.google.com/drive/folders/1KuIYgFcvWUXheDhT--cBALsfy1I4utOyF

* FFMPeg+Qemu [3]: https://drive.google.com/file/d/1x6hoF7G-tSYxg8AFybggypLZgMGDNHfF

To download the dataset used for evaluation in our experiments, run the following commands:
    
Notice：If you want to download multiple datasets, please note the overlay of the storage location!

    cd data_raw
    gdown path_Devign(path_Reveal/path_Fan)
    cd ..
    python split data_Devign(Reveal/Fan).py

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

## Results
### Results of RQ1



### Results of RQ2



### Results of RQ3


### Results of RQ4

## References
[1] Jiahao Fan, Yi Li, Shaohua Wang, and Tien Nguyen. 2020. A C/C++ Code Vulnerability Dataset with Code Changes and CVE Summaries. In The 2020 International Conference on Mining Software Repositories (MSR). IEEE.

[2] Saikat Chakraborty, Rahul Krishna, Yangruibo Ding, and Baishakhi Ray. 2020. Deep Learning based Vulnerability Detection: Are We There Yet? arXiv preprint arXiv:2009.07235 (2020).

[3] Yaqin Zhou, Shangqing Liu, Jingkai Siow, Xiaoning Du, and Yang Liu. 2019. Devign: Effective vulnerability identification by learning comprehensive program semantics via graph neural networks. In Advances in Neural Information Processing Systems. 10197–10207.