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
<table border=0 cellpadding=0 cellspacing=0 width=1050 style='border-collapse:
 collapse;table-layout:fixed;width:784pt'>
 <col width=150 span=7 style='width:112pt'>
 <tr height=18 style='height:13.8pt'>
  <td height=18 class=xl70 width=150 style='height:13.8pt;width:112pt'>Dataset\Metrics(%)</td>
  <td class=xl70 width=150 style='border-left:none;width:112pt'>Baseline</td>
  <td class=xl70 width=150 style='border-left:none;width:112pt'>Devign</td>
  <td class=xl70 width=150 style='border-left:none;width:112pt'>Reveal</td>
  <td class=xl70 width=150 style='border-left:none;width:112pt'>IVDetect</td>
  <td class=xl70 width=150 style='border-left:none;width:112pt'>CodeBERT</td>
  <td class=xl70 width=150 style='border-left:none;width:112pt'>PUVD</td>
 </tr>
 <tr height=18 style='height:13.8pt'>
  <td rowspan=4 height=72 class=xl70 style='height:55.2pt;border-top:none'>FFMPeg+Qemu</td>
  <td class=xl70 style='border-top:none;border-left:none'>Acc</td>
  <td class=xl89 style='border-top:none;border-left:none'>56.89</td>
  <td class=xl89 style='border-top:none;border-left:none'>61.07</td>
  <td class=xl89 style='border-top:none;border-left:none'>57.26</td>
  <td class=xl89 style='border-top:none;border-left:none'>62.37</td>
  <td class=xl90 style='border-top:none;border-left:none'>63.14</td>
 </tr>
 <tr height=18 style='height:13.8pt'>
  <td height=18 class=xl70 style='height:13.8pt;border-top:none;border-left:
  none'>Pre</td>
  <td class=xl89 style='border-top:none;border-left:none'>52.50</td>
  <td class=xl89 style='border-top:none;border-left:none'>55.50</td>
  <td class=xl89 style='border-top:none;border-left:none'>52.37</td>
  <td class=xl90 style='border-top:none;border-left:none'>61.55</td>
  <td class=xl89 style='border-top:none;border-left:none'>58.23</td>
 </tr>
 <tr height=18 style='height:13.8pt'>
  <td height=18 class=xl70 style='height:13.8pt;border-top:none;border-left:
  none'>Rec</td>
  <td class=xl89 style='border-top:none;border-left:none'>64.67</td>
  <td class=xl90 style='border-top:none;border-left:none'>70.70</td>
  <td class=xl89 style='border-top:none;border-left:none'>57.55</td>
  <td class=xl89 style='border-top:none;border-left:none'>48.21</td>
  <td class=xl89 style='border-top:none;border-left:none'>69.88</td>
 </tr>
 <tr height=18 style='height:13.8pt'>
  <td height=18 class=xl70 style='height:13.8pt;border-top:none;border-left:
  none'>F1</td>
  <td class=xl89 style='border-top:none;border-left:none'>57.95</td>
  <td class=xl89 style='border-top:none;border-left:none'>62.19</td>
  <td class=xl89 style='border-top:none;border-left:none'>54.84</td>
  <td class=xl89 style='border-top:none;border-left:none'>54.07</td>
  <td class=xl90 style='border-top:none;border-left:none'>63.53</td>
 </tr>
 <tr height=18 style='height:13.8pt'>
  <td rowspan=4 height=72 class=xl70 style='height:55.2pt;border-top:none'>Reveal</td>
  <td class=xl70 style='border-top:none;border-left:none'>Acc</td>
  <td class=xl89 style='border-top:none;border-left:none'>87.49</td>
  <td class=xl89 style='border-top:none;border-left:none'>81.77</td>
  <td class=xl70 style='border-top:none;border-left:none'>—</td>
  <td class=xl89 style='border-top:none;border-left:none'>87.51</td>
  <td class=xl90 style='border-top:none;border-left:none'>88.96</td>
 </tr>
 <tr height=18 style='height:13.8pt'>
  <td height=18 class=xl70 style='height:13.8pt;border-top:none;border-left:
  none'>Pre</td>
  <td class=xl89 style='border-top:none;border-left:none'>31.55</td>
  <td class=xl89 style='border-top:none;border-left:none'>31.55</td>
  <td class=xl70 style='border-top:none;border-left:none'>—</td>
  <td class=xl89 style='border-top:none;border-left:none'>43.63</td>
  <td class=xl90 style='border-top:none;border-left:none'>49.14</td>
 </tr>
 <tr height=18 style='height:13.8pt'>
  <td height=18 class=xl70 style='height:13.8pt;border-top:none;border-left:
  none'>Rec</td>
  <td class=xl89 style='border-top:none;border-left:none'>36.65</td>
  <td class=xl89 style='border-top:none;border-left:none'>61.14</td>
  <td class=xl70 style='border-top:none;border-left:none'>—</td>
  <td class=xl89 style='border-top:none;border-left:none'>56.15</td>
  <td class=xl90 style='border-top:none;border-left:none'>82.38</td>
 </tr>
 <tr height=18 style='height:13.8pt'>
  <td height=18 class=xl70 style='height:13.8pt;border-top:none;border-left:
  none'>F1</td>
  <td class=xl89 style='border-top:none;border-left:none'>33.91</td>
  <td class=xl89 style='border-top:none;border-left:none'>41.62</td>
  <td class=xl70 style='border-top:none;border-left:none'>—</td>
  <td class=xl89 style='border-top:none;border-left:none'>49.10</td>
  <td class=xl90 style='border-top:none;border-left:none'>61.56</td>
 </tr>
 <tr height=18 style='height:13.8pt'>
  <td rowspan=4 height=72 class=xl70 style='height:55.2pt;border-top:none'>Fan
  et al.</td>
  <td class=xl70 style='border-top:none;border-left:none'>Acc</td>
  <td class=xl89 style='border-top:none;border-left:none'>92.78</td>
  <td class=xl89 style='border-top:none;border-left:none'>87.14</td>
  <td class=xl70 style='border-top:none;border-left:none'>—</td>
  <td class=xl90 style='border-top:none;border-left:none'>94.44</td>
  <td class=xl89 style='border-top:none;border-left:none'>92.70</td>
 </tr>
 <tr height=18 style='height:13.8pt'>
  <td height=18 class=xl70 style='height:13.8pt;border-top:none;border-left:
  none'>Pre</td>
  <td class=xl89 style='border-top:none;border-left:none'>30.61</td>
  <td class=xl89 style='border-top:none;border-left:none'>17.22</td>
  <td class=xl70 style='border-top:none;border-left:none'>—</td>
  <td class=xl90 style='border-top:none;border-left:none'>50.50</td>
  <td class=xl89 style='border-top:none;border-left:none'>38.00</td>
 </tr>
 <tr height=18 style='height:13.8pt'>
  <td height=18 class=xl70 style='height:13.8pt;border-top:none;border-left:
  none'>Rec</td>
  <td class=xl89 style='border-top:none;border-left:none'>15.96</td>
  <td class=xl89 style='border-top:none;border-left:none'>34.04</td>
  <td class=xl70 style='border-top:none;border-left:none'>—</td>
  <td class=xl89 style='border-top:none;border-left:none'>28.53</td>
  <td class=xl90 style='border-top:none;border-left:none'>42.56</td>
 </tr>
 <tr height=18 style='height:13.8pt'>
  <td height=18 class=xl70 style='height:13.8pt;border-top:none;border-left:
  none'>F1</td>
  <td class=xl89 style='border-top:none;border-left:none'>20.98</td>
  <td class=xl89 style='border-top:none;border-left:none'>22.87</td>
  <td class=xl70 style='border-top:none;border-left:none'>—</td>
  <td class=xl89 style='border-top:none;border-left:none'>36.46</td>
  <td class=xl90 style='border-top:none;border-left:none'>39.46</td>
 </tr>
</table>

### Results of RQ2

<table border=0 cellpadding=0 cellspacing=0 width=1050 style='border-collapse:
 collapse;table-layout:fixed;width:784pt'>
 <col width=150 span=7 style='width:112pt'>
 <tr height=18 style='height:13.8pt'>
  <td height=18 class=xl89 width=150 style='height:13.8pt;width:112pt'>Dataset\Metrics(%)</td>
  <td class=xl89 width=150 style='border-left:none;width:112pt'>Baseline</td>
  <td class=xl89 width=150 style='border-left:none;width:112pt'>CR SVM</td>
  <td class=xl89 width=150 style='border-left:none;width:112pt'>uPU</td>
  <td class=xl89 width=150 style='border-left:none;width:112pt'>nnPU</td>
  <td class=xl89 width=150 style='border-left:none;width:112pt'>Self-PU</td>
  <td class=xl89 width=150 style='border-left:none;width:112pt'>PUVD</td>
 </tr>
 <tr height=18 style='height:13.8pt'>
  <td rowspan=4 height=72 class=xl89 style='height:55.2pt;border-top:none'>FFMPeg+Qemu</td>
  <td class=xl89 style='border-top:none;border-left:none'>Acc</td>
  <td class=xl89 style='border-top:none;border-left:none'>48.99</td>
  <td class=xl89 style='border-top:none;border-left:none'>56.08</td>
  <td class=xl91 style='border-top:none;border-left:none'>56.01</td>
  <td class=xl91 style='border-top:none;border-left:none'>53.69</td>
  <td class=xl91 style='border-top:none;border-left:none'>58.38</td>
 </tr>
 <tr height=18 style='height:13.8pt'>
  <td height=18 class=xl89 style='height:13.8pt;border-top:none;border-left:
  none'>Pre</td>
  <td class=xl89 style='border-top:none;border-left:none'>45.83</td>
  <td class=xl89 style='border-top:none;border-left:none'>54.43</td>
  <td class=xl91 style='border-top:none;border-left:none'>50.20</td>
  <td class=xl91 style='border-top:none;border-left:none'>50.15</td>
  <td class=xl91 style='border-top:none;border-left:none'>54.66</td>
 </tr>
 <tr height=18 style='height:13.8pt'>
  <td height=18 class=xl89 style='height:13.8pt;border-top:none;border-left:
  none'>Rec</td>
  <td class=xl89 style='border-top:none;border-left:none'>60.80</td>
  <td class=xl89 style='border-top:none;border-left:none'>30.15</td>
  <td class=xl91 style='border-top:none;border-left:none'>41.96</td>
  <td class=xl91 style='border-top:none;border-left:none'>44.30</td>
  <td class=xl91 style='border-top:none;border-left:none'>55.48</td>
 </tr>
 <tr height=18 style='height:13.8pt'>
  <td height=18 class=xl89 style='height:13.8pt;border-top:none;border-left:
  none'>F1</td>
  <td class=xl89 style='border-top:none;border-left:none'>52.21</td>
  <td class=xl89 style='border-top:none;border-left:none'>38.74</td>
  <td class=xl91 style='border-top:none;border-left:none'>46.60</td>
  <td class=xl91 style='border-top:none;border-left:none'>45.85</td>
  <td class=xl91 style='border-top:none;border-left:none'>54.99</td>
 </tr>
 <tr height=18 style='height:13.8pt'>
  <td rowspan=4 height=72 class=xl89 style='height:55.2pt;border-top:none'>Reveal</td>
  <td class=xl89 style='border-top:none;border-left:none'>Acc</td>
  <td class=xl89 style='border-top:none;border-left:none'>86.10</td>
  <td class=xl91 style='border-top:none;border-left:none'>83.09</td>
  <td class=xl91 style='border-top:none;border-left:none'>83.07</td>
  <td class=xl91 style='border-top:none;border-left:none'>84.41</td>
  <td class=xl91 style='border-top:none;border-left:none'>86.99</td>
 </tr>
 <tr height=18 style='height:13.8pt'>
  <td height=18 class=xl89 style='height:13.8pt;border-top:none;border-left:
  none'>Pre</td>
  <td class=xl89 style='border-top:none;border-left:none'>7.87</td>
  <td class=xl91 style='border-top:none;border-left:none'>28.79</td>
  <td class=xl91 style='border-top:none;border-left:none'>28.93</td>
  <td class=xl91 style='border-top:none;border-left:none'>22.01</td>
  <td class=xl91 style='border-top:none;border-left:none'>40.83</td>
 </tr>
 <tr height=18 style='height:13.8pt'>
  <td height=18 class=xl89 style='height:13.8pt;border-top:none;border-left:
  none'>Rec</td>
  <td class=xl89 style='border-top:none;border-left:none'>9.12</td>
  <td class=xl91 style='border-top:none;border-left:none'>26.55</td>
  <td class=xl91 style='border-top:none;border-left:none'>27.18</td>
  <td class=xl91 style='border-top:none;border-left:none'>17.32</td>
  <td class=xl91 style='border-top:none;border-left:none'>47.34</td>
 </tr>
 <tr height=18 style='height:13.8pt'>
  <td height=18 class=xl89 style='height:13.8pt;border-top:none;border-left:
  none'>F1</td>
  <td class=xl89 style='border-top:none;border-left:none'>7.80</td>
  <td class=xl91 style='border-top:none;border-left:none'>24.75</td>
  <td class=xl91 style='border-top:none;border-left:none'>25.38</td>
  <td class=xl91 style='border-top:none;border-left:none'>18.61</td>
  <td class=xl91 style='border-top:none;border-left:none'>43.82</td>
 </tr>
 <tr height=18 style='height:13.8pt'>
  <td rowspan=4 height=72 class=xl89 style='height:55.2pt;border-top:none'>Fan
  et al.</td>
  <td class=xl89 style='border-top:none;border-left:none'>Acc</td>
  <td class=xl89 style='border-top:none;border-left:none'>85.66</td>
  <td class=xl91 style='border-top:none;border-left:none'>91.44</td>
  <td class=xl91 style='border-top:none;border-left:none'>91.45</td>
  <td class=xl91 style='border-top:none;border-left:none'>89.52</td>
  <td class=xl91 style='border-top:none;border-left:none'>91.92</td>
 </tr>
 <tr height=18 style='height:13.8pt'>
  <td height=18 class=xl89 style='height:13.8pt;border-top:none;border-left:
  none'>Pre</td>
  <td class=xl89 style='border-top:none;border-left:none'>9.57</td>
  <td class=xl91 style='border-top:none;border-left:none'>24.52</td>
  <td class=xl91 style='border-top:none;border-left:none'>25.15</td>
  <td class=xl91 style='border-top:none;border-left:none'>19.75</td>
  <td class=xl91 style='border-top:none;border-left:none'>29.05</td>
 </tr>
 <tr height=18 style='height:13.8pt'>
  <td height=18 class=xl89 style='height:13.8pt;border-top:none;border-left:
  none'>Rec</td>
  <td class=xl89 style='border-top:none;border-left:none'>6.18</td>
  <td class=xl91 style='border-top:none;border-left:none'>11.22</td>
  <td class=xl91 style='border-top:none;border-left:none'>10.77</td>
  <td class=xl91 style='border-top:none;border-left:none'>9.39</td>
  <td class=xl91 style='border-top:none;border-left:none'>30.30</td>
 </tr>
 <tr height=18 style='height:13.8pt'>
  <td height=18 class=xl89 style='height:13.8pt;border-top:none;border-left:
  none'>F1</td>
  <td class=xl89 style='border-top:none;border-left:none'>6.72</td>
  <td class=xl91 style='border-top:none;border-left:none'>10.62</td>
  <td class=xl91 style='border-top:none;border-left:none'>9.79</td>
  <td class=xl91 style='border-top:none;border-left:none'>9.04</td>
  <td class=xl91 style='border-top:none;border-left:none'>29.55</td>
 </tr>

</table>

### Results of RQ3

<table border=0 cellpadding=0 cellspacing=0 width=600 style='border-collapse:
 collapse;table-layout:fixed;width:448pt'>
 <col width=150 span=4 style='width:112pt'>
 <tr height=18 style='height:13.8pt'>
  <td height=18 class=xl89 width=150 style='height:13.8pt;width:112pt'>Dataset</td>
  <td class=xl89 width=150 style='border-left:none;width:112pt'>Module</td>
  <td class=xl89 width=150 style='border-left:none;width:112pt'>Acc</td>
  <td class=xl89 width=150 style='border-left:none;width:112pt'>F1</td>
 </tr>
 <tr height=18 style='height:13.8pt'>
  <td rowspan=4 height=72 class=xl89 style='height:55.2pt;border-top:none'>FFMPeg+Qemu</td>
  <td class=xl89 style='border-top:none;border-left:none'>w/o ID Prototype</td>
  <td class=xl89 style='border-top:none;border-left:none'>56.30</td>
  <td class=xl89 style='border-top:none;border-left:none'>47.35</td>
 </tr>
 <tr height=18 style='height:13.8pt'>
  <td height=18 class=xl89 style='height:13.8pt;border-top:none;border-left:
  none'>w/o Pfine-tuning</td>
  <td class=xl89 style='border-top:none;border-left:none'>56.77</td>
  <td class=xl89 style='border-top:none;border-left:none'>58.17</td>
 </tr>
 <tr height=18 style='height:13.8pt'>
  <td height=18 class=xl89 style='height:13.8pt;border-top:none;border-left:
  none'>w/o RPML</td>
  <td class=xl89 style='border-top:none;border-left:none'>58.71</td>
  <td class=xl89 style='border-top:none;border-left:none'>55.49</td>
 </tr>
 <tr height=18 style='height:13.8pt'>
  <td height=18 class=xl89 style='height:13.8pt;border-top:none;border-left:
  none'>PUVD</td>
  <td class=xl89 style='border-top:none;border-left:none'>59.30</td>
  <td class=xl89 style='border-top:none;border-left:none'>57.23</td>
 </tr>
 <tr height=18 style='height:13.8pt'>
  <td rowspan=4 height=72 class=xl89 style='height:55.2pt;border-top:none'>Reveal</td>
  <td class=xl89 style='border-top:none;border-left:none'>w/o ID Prototype</td>
  <td class=xl89 style='border-top:none;border-left:none'>73.97</td>
  <td class=xl91 style='border-top:none;border-left:none'>41.27</td>
 </tr>
 <tr height=18 style='height:13.8pt'>
  <td height=18 class=xl89 style='height:13.8pt;border-top:none;border-left:
  none'>w/o Pfine-tuning</td>
  <td class=xl89 style='border-top:none;border-left:none'>60.47</td>
  <td class=xl91 style='border-top:none;border-left:none'>32.66</td>
 </tr>
 <tr height=18 style='height:13.8pt'>
  <td height=18 class=xl89 style='height:13.8pt;border-top:none;border-left:
  none'>w/o RPML</td>
  <td class=xl89 style='border-top:none;border-left:none'>80.43</td>
  <td class=xl91 style='border-top:none;border-left:none'>48.20</td>
 </tr>
 <tr height=18 style='height:13.8pt'>
  <td height=18 class=xl89 style='height:13.8pt;border-top:none;border-left:
  none'>PUVD</td>
  <td class=xl89 style='border-top:none;border-left:none'>85.79</td>
  <td class=xl91 style='border-top:none;border-left:none'>54.18</td>
 </tr>
 <tr height=18 style='height:13.8pt'>
  <td rowspan=4 height=72 class=xl89 style='height:55.2pt;border-top:none'>Fan
  et al.</td>
  <td class=xl89 style='border-top:none;border-left:none'>w/o ID Prototype</td>
  <td class=xl89 style='border-top:none;border-left:none'>72.90</td>
  <td class=xl91 style='border-top:none;border-left:none'>21.83</td>
 </tr>
 <tr height=18 style='height:13.8pt'>
  <td height=18 class=xl89 style='height:13.8pt;border-top:none;border-left:
  none'>w/o Pfine-tuning</td>
  <td class=xl89 style='border-top:none;border-left:none'>57.43</td>
  <td class=xl91 style='border-top:none;border-left:none'>18.09</td>
 </tr>
 <tr height=18 style='height:13.8pt'>
  <td height=18 class=xl89 style='height:13.8pt;border-top:none;border-left:
  none'>w/o RPML</td>
  <td class=xl89 style='border-top:none;border-left:none'>77.77</td>
  <td class=xl91 style='border-top:none;border-left:none'>24.19</td>
 </tr>
 <tr height=18 style='height:13.8pt'>
  <td height=18 class=xl89 style='height:13.8pt;border-top:none;border-left:
  none'>PUVD</td>
  <td class=xl89 style='border-top:none;border-left:none'>87.62</td>
  <td class=xl91 style='border-top:none;border-left:none'>28.70</td>
 </tr>
</table>

### Results of RQ4


## References
[1] Jiahao Fan, Yi Li, Shaohua Wang, and Tien Nguyen. 2020. A C/C++ Code Vulnerability Dataset with Code Changes and CVE Summaries. In The 2020 International Conference on Mining Software Repositories (MSR). IEEE.

[2] Saikat Chakraborty, Rahul Krishna, Yangruibo Ding, and Baishakhi Ray. 2020. Deep Learning based Vulnerability Detection: Are We There Yet? arXiv preprint arXiv:2009.07235 (2020).

[3] Yaqin Zhou, Shangqing Liu, Jingkai Siow, Xiaoning Du, and Yang Liu. 2019. Devign: Effective vulnerability identification by learning comprehensive program semantics via graph neural networks. In Advances in Neural Information Processing Systems. 10197–10207.