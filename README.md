# PUVD
# When Less is Enough: Positive-Unlabeled Learning Model for Vulnerability Detection
## Introducion
Abstract— Automated code vulnerability detection has gained
increasing attention in recent years. The deep learning (DL)-
based methods, which implicitly learn vulnerable code patterns,
have proven effective in vulnerability detection. However, the
learning performance of DL-based methods relies on the quantity
of labeled data. The current labeled data usually rely on statically
analyzed tools or human-generated commits, which it leads
difficult to get high-quality labels. Previous works have also
demonstrated that non-vulnerable (negative) labels for source
functions are unreliable in the real-world scenario. Therefore,
the main challenge is to mitigate the problem of poor-quality
labels by using the vulnerable (positive) labeled data and a large
number of unlabeled data for vulnerability detection.
To mitigate the above issues, in this paper, we propose a
novel Positive and Unlabeled learning model for Vulnerability
Detection (PUVD), which only learn from positive and unlabeled
data for vulnerability detection. PUVD mainly contains two
modules: (1) A distance-aware label selection module aims at
generating reliable pseudo-labels by leveraging positive data to
learn vulnerability patterns and then utilizing pseudo-labels to
further detect unlabeled vulnerabilities. (2) A representation and
pseudo-label metric learning module to enhance the discrimina-
tive power of the vulnerability representation in noisy situations.
We conducted several experiments to evaluate PUVD using real-
world vulnerability datasets. It shows that PUVD outperforms the
state-of-the-art and PU learning methods by xx%-xx% and xx%-
xx% in F1 score metrics, respectively. The results demonstrate
the effectiveness of PUVD in label-missing and noisy situations.
PUVD can also identify 15% of the noise data after manual
checking.
## Dataset
To investigate the effectiveness of PUVD, we adopt three vulnerability datasets from these paper:

Fan et al. [1]: https://drive.google.com/file/d/1-0VhnHBp9IGh90s2wCNjeCMuy70HPl8X/view?usp=sharing

Reveal [2]: https://drive.google.com/drive/folders/1KuIYgFcvWUXheDhT--cBALsfy1I4utOyF

FFMPeg+Qemu [3]: https://drive.google.com/file/d/1x6hoF7G-tSYxg8AFybggypLZgMGDNHfF
## Running the model
## References
[1] Jiahao Fan, Yi Li, Shaohua Wang, and Tien Nguyen. 2020. A C/C++ Code Vulnerability Dataset with Code Changes and CVE Summaries. In The 2020 International Conference on Mining Software Repositories (MSR). IEEE.

[2] Saikat Chakraborty, Rahul Krishna, Yangruibo Ding, and Baishakhi Ray. 2020. Deep Learning based Vulnerability Detection: Are We There Yet? arXiv preprint arXiv:2009.07235 (2020).

[3] Yaqin Zhou, Shangqing Liu, Jingkai Siow, Xiaoning Du, and Yang Liu. 2019. Devign: Effective vulnerability identification by learning comprehensive program semantics via graph neural networks. In Advances in Neural Information Processing Systems. 10197–10207.