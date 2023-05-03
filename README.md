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

To download the dataset used for evaluation in our experiments, run the following commands:
    
    # If you want to download multiple datasets, please note the overlay of the storage location!
    cd data_raw
    gdown path_Devign(path_Reveal/path_Fan)
    cd ..
    python split data_Devign(Reveal/Fan).py

## Running the model
## Results
### Results of RQ1
<table border=0 cellpadding=0 cellspacing=0 width=898 style='border-collapse:
 collapse;table-layout:fixed;width:673pt'>
 <col width=130 style='mso-width-source:userset;mso-width-alt:4608;width:97pt'>
 <col width=64 span=12 style='width:48pt'>
 <tr height=26 style='mso-height-source:userset;height:19.95pt'>
  <td height=26 class=xl70 width=130 style='height:19.95pt;width:97pt'>Metrics(%)\Dataset</td>
  <td colspan=4 class=xl69 width=256 style='width:192pt'>FFMPeg+Qemu</td>
  <td colspan=4 class=xl70 width=256 style='border-left:none;width:192pt'>Reveal</td>
  <td colspan=4 class=xl70 width=256 style='border-left:none;width:192pt'>Fan
  et al.</td>
 </tr>
 <tr height=26 style='mso-height-source:userset;height:19.95pt'>
  <td height=26 class=xl71 style='height:19.95pt;border-top:none'>Baseline</td>
  <td class=xl65 style='border-top:none;border-left:none'>Acc</td>
  <td class=xl72 style='border-top:none'>Pre</td>
  <td class=xl72 style='border-top:none'>Rec</td>
  <td class=xl73 style='border-top:none'>F1</td>
  <td class=xl65 style='border-top:none;border-left:none'>Acc</td>
  <td class=xl72 style='border-top:none'>Pre</td>
  <td class=xl72 style='border-top:none'>Rec</td>
  <td class=xl73 style='border-top:none'>F1</td>
  <td class=xl72 style='border-top:none'>Acc</td>
  <td class=xl72 style='border-top:none'>Pre</td>
  <td class=xl72 style='border-top:none'>Rec</td>
  <td class=xl73 style='border-top:none'>F1</td>
 </tr>
 <tr height=26 style='mso-height-source:userset;height:19.95pt'>
  <td height=26 class=xl74 style='height:19.95pt'>Devign</td>
  <td class=xl80 style='border-left:none'>56.89</td>
  <td class=xl78>52.50</td>
  <td class=xl78>64.67</td>
  <td class=xl79>57.95</td>
  <td class=xl80 style='border-left:none'>87.49</td>
  <td class=xl78>31.55</td>
  <td class=xl78>36.65</td>
  <td class=xl79>33.91</td>
  <td class=xl78>92.78</td>
  <td class=xl78>30.61</td>
  <td class=xl78>15.96</td>
  <td class=xl79>20.98</td>
 </tr>
 <tr height=26 style='mso-height-source:userset;height:19.95pt'>
  <td height=26 class=xl74 style='height:19.95pt'>Reveal</td>
  <td class=xl80 style='border-left:none'>61.07</td>
  <td class=xl78>55.50</td>
  <td class=xl85>70.70</td>
  <td class=xl79>62.19</td>
  <td class=xl80 style='border-left:none'>81.77</td>
  <td class=xl78>31.55</td>
  <td class=xl78>61.14</td>
  <td class=xl79>41.62</td>
  <td class=xl78>87.14</td>
  <td class=xl78>17.22</td>
  <td class=xl78>34.04</td>
  <td class=xl79>22.87</td>
 </tr>
 <tr height=26 style='mso-height-source:userset;height:19.95pt'>
  <td height=26 class=xl74 style='height:19.95pt'>IVDetect</td>
  <td class=xl80 style='border-left:none'>57.26</td>
  <td class=xl78>52.37</td>
  <td class=xl78>57.55</td>
  <td class=xl79>54.84</td>
  <td class=xl66 style='border-left:none'>—</td>
  <td class=xl67>—</td>
  <td class=xl67>—</td>
  <td class=xl68>—</td>
  <td class=xl67>—</td>
  <td class=xl67>—</td>
  <td class=xl67>—</td>
  <td class=xl68>—</td>
 </tr>
 <tr height=26 style='mso-height-source:userset;height:19.95pt'>
  <td height=26 class=xl75 style='height:19.95pt'>CodeBERT</td>
  <td class=xl81 style='border-left:none'>62.37</td>
  <td class=xl83>61.55</td>
  <td class=xl76>48.21</td>
  <td class=xl77>54.07</td>
  <td class=xl81 style='border-left:none'>87.51</td>
  <td class=xl76>43.63</td>
  <td class=xl76>56.15</td>
  <td class=xl77>49.10</td>
  <td class=xl83>94.44</td>
  <td class=xl83>50.50</td>
  <td class=xl76>28.53</td>
  <td class=xl77>36.46</td>
 </tr>
 <tr height=26 style='mso-height-source:userset;height:19.95pt'>
  <td height=26 class=xl70 style='height:19.95pt;border-top:none'>PUVD</td>
  <td class=xl84 style='border-top:none;border-left:none'>63.14</td>
  <td class=xl82 style='border-top:none'>58.23</td>
  <td class=xl82 style='border-top:none'>69.88</td>
  <td class=xl86 style='border-top:none'>63.53</td>
  <td class=xl84 style='border-top:none;border-left:none'>88.96</td>
  <td class=xl87 style='border-top:none'>49.14</td>
  <td class=xl87 style='border-top:none'>82.38</td>
  <td class=xl86 style='border-top:none'>61.56</td>
  <td class=xl76>92.70</td>
  <td class=xl76>38.00</td>
  <td class=xl83>42.56</td>
  <td class=xl88>39.46</td>
 </tr>
 <![if supportMisalignedColumns]>
 <tr height=0 style='display:none'>
  <td width=130 style='width:97pt'></td>
  <td width=64 style='width:48pt'></td>
  <td width=64 style='width:48pt'></td>
  <td width=64 style='width:48pt'></td>
  <td width=64 style='width:48pt'></td>
  <td width=64 style='width:48pt'></td>
  <td width=64 style='width:48pt'></td>
  <td width=64 style='width:48pt'></td>
  <td width=64 style='width:48pt'></td>
  <td width=64 style='width:48pt'></td>
  <td width=64 style='width:48pt'></td>
  <td width=64 style='width:48pt'></td>
  <td width=64 style='width:48pt'></td>
 </tr>
 <![endif]>
</table>
### Results of RQ2
### Results of RQ3
### Results of RQ4
### Ablation Study Results 

## References
[1] Jiahao Fan, Yi Li, Shaohua Wang, and Tien Nguyen. 2020. A C/C++ Code Vulnerability Dataset with Code Changes and CVE Summaries. In The 2020 International Conference on Mining Software Repositories (MSR). IEEE.

[2] Saikat Chakraborty, Rahul Krishna, Yangruibo Ding, and Baishakhi Ray. 2020. Deep Learning based Vulnerability Detection: Are We There Yet? arXiv preprint arXiv:2009.07235 (2020).

[3] Yaqin Zhou, Shangqing Liu, Jingkai Siow, Xiaoning Du, and Yang Liu. 2019. Devign: Effective vulnerability identification by learning comprehensive program semantics via graph neural networks. In Advances in Neural Information Processing Systems. 10197–10207.