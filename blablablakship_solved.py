#!/bin/env python
import string
restrictions = [
 'qohrjzsvlxaah_dpjjwfgyobgclqtznrxdz',
 'mpuvuegnkurhvuhokmvrjixtxsepgtlsovf',
 'cmsxmkmkupkouowfngkhfbmhtrnci_gywgw',
 'svcsdplbejibpejuzqtuvqycvzmuuhbbfsy',
 'lgblcwitqkepxwkatx_a_craptrobpwvuus',
 'krdzoled_dcvqacyvoyimmjssqaahitezym',
 'dklwrxdigqvxfcidgbpxboeobjxensdq_fj',
 'thqcpupunc_uwmbkbtqcivwwngpyxfvilnu',
 'rwedvffwiwzyyvlwrpejkeki_etmwkrlhjr',
 'vlmhtqrfpopgnkuhevzdwt_mhvszmruzset',
 'ybtthrqlrhnnbstzyzfsqrikibolpczhntb',
 'js_mxhohcnljgtqrdunwaalyldbwcdiwakq',
 'puniwshqxvgcshssqygphsguu_uravkdkzg',
 'fxvebaa_tiukjjgxhisztdanqxwjkuanqxn',
 '__oyibuabyttzgnepfrgeptfaigfqxeacox',
 'otjjqiwcjmwliqoqwnokulhemhfgrwcmgb_',
 'gjiosykjftxiopajssmyzxzjzainjg_jval',
 'nyxnkgcpofq_rzelfwxepgsgflqbljskdrc',
 'aiygfozxsgmftipimcimsuqdcwkioyqfiie',
 'beaqnttodesdklyvueubrzpqkyzsfqxup_v',
 'zffblj_gzzowdyznalb_chnzyocxylhpemd',
 'uqwfzvjmabdrebfgidcnokulrfdv_mpgywp',
 'ink_acxymsjz_nv__rjvdndxjpj_snyothh',
 'xdga_mysvabmmxrmxhltxjbpdkhhvefxjqo',
 'wzzkgnvrhrhqldxbcahoyfvvwnyddoocmpi',
 'ecruedbzylfscfmclkdqnwc_euvkzbjtrck']
capital = [
 0, 6, 10, 15, 18, 22, 27, 32]

final = ""
for i in range (35):
    flag = string.lowercase + '_'
    for c in flag :
        found = 0;
        for r in restrictions:
            if c == r[i]:
                
                found = 1
                break
        if found == 0:
            final += c

flag = final
cap_flag = ''
for f in range(len(flag)):
    if f in capital:
        cap_flag += flag[f].upper()
    else:
        cap_flag += flag[f]

print 'Yeah, you got it !\nBlaCTF{' + cap_flag + '}\n'