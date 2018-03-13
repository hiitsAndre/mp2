#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 18:36:55 2018

@author: Daoji Zhang
"""
#the first line is the start node, and node[1]-node[5] are the widgets, the second line is the path, the third line is the expanded node
MinStop(n=3) Average:544.8
('S', 'AEA', 'BBA', 'DDA', 'EAC', 'CBE')
['C', 'B', 'B', 'D', 'D', 'A', 'E', 'A', 'C']
1008

('S', 'ABC', 'CDC', 'CDC', 'CCB', 'ECD')
['E', 'C', 'D', 'C', 'A', 'B', 'C']
210

('S', 'EBB', 'DBC', 'CEC', 'DEA', 'AEA')
['D', 'A', 'C', 'E', 'A', 'B', 'C', 'B']
661

('S', 'CDA', 'CCB', 'BDD', 'BAA', 'DDE')
['C', 'C', 'B', 'D', 'A', 'D', 'A', 'E']
579

('S', 'EDA', 'DDA', 'ECE', 'EDC', 'AEA')
['E', 'D', 'D', 'A', 'C', 'E', 'A']
266

MinStop(n=4) Average:1148
('S', 'ADCC', 'AABC', 'DADD', 'ABEA', 'DEAA')
['A', 'D', 'B', 'E', 'A', 'B', 'C', 'A', 'C', 'D', 'D']
1338

('S', 'EBAD', 'ACAE', 'DBBA', 'DDDE', 'EDBC')
['E', 'D', 'B', 'B', 'A', 'C', 'D', 'A', 'D', 'E']
1272

('S', 'DEBA', 'CDEE', 'EECA', 'CCCD', 'CBEA')
['C', 'D', 'E', 'B', 'E', 'C', 'A', 'C', 'D']
938

('S', 'ACEE', 'AADB', 'AECD', 'EBEA', 'EABA')
['A', 'E', 'A', 'C', 'D', 'B', 'E', 'A', 'E']
791

('S', 'ADCB', 'CCDD', 'BCED', 'AADD', 'ABDA')
['A', 'A', 'D', 'C', 'B', 'C', 'E', 'D', 'A', 'D']
1401

MinStop(n=5) Average: 3508.8
('S', 'EBCCE', 'CBDBE', 'AEEED', 'ACACD', 'DACDC')
['A', 'C', 'E', 'B', 'D', 'A', 'C', 'D', 'C', 'B', 'E', 'E', 'D']
5163

('S', 'CCDDC', 'ADBDD', 'EDECE', 'AEAEC', 'BAEAE')
['B', 'A', 'E', 'A', 'D', 'E', 'C', 'B', 'C', 'D', 'D', 'C', 'E']
4741

('S', 'ACEEE', 'EDCEE', 'DECED', 'EACEE', 'BDADB')
['B', 'D', 'E', 'A', 'D', 'C', 'E', 'E', 'B', 'D', 'E']
2359

('S', 'CACBA', 'EDBCB', 'DEAEB', 'EEEDD', 'DADBE')
['D', 'E', 'C', 'A', 'D', 'B', 'E', 'C', 'B', 'A', 'E', 'D', 'D']
4171

('S', 'CEACD', 'BECCC', 'BEECD', 'EECAB', 'EACBC')
['B', 'E', 'C', 'E', 'C', 'A', 'C', 'B', 'D', 'C']
1110   

MinStop(n=6) Average: 8277.6
('S', 'CCECBC', 'AEDAAD', 'EEDCAD', 'BEBBEB', 'DDEBCE')
['A', 'B', 'E', 'E', 'D', 'C', 'A', 'A', 'D', 'C', 'E', 'B', 'C', 'B', 'E', 'B', 'C']
14301

('S', 'EBDEEB', 'BDDDAA', 'DEACCE', 'EEAACE', 'DAEEBC')
['E', 'B', 'D', 'E', 'D', 'D', 'A', 'A', 'C', 'C', 'E', 'E', 'B', 'C']
7086

('S', 'CDDBAE', 'CDBCCA', 'BAECED', 'DCCCDB', 'EECDAC')
['C', 'D', 'D', 'B', 'A', 'E', 'C', 'E', 'C', 'D', 'A', 'C', 'D', 'B']
5596

('S', 'EEDCEA', 'CCEADD', 'DEDDCA', 'ADAEDC', 'CCABAA')
['C', 'C', 'E', 'A', 'D', 'B', 'A', 'E', 'D', 'D', 'C', 'E', 'A']
4198

('S', 'CDBEBB', 'EDAAAC', 'AAEDDE', 'EAECBA', 'BECBCB')
['E', 'C', 'D', 'A', 'A', 'B', 'E', 'C', 'B', 'A', 'C', 'B', 'D', 'D', 'E']
10207
    
MinStop(n=7) Average: 15620.4
('S', 'CDCECCC', 'ABADAEC', 'ADDEDEB', 'BBBADAD', 'AACDCDC')
['A', 'B', 'B', 'B', 'A', 'C', 'D', 'A', 'C', 'D', 'E', 'C', 'C', 'C', 'D', 'E', 'B']
15261

('S', 'EDDDABC', 'EDDBAEE', 'DBEDAAC', 'ACBBDCC', 'AADCECD')
['E', 'D', 'D', 'B', 'E', 'D', 'A', 'A', 'C', 'B', 'B', 'D', 'C', 'E', 'C', 'D', 'E']
11056

('S', 'CACCCEE', 'AABACAD', 'EEBBDDB', 'ADCCBEC', 'CCBDEDD')
['C', 'A', 'C', 'A', 'B', 'D', 'A', 'C', 'C', 'E', 'E', 'B', 'A', 'B', 'D', 'D', 'B', 'E', 'C']
26815

('S', 'ABBBDDC', 'CDBCCBB', 'ADDABBD', 'DBECDED', 'BDECCBA')
['A', 'C', 'D', 'B', 'D', 'E', 'C', 'C', 'A', 'B', 'B', 'D', 'E', 'D', 'A', 'C']
17253

('S', 'ABDBDBB', 'DECBDBD', 'EACECCA', 'BCDEADB', 'DEADCDD')
['D', 'E', 'A', 'B', 'C', 'D', 'B', 'E', 'C', 'C', 'A', 'D', 'B', 'D', 'B']
7717

MinStop(n=8) Average: 19688.8
('S', 'BADDCAEC', 'CABEEEAD', 'DABCAEDA', 'DAEEBEDC', 'ACCDBCEA')
['B', 'A', 'C', 'C', 'D', 'A', 'B', 'D', 'C', 'E', 'A', 'E', 'B', 'E', 'D', 'A', 'C', 'D']
19462

('S', 'DCDBADBC', 'CCCABCBC', 'DAAACCCA', 'ECCCEACB', 'DAAABACC')
['D', 'A', 'A', 'A', 'E', 'C', 'C', 'C', 'D', 'B', 'E', 'A', 'D', 'B', 'C', 'B', 'C']
11848

('S', 'AABDBCAD', 'EEAEEBAD', 'CECEDEAC', 'DDEDACEA', 'AACAECDB')
['A', 'A', 'C', 'D', 'D', 'E', 'C', 'E', 'D', 'A', 'E', 'C', 'E', 'B', 'A', 'D', 'B', 'C', 'A', 'D']
23102

('S', 'ACBAEDCD', 'EEBBCAEA', 'ABDCAADD', 'DCBDDEDE', 'ACCDBAEA')
['A', 'E', 'E', 'B', 'D', 'C', 'B', 'C', 'D', 'B', 'A', 'D', 'E', 'A', 'D', 'C', 'D', 'E']
19649

('S', 'CEBEDEEC', 'BDCEACDB', 'EAAAEDAA', 'CCBEAAAE', 'ADBEAEDC')
['B', 'D', 'C', 'E', 'A', 'C', 'D', 'B', 'E', 'A', 'A', 'E', 'D', 'A', 'E', 'E', 'C', 'A']
24383

#for MinDistance, first line is the start node that contains widget1-5, second line is path, third line is MinDistance, last line is expanded nodes
MinDistance(n=3) Average: 57.2
('S', 'ADA', 'BAC', 'CDE', 'AAE', 'BCD')
['B', 'E', 'A', 'A', 'C', 'E', 'D', 'E', 'A']
2737
34

('S', 'BAD', 'CDD', 'CAD', 'BCC', 'ACD')
['B', 'E', 'A', 'C', 'C', 'A', 'E', 'D', 'D']
2624
17

('S', 'BCA', 'ABB', 'EEA', 'ACC', 'ACE')
['A', 'E', 'B', 'B', 'E', 'C', 'C', 'E', 'A']
2026
32

('S', 'EEE', 'EDE', 'EAD', 'DDC', 'DDE')
['E', 'A', 'E', 'D', 'D', 'E', 'C']
1727
41

('S', 'BBD', 'CEB', 'DBE', 'BBA', 'EBC')
['E', 'B', 'B', 'E', 'D', 'E', 'C', 'E', 'B', 'E', 'A']
3197
162

MinDistance(n=4) Average: 314
('S', 'EDDE', 'ACEC', 'DAAC', 'BCBE', 'ABCE')
['E', 'D', 'D', 'E', 'A', 'A', 'E', 'B', 'E', 'C', 'E', 'B', 'E', 'C']
3873
170

('S', 'DAAB', 'CCEB', 'BBBD', 'ECBA', 'BADE')
['D', 'E', 'C', 'C', 'E', 'B', 'B', 'B', 'E', 'A', 'A', 'E', 'D', 'E', 'B']
3524
305

('S', 'BEDB', 'EDBA', 'EABD', 'DDCE', 'CCAC')
['C', 'C', 'E', 'A', 'E', 'B', 'E', 'D', 'D', 'E', 'B', 'E', 'C', 'E', 'A']
4150
483

('S', 'DDDE', 'ADBA', 'CAEB', 'DDDB', 'AAEC')
['C', 'A', 'A', 'E', 'D', 'D', 'D', 'E', 'B', 'E', 'A', 'C']
3348
124

('S', 'BBEB', 'DAAE', 'CDCE', 'ECCC', 'BADB')
['C', 'E', 'B', 'B', 'E', 'A', 'E', 'D', 'E', 'A', 'A', 'C', 'C', 'C', 'E', 'B']
4087
488

MinDistance(n=5) Average: 822.4
('S', 'EDDDC', 'BBCDE', 'CCCDA', 'CBEBC', 'ADEDC')
['B', 'B', 'E', 'A', 'C', 'C', 'C', 'E', 'D', 'E', 'B', 'E', 'B', 'E', 'D', 'D', 'E', 'A', 'C']
5532
2382

runfile('/Users/mac/RandomGenerator.py', wdir='/Users/mac')
('S', 'CCACA', 'CAAAE', 'AAEDE', 'DEEDA', 'DCBDE')
['C', 'C', 'E', 'D', 'E', 'A', 'A', 'A', 'C', 'E', 'B', 'E', 'D', 'E', 'A']
4247
366

runfile('/Users/mac/RandomGenerator.py', wdir='/Users/mac')
('S', 'ABCEC', 'CAEED', 'AABCB', 'DEDAD', 'DAEBC')
['D', 'E', 'A', 'A', 'E', 'B', 'E', 'D', 'E', 'C', 'A', 'E', 'B', 'E', 'D', 'E', 'C']
5585
947

runfile('/Users/mac/RandomGenerator.py', wdir='/Users/mac')
('S', 'DEBEA', 'EBEDD', 'BAAAC', 'DABEB', 'AABDB')
['D', 'E', 'A', 'A', 'E', 'B', 'E', 'D', 'D', 'E', 'B', 'E', 'A', 'A', 'A', 'C']
4013
318

runfile('/Users/mac/RandomGenerator.py', wdir='/Users/mac')
('S', 'ACCBA', 'ABBDA', 'EDBDA', 'EDADA', 'DAAAC')
['E', 'D', 'E', 'A', 'A', 'A', 'C', 'C', 'E', 'B', 'B', 'E', 'D', 'E', 'A']
3848
99

MinDistance(n=6) Average: 922.6
('S', 'CEBCAB', 'CEBCED', 'ACEEBC', 'DBBCCD', 'ADEDEA')
['A', 'C', 'E', 'D', 'E', 'B', 'B', 'E', 'C', 'C', 'E', 'D', 'E', 'A', 'E', 'B']
4983
263

('S', 'ABABDD', 'BAAADA', 'CAADAC', 'ECDDBB', 'DBDAAD')
['D', 'E', 'C', 'A', 'A', 'E', 'B', 'E', 'D', 'D', 'E', 'A', 'A', 'A', 'E', 'B', 'B', 'E', 'D', 'D', 'E', 'A', 'C']
6136
2508

('S', 'BADDDA', 'ABEECD', 'EEABEE', 'CCADED', 'CCBDCC')
['C', 'C', 'E', 'E', 'A', 'E', 'B', 'E', 'E', 'A', 'E', 'D', 'D', 'D', 'E', 'C', 'C', 'A', 'E', 'D']
4691
585

('S', 'EDCEDD', 'DCECDA', 'AEECAB', 'CDBCCD', 'EEBECC')
['D', 'E', 'A', 'E', 'E', 'C', 'A', 'E', 'D', 'E', 'B', 'E', 'C', 'C', 'E', 'D', 'D', 'E', 'A']
5587
937

('S', 'DDDBCE', 'DABBEC', 'BEDEBB', 'DAAABD', 'AAEEEC')
['B', 'E', 'D', 'D', 'D', 'E', 'A', 'A', 'A', 'E', 'B', 'B', 'E', 'E', 'C', 'E', 'D']
3524
319

MinDistance(n=7) Average: 955.4
('S', 'DACABBE', 'DDDEBBC', 'ECEBABB', 'BAEDDCE', 'DDAEBDA')
['D', 'D', 'D', 'E', 'A', 'C', 'E', 'B', 'B', 'E', 'A', 'E', 'D', 'D', 'E', 'B', 'B', 'E', 'C', 'E', 'A']
5487
1158

('S', 'CAEDEAB', 'CAADDED', 'CBEDADB', 'BBEADDD', 'ECBDCAC')
['E', 'C', 'A', 'A', 'E', 'B', 'B', 'E', 'D', 'D', 'E', 'C', 'A', 'E', 'D', 'D', 'D', 'E', 'B', 'E', 'C']
5993
1041

('S', 'AADDCDE', 'CCAEACD', 'CCCDBBB', 'ADBBEDC', 'BACAADA')
['C', 'C', 'C', 'A', 'A', 'E', 'D', 'D', 'E', 'B', 'B', 'B', 'E', 'A', 'C', 'A', 'A', 'E', 'D', 'E', 'A', 'C']
6022
1329

('S', 'ACACABA', 'ABCDDDB', 'BACEDBE', 'BAABADB', 'CDDDDCE')
['B', 'E', 'A', 'A', 'E', 'B', 'E', 'C', 'A', 'E', 'D', 'D', 'D', 'D', 'E', 'C', 'A', 'E', 'B', 'E', 'A']
5988
463

('S', 'DCBBBEB', 'DBAEDEA', 'DDDEEDC', 'BEADCBE', 'CCCABCB')
['D', 'D', 'D', 'E', 'C', 'C', 'C', 'A', 'E', 'B', 'B', 'B', 'E', 'A', 'E', 'D', 'E', 'C', 'E', 'B', 'E', 'A']
5487
986

MinDistance(n=8) Average: 1550.6
('S', 'BDBCEDCE', 'DBCDBEBA', 'BDCEADBC', 'BADDCCEE', 'AABDDDDB')
['B', 'E', 'A', 'A', 'E', 'D', 'D', 'E', 'B', 'E', 'C', 'C', 'E', 'A', 'E', 'D', 'D', 'D', 'D', 'E', 'B', 'E', 'B', 'E', 'C', 'E', 'A']
6888
1348

('S', 'BDCEDBCC', 'BADCBCCD', 'BEABDAAC', 'EBEEEDBD', 'CABEAABB')
['B', 'E', 'A', 'E', 'D', 'E', 'C', 'A', 'E', 'B', 'E', 'E', 'E', 'D', 'E', 'A', 'A', 'E', 'B', 'B', 'E', 'C', 'C', 'E', 'D']
6875
1865

('S', 'ADECBCCA', 'EBBDACAC', 'ABCABEAA', 'BBABCCBE', 'CAEEEDBA')
['C', 'A', 'E', 'E', 'B', 'B', 'E', 'D', 'E', 'A', 'C', 'A', 'E', 'B', 'E', 'C', 'C', 'E', 'B', 'E', 'A', 'A']
6721
1588

('S', 'CDAEDDAE', 'DBDEBABD', 'AACEBAAE', 'EDBEACCB', 'EAEEAEEA')
['E', 'D', 'E', 'B', 'E', 'A', 'A', 'C', 'C', 'E', 'D', 'E', 'B', 'E', 'A', 'E', 'B', 'E', 'D', 'D', 'E', 'A', 'E']
6801
2816

('S', 'BDDAEDEE', 'CCACCADC', 'ABDCDDBC', 'AABAABBE', 'BEDCDBEC')
['C', 'C', 'A', 'A', 'E', 'B', 'E', 'D', 'D', 'E', 'C', 'C', 'A', 'A', 'E', 'D', 'D', 'E', 'B', 'B', 'E', 'C']
5594
136