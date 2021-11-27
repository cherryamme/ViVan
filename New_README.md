# 说明
old_README.txt 为软件原始的说明文档，提供了软件的功能说明和参数设置。

*py脚本已经改为3.X版本。*

ViVan_flow.png 显示了该软件的执行图，以/completeAnalysis.py 为核心的流程

![Vivanflow](ViVan_flow.png)

# 配置文件:

配置文件均放置在运行工作目录，fastq文件和参考基因组任意位置均可

## config文件
**config文件 需要配置输入的样本**

./sample-configuration-file

### 输入样本信息
参照样例,以如下格式修改: 脚本扫描(#samples_start)起始行,(#samples_end)终止行，第二列为分组，中间以/t分割，单端测序只需一个文件.

#samples_start
sample1	male	/home/jc/b2/SRR3105190_R1.fastq	/home/jc/b2/SRR3105190_R2.fastq	
sample2	male	/home/jc/b2/SRR3105191_R1.fastq	/home/jc/b2/SRR3105191_R2.fastq	
sample3	female	/home/jc/b2/SRR3105192_R1.fastq	/home/jc/b2/SRR3105192_R2.fastq
sample4	female	/home/jc/b2/SRR3105193_R1.fastq	/home/jc/b2/SRR3105193_R2.fastq
#samples_end

### 输入样本比对索引信息
参照样例,以如下格式修改: 脚本扫描(#referencesNfeatures_start)起始行,(#referencesNfeatures_end)终止行，第三列为蛋白特征CDS文件，中间以/t分割

#referencesNfeatures_start
male	/home/jc/ViVan/00_reference/GCF_000861825.2_ViralProj15428_genomic.fna	/home/jc/ViVan/ViVan-source-py3.9-jc/sample-features-file
female	/home/jc/ViVan/00_reference/GCF_000861825.2_ViralProj15428_genomic.fna	/home/jc/ViVan/ViVan-source-py3.9-jc/sample-features-file
#referencesNfeatures_end


### 筛选阈值
参照样例,以如下格式修改: 脚本扫描(#filters_start)起始行,(#filters_end)终止行，中间以/t分割

#filters_start
coverage	10
pval	0.05
#filters_end

## feature文件
./sample-features-file

脚本扫描省略#开头的行，在之后输入与reference对应的基因组的GTF内蛋白注释文件

NC_003977.2_Hepatitis_B_virus_(strain_ayw)_genome	2850	3179	CDS-HBVgp2
NC_003977.2_Hepatitis_B_virus_(strain_ayw)_genome	1376	1837	CDS-HBVgp3
NC_003977.2_Hepatitis_B_virus_(strain_ayw)_genome	1816	2451	CDS-HBVgp4


## 运行示例:

在工作目录下运行：
如果输入文件为fastq，则-a参数为必需，使用bwa比对，samtools index、sort、mpileup。
-f 后输入config文件，-c参数表示reads经过修剪和去接头
```
python completeAnalysis.py -c -I -a -f sample-configuration-file
```