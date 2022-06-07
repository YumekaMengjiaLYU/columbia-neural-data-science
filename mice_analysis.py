#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# special call that tells notebook to show matlplotlib figures inline
# get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt  # standard Python plotting library
import numpy as np  # fundamental package for scientific computing, handles arrays and math
# import the tdt library
import tdt
from tdt import read_block, read_sev, epoc_filter, download_demo_data

# In[ ]:


COHORT1_COCAINE_DAY1_330 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 1_1ms pulse master 8/PA FLX/Mouse 330/Cocaine day 1_mouse 330"

COHORT1_COCAINE_DAY3_330 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 1_1ms pulse master 8/PA FLX/Mouse 330/Cocaine day 3_mouse 330"

COHORT1_BLOCK_PATH3 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 1_1ms pulse master 8/PA FLX/Mouse 330/CPP Test 3_mouse 330"

COHORT1_SALINE_DAY1_330 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 1_1ms pulse master 8/PA FLX/Mouse 330/Saline day 1_mouse 330"

COHORT1_SALINE_DAY3_330 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 1_1ms pulse master 8/PA FLX/Mouse 330/Saline day 3_mouse 330"

COHORT1_COCAINE_DAY1_550 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 1_1ms pulse master 8/PA FLX/Mouse 550/Cocaine day 1_mouse 550"

COHORT1_COCAINE_DAY3_550 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 1_1ms pulse master 8/PA FLX/Mouse 550/Cocaine day 3_mouse 550"

COHORT1_BLOCK_PATH3 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 1_1ms pulse master 8/PA FLX/Mouse 550/CPP test 3_mouse 550_part1"

COHORT1_BLOCK_PATH4 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 1_1ms pulse master 8/PA FLX/Mouse 550/CPP test 3_mouse 550_part1"

COHORT1_SALINE_DAY1_550 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 1_1ms pulse master 8/PA FLX/Mouse 550/Saline day 1_mouse 550"

COHORT1_SALINE_DAY3_550 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 1_1ms pulse master 8/PA FLX/Mouse 550/Saline day 3_mouse 550"

COHORT1_COCAINE_DAY1_574 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 1_1ms pulse master 8/PA FLX/Mouse 574/Cocaine day 1_mouse 574"

COHORT1_COCAINE_DAY3_574 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 1_1ms pulse master 8/PA FLX/Mouse 574/Cocaine day 3_mouse 574"

COHORT1_SALINE_DAY1_574 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 1_1ms pulse master 8/PA FLX/Mouse 574/Saline day 1_mouse 574"

COHORT1_SALINE_DAY3_574 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 1_1ms pulse master 8/PA FLX/Mouse 574/Saline day 3_mouse 574"

COHORT1_COCAINE_DAY1_580 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 1_1ms pulse master 8/PA FLX/Mouse 580/Cocaine day 1_mouse 580"

COHORT1_COCAINE_DAY3_580 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 1_1ms pulse master 8/PA FLX/Mouse 580/Cocaine day 3_mouse 580"

COHORT1_SALINE_DAY1_580 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 1_1ms pulse master 8/PA FLX/Mouse 580/Saline day 1_mouse 580"

COHORT1_SALINE_DAY3_580 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 1_1ms pulse master 8/PA FLX/Mouse 580/Saline day 3_mouse 580"

COHORT1_COCAINE_DAY1_331 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 1_1ms pulse master 8/PA GBR/Mouse 331/Cocaine day 1_mouse 331"

COHORT1_COCAINE_DAY3_331 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 1_1ms pulse master 8/PA GBR/Mouse 331/Cocaine day 3_mouse 331"

COHORT1_SALINE_DAY1_331 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 1_1ms pulse master 8/PA GBR/Mouse 331/Saline day 1_mouse 331"

COHORT1_SALINE_DAY3_331 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 1_1ms pulse master 8/PA GBR/Mouse 331/Saline day 3_mouse 331"

COHORT1_COCAINE_DAY1_549 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 1_1ms pulse master 8/PA GBR/Mouse 549/Cocaine day 1_mouse 549"

COHORT1_COCAINE_DAY3_549 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 1_1ms pulse master 8/PA GBR/Mouse 549/Cocaine day 3_mouse 549"

COHORT1_SALINE_DAY1_549 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 1_1ms pulse master 8/PA GBR/Mouse 549/Saline day 1_mouse 549"

COHORT1_SALINE_DAY3_549 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 1_1ms pulse master 8/PA GBR/Mouse 549/Saline day 3_mouse 549"

COHORT1_COCAINE_DAY1_325 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 1_1ms pulse master 8/PA SAL/Mouse 325/Cocaine day 1_mouse 325"

COHORT1_COCAINE_DAY3_325 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 1_1ms pulse master 8/PA SAL/Mouse 325/Cocaine day 3_mouse 325"

COHORT1_SALINE_DAY1_325 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 1_1ms pulse master 8/PA SAL/Mouse 325/Saline day 1_mouse 325"

COHORT1_SALINE_DAY3_325 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 1_1ms pulse master 8/PA SAL/Mouse 325/Saline day 3_mouse 325"

COHORT1_COCAINE_DAY1_552 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 1_1ms pulse master 8/PA SAL/Mouse 552/Cocaine day 1_mouse 552"

COHORT1_COCAINE_DAY3_552 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 1_1ms pulse master 8/PA SAL/Mouse 552/Cocaine day 3_mouse 552"

COHORT1_SALINE_DAY1_552 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 1_1ms pulse master 8/PA SAL/Mouse 552/Saline day 1_mouse 552"

COHORT1_SALINE_DAY3_552 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 1_1ms pulse master 8/PA SAL/Mouse 552/Saline day 3_mouse 552"

# In[ ]:


# read_block is an all-in-one function for reading TDT data into Python. It needs only one input: the block path.
cohort1_cocaine_day1_330 = tdt.read_block(COHORT1_COCAINE_DAY1_330)
cohort1_cocaine_day3_330 = tdt.read_block(COHORT1_COCAINE_DAY3_330)
cohort1_saline_day1_330 = tdt.read_block(COHORT1_SALINE_DAY1_330)
cohort1_saline_day3_330 = tdt.read_block(COHORT1_SALINE_DAY3_330)
cohort1_cocaine_day1_550 = tdt.read_block(COHORT1_COCAINE_DAY1_550)
cohort1_cocaine_day3_550 = tdt.read_block(COHORT1_COCAINE_DAY3_550)
cohort1_saline_day1_550 = tdt.read_block(COHORT1_SALINE_DAY1_550)
cohort1_saline_day3_550 = tdt.read_block(COHORT1_SALINE_DAY1_550)
cohort1_cocaine_day1_574 = tdt.read_block(COHORT1_COCAINE_DAY1_574)
cohort1_cocaine_day3_574 = tdt.read_block(COHORT1_COCAINE_DAY3_574)
cohort1_saline_day1_574 = tdt.read_block(COHORT1_SALINE_DAY1_574)
cohort1_saline_day3_574 = tdt.read_block(COHORT1_SALINE_DAY3_574)
cohort1_cocaine_day1_580 = tdt.read_block(COHORT1_COCAINE_DAY1_580)
cohort1_cocaine_day3_580 = tdt.read_block(COHORT1_COCAINE_DAY3_580)
cohort1_saline_day1_580 = tdt.read_block(COHORT1_SALINE_DAY1_580)
cohort1_saline_day3_580 = tdt.read_block(COHORT1_SALINE_DAY3_580)

cohort1_cocaine_day1_331 = tdt.read_block(COHORT1_COCAINE_DAY1_331)
cohort1_cocaine_day3_331 = tdt.read_block(COHORT1_COCAINE_DAY3_331)
cohort1_saline_day1_331 = tdt.read_block(COHORT1_SALINE_DAY1_331)
cohort1_saline_day3_331 = tdt.read_block(COHORT1_SALINE_DAY3_331)

cohort1_cocaine_day1_549 = tdt.read_block(COHORT1_COCAINE_DAY1_549)
cohort1_cocaine_day3_549 = tdt.read_block(COHORT1_COCAINE_DAY3_549)
cohort1_saline_day1_549 = tdt.read_block(COHORT1_SALINE_DAY1_549)
cohort1_saline_day3_549 = tdt.read_block(COHORT1_SALINE_DAY3_549)

cohort1_cocaine_day1_325 = tdt.read_block(COHORT1_COCAINE_DAY1_325)
cohort1_cocaine_day3_325 = tdt.read_block(COHORT1_COCAINE_DAY3_325)
cohort1_saline_day1_325 = tdt.read_block(COHORT1_SALINE_DAY1_325)
cohort1_saline_day3_325 = tdt.read_block(COHORT1_SALINE_DAY3_325)

cohort1_cocaine_day1_552 = tdt.read_block(COHORT1_COCAINE_DAY1_552)
cohort1_cocaine_day3_552 = tdt.read_block(COHORT1_COCAINE_DAY3_552)
cohort1_saline_day1_552 = tdt.read_block(COHORT1_SALINE_DAY1_552)
cohort1_saline_day3_552 = tdt.read_block(COHORT1_SALINE_DAY3_552)

# In[ ]:


# In[ ]:


COHORT2_BLOCK_PATH1 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Cocaine Days/Baseline Cocaine Day 1_616"
COHORT2_BLOCK_PATH2 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Saline Days/Baseline Saline Day 1_616"

COHORT2_BLOCK_PATH3 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Cocaine Days/Baseline Cocaine Day 1_620"
COHORT2_BLOCK_PATH4 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Saline Days/Baseline Saline Day 1_620"

COHORT2_BLOCK_PATH5 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Cocaine Days/Baseline Cocaine Day 1_621"
COHORT2_BLOCK_PATH6 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Saline Days/Baseline Saline Day 1_621"

COHORT2_BLOCK_PATH7 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Cocaine Days/Baseline Cocaine Day 1_628"
COHORT2_BLOCK_PATH8 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Saline Days/Baseline Saline Day 1_628"

COHORT2_BLOCK_PATH9 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Cocaine Days/Baseline Cocaine Day 1_638"
COHORT2_BLOCK_PATH10 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Saline Days/Baseline Saline Day 1_638"

COHORT2_BLOCK_PATH11 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Cocaine Days/Baseline Cocaine Day 1_641"
COHORT2_BLOCK_PATH12 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Saline Days/Baseline Saline Day 1_641"

COHORT2_BLOCK_PATH13 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Cocaine Days/Baseline Cocaine Day 1_642"
COHORT2_BLOCK_PATH14 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Saline Days/Baseline Saline Day 1_642"

COHORT2_BLOCK_PATH15 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Cocaine Days/Baseline Cocaine Day 1_657"
COHORT2_BLOCK_PATH16 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Saline Days/Baseline Saline Day 1_657"

COHORT2_BLOCK_PATH17 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Cocaine Days/Baseline Cocaine Day 1_660"
COHORT2_BLOCK_PATH18 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Saline Days/Baseline Saline Day 1_660"

COHORT2_BLOCK_PATH19 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Cocaine Days/Baseline Cocaine Day 1_674"
COHORT2_BLOCK_PATH20 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Saline Days/Baseline Saline Day 1_674"

COHORT2_BLOCK_PATH21 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Cocaine Days/Baseline Cocaine Day 1_675"
COHORT2_BLOCK_PATH22 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Saline Days/Baseline Saline Day 1_675"

# store the path for all the tank folder
# take 7 new data tank folders as examples
COHORT2_BLOCK_PATH23 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Cocaine Days/Baseline Cocaine Day 3_616"
COHORT2_BLOCK_PATH24 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Saline Days/Baseline Saline Day 3_616"

COHORT2_BLOCK_PATH25 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Cocaine Days/Baseline Cocaine Day 3_620"
COHORT2_BLOCK_PATH26 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Saline Days/Baseline Saline Day 3_620"

COHORT2_BLOCK_PATH27 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Cocaine Days/Baseline Cocaine Day 3_621"
COHORT2_BLOCK_PATH28 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Saline Days/Baseline Saline Day 3_621"

COHORT2_BLOCK_PATH29 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Cocaine Days/Baseline Cocaine Day 3_628"
COHORT2_BLOCK_PATH30 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Saline Days/Baseline Saline Day 3_628"

COHORT2_BLOCK_PATH31 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Cocaine Days/Baseline Cocaine Day 3_638"
COHORT2_BLOCK_PATH32 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Saline Days/Baseline Saline Day 3_638"

COHORT2_BLOCK_PATH33 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Cocaine Days/Baseline Cocaine Day 3_641"
COHORT2_BLOCK_PATH34 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Saline Days/Baseline Saline Day 3_641"

COHORT2_BLOCK_PATH35 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Cocaine Days/Baseline Cocaine Day 3_642"
COHORT2_BLOCK_PATH36 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Saline Days/Baseline Saline Day 3_642"

COHORT2_BLOCK_PATH37 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Cocaine Days/Baseline Cocaine Day 3_657"
COHORT2_BLOCK_PATH38 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Saline Days/Baseline Saline Day 3_657"

COHORT2_BLOCK_PATH39 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Cocaine Days/Baseline Cocaine Day 3_660"
COHORT2_BLOCK_PATH40 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Saline Days/Baseline Saline Day 3_660"

COHORT2_BLOCK_PATH41 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Cocaine Days/Baseline Cocaine Day 3_674"
COHORT2_BLOCK_PATH42 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Saline Days/Baseline Saline Day 3_674"

COHORT2_BLOCK_PATH43 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Cocaine Days/Baseline Cocaine Day 3_675"
COHORT2_BLOCK_PATH44 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Saline Days/Baseline Saline Day 3_675"

COHORT2_COCAINE_DAY1_616 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Cocaine Days/Cocaine Day 1_616"
COHORT2_COCAINE_DAY1_620 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Cocaine Days/Cocaine Day 1_620"
COHORT2_COCAINE_DAY1_621 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Cocaine Days/Cocaine Day 1_621"
COHORT2_COCAINE_DAY1_628 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Cocaine Days/Cocaine Day 1_628"
COHORT2_COCAINE_DAY1_638 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Cocaine Days/Cocaine Day 1_638"
COHORT2_COCAINE_DAY1_641 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Cocaine Days/Cocaine Day 1_641"
COHORT2_COCAINE_DAY1_642 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Cocaine Days/Cocaine Day 1_642"
COHORT2_COCAINE_DAY1_657 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Cocaine Days/Cocaine Day 1_657"
COHORT2_COCAINE_DAY1_660 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Cocaine Days/Cocaine Day 1_660"
COHORT2_COCAINE_DAY1_674 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Cocaine Days/Cocaine Day 1_674"
COHORT2_COCAINE_DAY1_675 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Cocaine Days/Cocaine Day 1_675"
COHORT2_SALINE_DAY1_616 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Saline Days/Saline Day 1_616"
COHORT2_SALINE_DAY1_620 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Saline Days/Saline Day 1_620"
COHORT2_SALINE_DAY1_621 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Saline Days/Saline Day 1_621"
COHORT2_SALINE_DAY1_628 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Saline Days/Saline Day 1_628"
COHORT2_SALINE_DAY1_638 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Saline Days/Saline Day 1_638"
COHORT2_SALINE_DAY1_641 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Saline Days/Saline Day 1_641"
COHORT2_SALINE_DAY1_642 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Saline Days/Saline Day 1_642"
COHORT2_SALINE_DAY1_657 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Saline Days/Saline Day 1_657"
COHORT2_SALINE_DAY1_660 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Saline Days/Saline Day 1_660"
COHORT2_SALINE_DAY1_674 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Saline Days/Saline Day 1_674"
COHORT2_SALINE_DAY1_675 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Saline Days/Saline Day 1_675"

COHORT2_COCAINE_DAY3_616 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Cocaine Days/Cocaine Day 3_616"
COHORT2_COCAINE_DAY3_620 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Cocaine Days/Cocaine Day 3_620"
COHORT2_COCAINE_DAY3_621 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Cocaine Days/Cocaine Day 3_621"
COHORT2_COCAINE_DAY3_628 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Cocaine Days/Cocaine Day 3_628"
COHORT2_COCAINE_DAY3_638 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Cocaine Days/Cocaine Day 3_638"
COHORT2_COCAINE_DAY3_641 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Cocaine Days/Cocaine Day 3_641"
COHORT2_COCAINE_DAY3_642 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Cocaine Days/Cocaine Day 3_642"
COHORT2_COCAINE_DAY3_657 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Cocaine Days/Cocaine Day 3_657"
COHORT2_COCAINE_DAY3_660 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Cocaine Days/Cocaine Day 3_660"
COHORT2_COCAINE_DAY3_674 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Cocaine Days/Cocaine Day 3_674"
COHORT2_COCAINE_DAY3_675 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Cocaine Days/Cocaine Day 3_675"
COHORT2_SALINE_DAY3_616 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Saline Days/Saline Day 3_616"
COHORT2_SALINE_DAY3_620 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Saline Days/Saline Day 3_620"
COHORT2_SALINE_DAY3_621 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Saline Days/Saline Day 3_621"
COHORT2_SALINE_DAY3_628 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Saline Days/Saline Day 3_628"
COHORT2_SALINE_DAY3_638 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Saline Days/Saline Day 3_638"
COHORT2_SALINE_DAY3_641 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Saline Days/Saline Day 3_641"
COHORT2_SALINE_DAY3_642 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Saline Days/Saline Day 3_642"
COHORT2_SALINE_DAY3_657 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Saline Days/Saline Day 3_657"
COHORT2_SALINE_DAY3_660 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Saline Days/Saline Day 3_660"
COHORT2_SALINE_DAY3_674 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Saline Days/Saline Day 3_674"
COHORT2_SALINE_DAY3_675 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Saline Days/Saline Day 3_675"

# In[ ]:


# store the path for all the tank folder
# take 7 new data tank folders as examples
COHORT3_BLOCK_PATH1 = "Cocaine Day 1_Cage 5 and 6/Baseline Cocaine Day 1_3321_cage5"
COHORT3_BLOCK_PATH2 = "Cocaine Day 1_Cage 5 and 6/Baseline Cocaine Day 1_3336_cage6"

COHORT3_BLOCK_PATH3 = "Cocaine Day 1_Cage 5 and 6/Baseline Cocaine Day 1_3337_cage6"
COHORT3_BLOCK_PATH4 = "Cocaine Day 1_Cage 5 and 6/Cocaine Day 1_3321_cage5"
COHORT3_BLOCK_PATH5 = "Cocaine Day 1_Cage 5 and 6/Cocaine Day 1_3336_cage6"
COHORT3_BLOCK_PATH6 = "Cocaine Day 1_Cage 5 and 6/Cocaine Day 1_3337_cage6"

COHORT3_BLOCK_PATH7 = "Cocaine Day 1_Cage 7/Baseline Cocaine Day 1_3341_cage7"
COHORT3_BLOCK_PATH8 = "Cocaine Day 1_Cage 7/Baseline Cocaine Day 1_3346_cage7"
COHORT3_BLOCK_PATH9 = "Cocaine Day 1_Cage 7/Cocaine Day 1_3341_cage7"
COHORT3_BLOCK_PATH10 = "Cocaine Day 1_Cage 7/Cocaine Day 1_3346_cage7"

COHORT3_BLOCK_PATH11 = "Cocaine Day 3_cage 5 and 6/Baseline Cocaine Day 3_3321_cage 5"
COHORT3_BLOCK_PATH12 = "Cocaine Day 3_cage 5 and 6/Baseline Cocaine Day 3_3336_cage6"

COHORT3_BLOCK_PATH13 = "Cocaine Day 3_cage 5 and 6/Baseline Cocaine Day 3_3337_cage6"
COHORT3_BLOCK_PATH14 = "Cocaine Day 3_cage 5 and 6/Cocaine Day 3_3321_cage5"
COHORT3_BLOCK_PATH15 = "Cocaine Day 3_cage 5 and 6/Cocaine Day 3_3336_cage6"
COHORT3_BLOCK_PATH16 = "Cocaine Day 3_cage 5 and 6/Cocaine Day 3_3337_cage6"

COHORT3_BLOCK_PATH17 = "Cocaine Day 3_cage 7/Baseline Cocaine Day 3_3341_cage7"
COHORT3_BLOCK_PATH18 = "Cocaine Day 3_cage 7/Baseline Cocaine Day 3_3346_cage7"
COHORT3_BLOCK_PATH19 = "Cocaine Day 3_cage 7/Cocaine Day 3_3341_cage7"
COHORT3_BLOCK_PATH20 = "Cocaine Day 3_cage 7/Cocaine Day 3_3346_cage7"

COHORT3_BLOCK_PATH21 = "Saline Day 1_Cage 5 and 6/Baseline Saline Day 1_3321_cage5"
COHORT3_BLOCK_PATH22 = "Saline Day 1_Cage 5 and 6/Baseline Saline Day 1_3336_cage6"

COHORT3_BLOCK_PATH23 = "Saline Day 1_Cage 5 and 6/Baseline Saline Day 1_3337_cage6"
COHORT3_BLOCK_PATH24 = "Saline Day 1_Cage 5 and 6/Saline Day 1_3321_cage5"
COHORT3_BLOCK_PATH25 = "Saline Day 1_Cage 5 and 6/Saline Day 1_3336_cage6"
COHORT3_BLOCK_PATH26 = "Saline Day 1_Cage 5 and 6/Saline Day 1_3337_cage6"

COHORT3_BLOCK_PATH27 = "Saline Day 1_Cage 7/Baseline Saline Day 1_3341_cage7"
COHORT3_BLOCK_PATH28 = "Saline Day 1_Cage 7/Baseline Saline Day 1_3346_cage7"
COHORT3_BLOCK_PATH29 = "Saline Day 1_Cage 7/Saline Day 1_3341_cage7"
COHORT3_BLOCK_PATH30 = "Saline Day 1_Cage 7/Saline Day 1_3346_cage7"

COHORT3_BLOCK_PATH31 = "Saline Day 3_cage 5 and 6/Baseline Saline Day 3_3321_cage5"
COHORT3_BLOCK_PATH32 = "Saline Day 3_cage 5 and 6/Baseline Saline Day 3_3336_cage6"

COHORT3_BLOCK_PATH33 = "Saline Day 3_cage 5 and 6/Baseline Saline Day 3_3337_cage6"
COHORT3_BLOCK_PATH34 = "Saline Day 3_cage 5 and 6/Saline Day 3_3321_cage5"
COHORT3_BLOCK_PATH35 = "Saline Day 3_cage 5 and 6/Saline Day 3_3336_cage6"
COHORT3_BLOCK_PATH36 = "Saline Day 3_cage 5 and 6/Saline Day 3_3337_cage6"

COHORT3_BLOCK_PATH37 = "Saline Day 3_cage 7/Baseline Saline Day 3_3341_cage7"
COHORT3_BLOCK_PATH38 = "Saline Day 3_cage 7/Baseline Saline Day 3_3346_cage7"
COHORT3_BLOCK_PATH39 = "Saline Day 3_cage 7/Saline Day 3_3341_cage7"
COHORT3_BLOCK_PATH40 = "Saline Day 3_cage 7/Saline Day 3_3346_cage7"

# In[ ]:


# In[ ]:


# In[ ]:


cohort3_data1 = tdt.read_block(COHORT3_BLOCK_PATH1)
cohort3_data2 = tdt.read_block(COHORT3_BLOCK_PATH2)
cohort3_data3 = tdt.read_block(COHORT3_BLOCK_PATH3)
cohort3_data4 = tdt.read_block(COHORT3_BLOCK_PATH4)
cohort3_data5 = tdt.read_block(COHORT3_BLOCK_PATH5)
cohort3_data6 = tdt.read_block(COHORT3_BLOCK_PATH6)
cohort3_data7 = tdt.read_block(COHORT3_BLOCK_PATH7)
cohort3_data8 = tdt.read_block(COHORT3_BLOCK_PATH8)
cohort3_data9 = tdt.read_block(COHORT3_BLOCK_PATH9)
cohort3_data10 = tdt.read_block(COHORT3_BLOCK_PATH10)
cohort3_data11 = tdt.read_block(COHORT3_BLOCK_PATH11)
cohort3_data12 = tdt.read_block(COHORT3_BLOCK_PATH12)
cohort3_data13 = tdt.read_block(COHORT3_BLOCK_PATH13)
cohort3_data14 = tdt.read_block(COHORT3_BLOCK_PATH14)
cohort3_data15 = tdt.read_block(COHORT3_BLOCK_PATH15)
cohort3_data16 = tdt.read_block(COHORT3_BLOCK_PATH16)
cohort3_data17 = tdt.read_block(COHORT3_BLOCK_PATH17)
cohort3_data18 = tdt.read_block(COHORT3_BLOCK_PATH18)
cohort3_data19 = tdt.read_block(COHORT3_BLOCK_PATH19)
cohort3_data20 = tdt.read_block(COHORT3_BLOCK_PATH20)
cohort3_data21 = tdt.read_block(COHORT3_BLOCK_PATH21)
cohort3_data22 = tdt.read_block(COHORT3_BLOCK_PATH22)
cohort3_data23 = tdt.read_block(COHORT3_BLOCK_PATH23)
cohort3_data24 = tdt.read_block(COHORT3_BLOCK_PATH24)
cohort3_data25 = tdt.read_block(COHORT3_BLOCK_PATH25)
cohort3_data26 = tdt.read_block(COHORT3_BLOCK_PATH26)
cohort3_data27 = tdt.read_block(COHORT3_BLOCK_PATH27)
cohort3_data28 = tdt.read_block(COHORT3_BLOCK_PATH28)
cohort3_data29 = tdt.read_block(COHORT3_BLOCK_PATH29)
cohort3_data30 = tdt.read_block(COHORT3_BLOCK_PATH30)
cohort3_data31 = tdt.read_block(COHORT3_BLOCK_PATH31)
cohort3_data32 = tdt.read_block(COHORT3_BLOCK_PATH32)
cohort3_data33 = tdt.read_block(COHORT3_BLOCK_PATH33)
cohort3_data34 = tdt.read_block(COHORT3_BLOCK_PATH34)
cohort3_data35 = tdt.read_block(COHORT3_BLOCK_PATH35)
cohort3_data36 = tdt.read_block(COHORT3_BLOCK_PATH36)
cohort3_data37 = tdt.read_block(COHORT3_BLOCK_PATH37)
cohort3_data38 = tdt.read_block(COHORT3_BLOCK_PATH38)
cohort3_data39 = tdt.read_block(COHORT3_BLOCK_PATH39)
cohort3_data40 = tdt.read_block(COHORT3_BLOCK_PATH40)

# In[ ]:


# In[ ]:


from scipy import stats

num_samples_470A_coc = len(cohort3_data1.streams._470A.data)
num_samples_405A_coc = len(cohort3_data1.streams._405A.data)
_470A_time_coc = np.linspace(1, num_samples_470A_coc, num_samples_470A_coc) / cohort3_data1.streams._470A.fs

t_coc = int(120 * cohort3_data1.streams._470A.fs)  # int rounds it to the nearest integer

# print(t1==t3)

num_samples_470A_sal = len(cohort3_data2.streams._470A.data)
num_samples_405A_sal = len(cohort3_data2.streams._405A.data)
_470A_time_sal = np.linspace(1, num_samples_470A_sal, num_samples_470A_sal) / cohort3_data2.streams._470A.fs
# _470B_time = np.linspace(1, num_samples, num_samples) / data2.streams._470B.fs

_405A_time_sal = np.linspace(1, num_samples_405A_sal, num_samples_405A_sal) / cohort3_data2.streams._405A.fs

t_sal = int(120 * cohort3_data2.streams._470A.fs)  # int rounds it to the nearest integer

# In[ ]:


# In[ ]:


# In[ ]:


# In[ ]:


# In[ ]:


# x1 = np.array(cohort1_cocaine_day1_330.streams._405A.data[0:8*t_coc])
# y1 = np.array(cohort1_cocaine_day1_330.streams._470A.data[0:8*t_coc])
# bls = np.flip(np.polynomial.chebyshev.chebfit(x1, y1, 1))
# fit_line = np.multiply(bls[0],x1)+bls[1]
# x_330__cocaine_day1_20min = np.array(stats.zscore((np.array(y1-fit_line)/np.array(fit_line))))


x1 = np.array(cohort1_cocaine_day1_330.streams._405A.data[0:2 * t_coc])
y1 = np.array(cohort1_cocaine_day1_330.streams._470A.data[0:2 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_330_cocaine_day1_20min_1 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort1_cocaine_day1_330.streams._405A.data[2 * t_coc + 1:4 * t_coc])
y1 = np.array(cohort1_cocaine_day1_330.streams._470A.data[2 * t_coc + 1:4 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_330_cocaine_day1_20min_3 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort1_cocaine_day1_330.streams._405A.data[4 * t_coc + 1:6 * t_coc])
y1 = np.array(cohort1_cocaine_day1_330.streams._470A.data[4 * t_coc + 1:6 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_330_cocaine_day1_20min_5 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort1_cocaine_day1_330.streams._405A.data[6 * t_coc + 1:8 * t_coc])
y1 = np.array(cohort1_cocaine_day1_330.streams._470A.data[6 * t_coc + 1:8 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_330_cocaine_day1_20min_7 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x_330_cocaine_day1_20min = np.concatenate((x_330_cocaine_day1_20min_1,
                                           x_330_cocaine_day1_20min_3,
                                           x_330_cocaine_day1_20min_5,
                                           x_330_cocaine_day1_20min_7), axis=0)

# x1 = np.array(cohort1_cocaine_day3_330.streams._405A.data[0:8*t_coc])
# y1 = np.array(cohort1_cocaine_day3_330.streams._470A.data[0:8*t_coc])
# bls = np.flip(np.polynomial.chebyshev.chebfit(x1, y1, 1))
# fit_line = np.multiply(bls[0],x1)+bls[1]
# x_330__cocaine_day3_20min = np.array(stats.zscore((np.array(y1-fit_line)/np.array(fit_line))))


x1 = np.array(cohort1_cocaine_day3_330.streams._405A.data[0:2 * t_coc])
y1 = np.array(cohort1_cocaine_day3_330.streams._470A.data[0:2 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_330_cocaine_day3_20min_1 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort1_cocaine_day3_330.streams._405A.data[2 * t_coc + 1:4 * t_coc])
y1 = np.array(cohort1_cocaine_day3_330.streams._470A.data[2 * t_coc + 1:4 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_330_cocaine_day3_20min_3 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort1_cocaine_day3_330.streams._405A.data[4 * t_coc + 1:6 * t_coc])
y1 = np.array(cohort1_cocaine_day3_330.streams._470A.data[4 * t_coc + 1:6 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_330_cocaine_day3_20min_5 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort1_cocaine_day3_330.streams._405A.data[6 * t_coc + 1:8 * t_coc])
y1 = np.array(cohort1_cocaine_day3_330.streams._470A.data[6 * t_coc + 1:8 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_330_cocaine_day3_20min_7 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x_330_cocaine_day3_20min = np.concatenate((x_330_cocaine_day3_20min_1,
                                           x_330_cocaine_day3_20min_3,
                                           x_330_cocaine_day3_20min_5,
                                           x_330_cocaine_day3_20min_7), axis=0)

# x1 = np.array(cohort1_saline_day1_330.streams._405A.data[0:8*t_coc])
# y1 = np.array(cohort1_saline_day1_330.streams._470A.data[0:8*t_coc])
# bls = np.flip(np.polynomial.chebyshev.chebfit(x1, y1, 1))
# fit_line = np.multiply(bls[0],x1)+bls[1]
# x_330__saline_day1_20min = np.array(stats.zscore((np.array(y1-fit_line)/np.array(fit_line))))


x1 = np.array(cohort1_saline_day1_330.streams._405A.data[0:2 * t_coc])
y1 = np.array(cohort1_saline_day1_330.streams._470A.data[0:2 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_330_saline_day1_20min_1 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort1_saline_day1_330.streams._405A.data[2 * t_coc + 1:4 * t_coc])
y1 = np.array(cohort1_saline_day1_330.streams._470A.data[2 * t_coc + 1:4 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_330_saline_day1_20min_3 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort1_saline_day1_330.streams._405A.data[4 * t_coc + 1:6 * t_coc])
y1 = np.array(cohort1_saline_day1_330.streams._470A.data[4 * t_coc + 1:6 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_330_saline_day1_20min_5 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort1_saline_day1_330.streams._405A.data[6 * t_coc + 1:8 * t_coc])
y1 = np.array(cohort1_saline_day1_330.streams._470A.data[6 * t_coc + 1:8 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_330_saline_day1_20min_7 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x_330_saline_day1_20min = np.concatenate((x_330_saline_day1_20min_1,
                                          x_330_saline_day1_20min_3,
                                          x_330_saline_day1_20min_5,
                                          x_330_saline_day1_20min_7), axis=0)

# x1 = np.array(cohort1_saline_day3_330.streams._405A.data[0:8*t_coc])
# y1 = np.array(cohort1_saline_day3_330.streams._470A.data[0:8*t_coc])
# bls = np.flip(np.polynomial.chebyshev.chebfit(x1, y1, 1))
# fit_line = np.multiply(bls[0],x1)+bls[1]
# x_330__saline_day3_20min = np.array(stats.zscore((np.array(y1-fit_line)/np.array(fit_line))))

x1 = np.array(cohort1_saline_day3_330.streams._405A.data[0:2 * t_coc])
y1 = np.array(cohort1_saline_day3_330.streams._470A.data[0:2 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_330_saline_day3_20min_1 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort1_saline_day3_330.streams._405A.data[2 * t_coc + 1:4 * t_coc])
y1 = np.array(cohort1_saline_day3_330.streams._470A.data[2 * t_coc + 1:4 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_330_saline_day3_20min_3 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort1_saline_day3_330.streams._405A.data[4 * t_coc + 1:6 * t_coc])
y1 = np.array(cohort1_saline_day3_330.streams._470A.data[4 * t_coc + 1:6 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_330_saline_day3_20min_5 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort1_saline_day3_330.streams._405A.data[6 * t_coc + 1:8 * t_coc])
y1 = np.array(cohort1_saline_day3_330.streams._470A.data[6 * t_coc + 1:8 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_330_saline_day3_20min_7 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x_330_saline_day3_20min = np.concatenate((x_330_saline_day3_20min_1,
                                          x_330_saline_day3_20min_3,
                                          x_330_saline_day3_20min_5,
                                          x_330_saline_day3_20min_7), axis=0)

# x1 = np.array(cohort1_cocaine_day1_331.streams._405A.data[0:8*t_coc])
# y1 = np.array(cohort1_cocaine_day1_331.streams._470A.data[0:8*t_coc])
# bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
# fit_line = np.multiply(bls[0],x1)+bls[1]
# x_331__cocaine_day1_20min = np.array(stats.zscore((np.array(y1-fit_line)/np.array(fit_line))))


x1 = np.array(cohort1_cocaine_day1_331.streams._405A.data[0:2 * t_coc])
y1 = np.array(cohort1_cocaine_day1_331.streams._470A.data[0:2 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_331_cocaine_day1_20min_1 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort1_cocaine_day1_331.streams._405A.data[2 * t_coc + 1:4 * t_coc])
y1 = np.array(cohort1_cocaine_day1_331.streams._470A.data[2 * t_coc + 1:4 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_331_cocaine_day1_20min_3 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort1_cocaine_day1_331.streams._405A.data[4 * t_coc + 1:6 * t_coc])
y1 = np.array(cohort1_cocaine_day1_331.streams._470A.data[4 * t_coc + 1:6 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_331_cocaine_day1_20min_5 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort1_cocaine_day1_331.streams._405A.data[6 * t_coc + 1:8 * t_coc])
y1 = np.array(cohort1_cocaine_day1_331.streams._470A.data[6 * t_coc + 1:8 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_331_cocaine_day1_20min_7 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x_331_cocaine_day1_20min = np.concatenate((x_331_cocaine_day1_20min_1,
                                           x_331_cocaine_day1_20min_3,
                                           x_331_cocaine_day1_20min_5,
                                           x_331_cocaine_day1_20min_7), axis=0)

x1 = np.array(cohort1_cocaine_day3_331.streams._405A.data[0:2 * t_coc])
y1 = np.array(cohort1_cocaine_day3_331.streams._470A.data[0:2 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_331_saline_day3_20min_1 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort1_saline_day3_331.streams._405A.data[2 * t_coc + 1:4 * t_coc])
y1 = np.array(cohort1_saline_day3_331.streams._470A.data[2 * t_coc + 1:4 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_331_saline_day3_20min_3 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort1_saline_day3_331.streams._405A.data[4 * t_coc + 1:6 * t_coc])
y1 = np.array(cohort1_saline_day3_331.streams._470A.data[4 * t_coc + 1:6 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_331_saline_day3_20min_5 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort1_saline_day3_331.streams._405A.data[6 * t_coc + 1:8 * t_coc])
y1 = np.array(cohort1_saline_day3_331.streams._470A.data[6 * t_coc + 1:8 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_331_saline_day3_20min_7 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x_331_saline_day3_20min = np.concatenate((x_331_saline_day3_20min_1,
                                          x_331_saline_day3_20min_3,
                                          x_331_saline_day3_20min_5,
                                          x_331_saline_day3_20min_7), axis=0)

# x1 = np.array(cohort1_cocaine_day3_331.streams._405A.data[0:8*t_coc])
# y1 = np.array(cohort1_cocaine_day3_331.streams._470A.data[0:8*t_coc])
# bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
# fit_line = np.multiply(bls[0],x1)+bls[1]
# x_331__cocaine_day3_20min = np.array(stats.zscore((np.array(y1-fit_line)/np.array(fit_line))))
x1 = np.array(cohort1_cocaine_day3_331.streams._405A.data[0:2 * t_coc])
y1 = np.array(cohort1_cocaine_day3_331.streams._470A.data[0:2 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_331_cocaine_day3_20min_1 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort1_cocaine_day3_331.streams._405A.data[2 * t_coc + 1:4 * t_coc])
y1 = np.array(cohort1_cocaine_day3_331.streams._470A.data[2 * t_coc + 1:4 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_331_cocaine_day3_20min_3 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort1_cocaine_day3_331.streams._405A.data[4 * t_coc + 1:6 * t_coc])
y1 = np.array(cohort1_cocaine_day3_331.streams._470A.data[4 * t_coc + 1:6 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_331_cocaine_day3_20min_5 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort1_cocaine_day3_331.streams._405A.data[6 * t_coc + 1:8 * t_coc])
y1 = np.array(cohort1_cocaine_day3_331.streams._470A.data[6 * t_coc + 1:8 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_331_cocaine_day3_20min_7 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x_331_cocaine_day3_20min = np.concatenate((x_331_cocaine_day3_20min_1,
                                           x_331_cocaine_day3_20min_3,
                                           x_331_cocaine_day3_20min_5,
                                           x_331_cocaine_day3_20min_7), axis=0)

# x1 = np.array(cohort1_saline_day1_331.streams._405A.data[0:8*t_coc])
# y1 = np.array(cohort1_saline_day1_331.streams._470A.data[0:8*t_coc])
# bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
# fit_line = np.multiply(bls[0],x1)+bls[1]
# x_331__saline_day1_20min = np.array(stats.zscore((np.array(y1-fit_line)/np.array(fit_line))))

x1 = np.array(cohort1_cocaine_day1_331.streams._405A.data[0:2 * t_coc])
y1 = np.array(cohort1_cocaine_day1_331.streams._470A.data[0:2 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_331_saline_day1_20min_1 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort1_saline_day1_331.streams._405A.data[2 * t_coc + 1:4 * t_coc])
y1 = np.array(cohort1_saline_day1_331.streams._470A.data[2 * t_coc + 1:4 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_331_saline_day1_20min_3 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort1_saline_day1_331.streams._405A.data[4 * t_coc + 1:6 * t_coc])
y1 = np.array(cohort1_saline_day1_331.streams._470A.data[4 * t_coc + 1:6 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_331_saline_day1_20min_5 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort1_saline_day1_331.streams._405A.data[6 * t_coc + 1:8 * t_coc])
y1 = np.array(cohort1_saline_day1_331.streams._470A.data[6 * t_coc + 1:8 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_331_saline_day1_20min_7 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x_331_saline_day1_20min = np.concatenate((x_331_saline_day1_20min_1,
                                          x_331_saline_day1_20min_3,
                                          x_331_saline_day1_20min_5,
                                          x_331_saline_day1_20min_7), axis=0)

# x1 = np.array(cohort1_cocaine_day1_550.streams._405A.data[0:8*t_coc])
# y1 = np.array(cohort1_cocaine_day1_550.streams._470A.data[0:8*t_coc])
# bls = np.flip(np.polynomial.chebyshev.chebfit(x1, y1, 1))
# fit_line = np.multiply(bls[0],x1)+bls[1]
# x_550__cocaine_day1_20min = np.array(stats.zscore((np.array(y1-fit_line)/np.array(fit_line))))

x1 = np.array(cohort1_cocaine_day1_550.streams._405A.data[0:2 * t_coc])
y1 = np.array(cohort1_cocaine_day1_550.streams._470A.data[0:2 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_550_cocaine_day1_20min_1 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort1_cocaine_day1_550.streams._405A.data[2 * t_coc + 1:4 * t_coc])
y1 = np.array(cohort1_cocaine_day1_550.streams._470A.data[2 * t_coc + 1:4 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_550_cocaine_day1_20min_3 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort1_cocaine_day1_550.streams._405A.data[4 * t_coc + 1:6 * t_coc])
y1 = np.array(cohort1_cocaine_day1_550.streams._470A.data[4 * t_coc + 1:6 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_550_cocaine_day1_20min_5 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort1_cocaine_day1_550.streams._405A.data[6 * t_coc + 1:8 * t_coc])
y1 = np.array(cohort1_cocaine_day1_550.streams._470A.data[6 * t_coc + 1:8 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_550_cocaine_day1_20min_7 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x_550_cocaine_day1_20min = np.concatenate((x_550_cocaine_day1_20min_1,
                                           x_550_cocaine_day1_20min_3,
                                           x_550_cocaine_day1_20min_5,
                                           x_550_cocaine_day1_20min_7), axis=0)

# x1 = np.array(cohort1_cocaine_day3_550.streams._405A.data[0:8*t_coc])
# y1 = np.array(cohort1_cocaine_day3_550.streams._470A.data[0:8*t_coc])
# bls = np.flip(np.polynomial.chebyshev.chebfit(x1, y1, 1))
# fit_line = np.multiply(bls[0],x1)+bls[1]
# x_550__cocaine_day3_20min = np.array(stats.zscore((np.array(y1-fit_line)/np.array(fit_line))))

x1 = np.array(cohort1_cocaine_day3_550.streams._405A.data[0:2 * t_coc])
y1 = np.array(cohort1_cocaine_day3_550.streams._470A.data[0:2 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_550_cocaine_day3_20min_1 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort1_cocaine_day3_550.streams._405A.data[2 * t_coc + 1:4 * t_coc])
y1 = np.array(cohort1_cocaine_day3_550.streams._470A.data[2 * t_coc + 1:4 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_550_cocaine_day3_20min_3 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort1_cocaine_day3_550.streams._405A.data[4 * t_coc + 1:6 * t_coc])
y1 = np.array(cohort1_cocaine_day3_550.streams._470A.data[4 * t_coc + 1:6 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_550_cocaine_day3_20min_5 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort1_cocaine_day3_550.streams._405A.data[6 * t_coc + 1:8 * t_coc])
y1 = np.array(cohort1_cocaine_day3_550.streams._470A.data[6 * t_coc + 1:8 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_550_cocaine_day3_20min_7 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x_550_cocaine_day3_20min = np.concatenate((x_550_cocaine_day3_20min_1,
                                           x_550_cocaine_day3_20min_3,
                                           x_550_cocaine_day3_20min_5,
                                           x_550_cocaine_day3_20min_7), axis=0)

# x1 = np.array(cohort1_saline_day1_550.streams._405A.data[0:8*t_coc])
# y1 = np.array(cohort1_saline_day1_550.streams._470A.data[0:8*t_coc])
# bls = np.flip(np.polynomial.chebyshev.chebfit(x1, y1, 1))
# fit_line = np.multiply(bls[0],x1)+bls[1]
# x_550__saline_day1_20min = np.array(stats.zscore((np.array(y1-fit_line)/np.array(fit_line))))

# x1 = np.array(cohort1_saline_day3_550.streams._405A.data[0:8*t_coc])
# y1 = np.array(cohort1_saline_day3_550.streams._470A.data[0:8*t_coc])
# bls = np.flip(np.polynomial.chebyshev.chebfit(x1, y1, 1))
# fit_line = np.multiply(bls[0],x1)+bls[1]
# x_550__saline_day3_20min = np.array(stats.zscore((np.array(y1-fit_line)/np.array(fit_line))))


x1 = np.array(cohort1_saline_day1_550.streams._405A.data[0:2 * t_coc])
y1 = np.array(cohort1_saline_day1_550.streams._470A.data[0:2 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_550_saline_day1_20min_1 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort1_saline_day1_550.streams._405A.data[2 * t_coc + 1:4 * t_coc])
y1 = np.array(cohort1_saline_day1_550.streams._470A.data[2 * t_coc + 1:4 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_550_saline_day1_20min_3 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort1_saline_day1_550.streams._405A.data[4 * t_coc + 1:6 * t_coc])
y1 = np.array(cohort1_saline_day1_550.streams._470A.data[4 * t_coc + 1:6 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_550_saline_day1_20min_5 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort1_saline_day1_550.streams._405A.data[6 * t_coc + 1:8 * t_coc])
y1 = np.array(cohort1_saline_day1_550.streams._470A.data[6 * t_coc + 1:8 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_550_saline_day1_20min_7 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x_550_saline_day1_20min = np.concatenate((x_550_saline_day1_20min_1,
                                          x_550_saline_day1_20min_3,
                                          x_550_saline_day1_20min_5,
                                          x_550_saline_day1_20min_7), axis=0)

x1 = np.array(cohort1_saline_day3_550.streams._405A.data[0:2 * t_coc])
y1 = np.array(cohort1_saline_day3_550.streams._470A.data[0:2 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_550_saline_day3_20min_1 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort1_saline_day3_550.streams._405A.data[2 * t_coc + 1:4 * t_coc])
y1 = np.array(cohort1_saline_day3_550.streams._470A.data[2 * t_coc + 1:4 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_550_saline_day3_20min_3 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort1_saline_day3_550.streams._405A.data[4 * t_coc + 1:6 * t_coc])
y1 = np.array(cohort1_saline_day3_550.streams._470A.data[4 * t_coc + 1:6 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_550_saline_day3_20min_5 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort1_saline_day3_550.streams._405A.data[6 * t_coc + 1:8 * t_coc])
y1 = np.array(cohort1_saline_day3_550.streams._470A.data[6 * t_coc + 1:8 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_550_saline_day3_20min_7 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x_550_saline_day3_20min = np.concatenate((x_550_saline_day3_20min_1,
                                          x_550_saline_day3_20min_3,
                                          x_550_saline_day3_20min_5,
                                          x_550_saline_day3_20min_7), axis=0)

# x1 = np.array(cohort1_saline_day3_574.streams._405A.data[0:8*t_coc])
# y1 = np.array(cohort1_saline_day3_574.streams._470A.data[0:8*t_coc])
# bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
# fit_line = np.multiply(bls[0],x1)+bls[1]
# x_574__saline_day3_20min = np.array(stats.zscore((np.array(y1-fit_line)/np.array(fit_line))))


x1 = np.array(cohort1_saline_day1_574.streams._405A.data[0:2 * t_coc])
y1 = np.array(cohort1_saline_day1_574.streams._470A.data[0:2 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_574_saline_day1_20min_1 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort1_saline_day1_574.streams._405A.data[2 * t_coc + 1:4 * t_coc])
y1 = np.array(cohort1_saline_day1_574.streams._470A.data[2 * t_coc + 1:4 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_574_saline_day1_20min_3 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort1_saline_day1_574.streams._405A.data[4 * t_coc + 1:6 * t_coc])
y1 = np.array(cohort1_saline_day1_574.streams._470A.data[4 * t_coc + 1:6 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_574_saline_day1_20min_5 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort1_saline_day1_574.streams._405A.data[6 * t_coc + 1:8 * t_coc])
y1 = np.array(cohort1_saline_day1_574.streams._470A.data[6 * t_coc + 1:8 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_574_saline_day1_20min_7 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x_574_saline_day1_20min = np.concatenate((x_574_saline_day1_20min_1,
                                          x_574_saline_day1_20min_3,
                                          x_574_saline_day1_20min_5,
                                          x_574_saline_day1_20min_7), axis=0)

x1 = np.array(cohort1_saline_day3_574.streams._405A.data[0:2 * t_coc])
y1 = np.array(cohort1_saline_day3_574.streams._470A.data[0:2 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_574_saline_day3_20min_1 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort1_saline_day3_574.streams._405A.data[2 * t_coc + 1:4 * t_coc])
y1 = np.array(cohort1_saline_day3_574.streams._470A.data[2 * t_coc + 1:4 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_574_saline_day3_20min_3 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort1_saline_day3_574.streams._405A.data[4 * t_coc + 1:6 * t_coc])
y1 = np.array(cohort1_saline_day3_574.streams._470A.data[4 * t_coc + 1:6 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_574_saline_day3_20min_5 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort1_saline_day3_574.streams._405A.data[6 * t_coc + 1:8 * t_coc])
y1 = np.array(cohort1_saline_day3_574.streams._470A.data[6 * t_coc + 1:8 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_574_saline_day3_20min_7 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x_574_saline_day3_20min = np.concatenate((x_574_saline_day3_20min_1,
                                          x_574_saline_day3_20min_3,
                                          x_574_saline_day3_20min_5,
                                          x_574_saline_day3_20min_7), axis=0)

x1 = np.array(cohort1_cocaine_day1_574.streams._405A.data[0:2 * t_coc])
y1 = np.array(cohort1_cocaine_day1_574.streams._470A.data[0:2 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_574_cocaine_day1_20min_1 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort1_cocaine_day1_574.streams._405A.data[2 * t_coc + 1:4 * t_coc])
y1 = np.array(cohort1_cocaine_day1_574.streams._470A.data[2 * t_coc + 1:4 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_574_cocaine_day1_20min_3 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort1_cocaine_day1_574.streams._405A.data[4 * t_coc + 1:6 * t_coc])
y1 = np.array(cohort1_cocaine_day1_574.streams._470A.data[4 * t_coc + 1:6 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_574_cocaine_day1_20min_5 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort1_cocaine_day1_574.streams._405A.data[6 * t_coc + 1:8 * t_coc])
y1 = np.array(cohort1_cocaine_day1_574.streams._470A.data[6 * t_coc + 1:8 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_574_cocaine_day1_20min_7 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x_574_cocaine_day1_20min = np.concatenate((x_574_cocaine_day1_20min_1,
                                           x_574_cocaine_day1_20min_3,
                                           x_574_cocaine_day1_20min_5,
                                           x_574_cocaine_day1_20min_7), axis=0)

x1 = np.array(cohort1_cocaine_day3_574.streams._405A.data[0:2 * t_coc])
y1 = np.array(cohort1_cocaine_day3_574.streams._470A.data[0:2 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_574_cocaine_day3_20min_1 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort1_cocaine_day3_574.streams._405A.data[2 * t_coc + 1:4 * t_coc])
y1 = np.array(cohort1_cocaine_day3_574.streams._470A.data[2 * t_coc + 1:4 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_574_cocaine_day3_20min_3 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort1_cocaine_day3_574.streams._405A.data[4 * t_coc + 1:6 * t_coc])
y1 = np.array(cohort1_cocaine_day3_574.streams._470A.data[4 * t_coc + 1:6 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_574_cocaine_day3_20min_5 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort1_cocaine_day3_574.streams._405A.data[6 * t_coc + 1:8 * t_coc])
y1 = np.array(cohort1_cocaine_day3_574.streams._470A.data[6 * t_coc + 1:8 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_574_cocaine_day3_20min_7 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x_574_cocaine_day3_20min = np.concatenate((x_574_cocaine_day3_20min_1,
                                           x_574_cocaine_day3_20min_3,
                                           x_574_cocaine_day3_20min_5,
                                           x_574_cocaine_day3_20min_7), axis=0)

# x1 = np.array(cohort1_cocaine_day1_580.streams._405A.data[0:8*t_coc])
# y1 = np.array(cohort1_cocaine_day1_580.streams._470A.data[0:8*t_coc])
# bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
# fit_line = np.multiply(bls[0],x1)+bls[1]
# x_580__cocaine_day1_20min = np.array(stats.zscore((np.array(y1-fit_line)/np.array(fit_line))))


x1 = np.array(cohort1_cocaine_day1_580.streams._405A.data[0:2 * t_coc])
y1 = np.array(cohort1_cocaine_day1_580.streams._470A.data[0:2 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_580_cocaine_day1_20min_1 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort1_cocaine_day1_580.streams._405A.data[2 * t_coc + 1:4 * t_coc])
y1 = np.array(cohort1_cocaine_day1_580.streams._470A.data[2 * t_coc + 1:4 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_580_cocaine_day1_20min_3 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort1_cocaine_day1_580.streams._405A.data[4 * t_coc + 1:6 * t_coc])
y1 = np.array(cohort1_cocaine_day1_580.streams._470A.data[4 * t_coc + 1:6 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_580_cocaine_day1_20min_5 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort1_cocaine_day1_580.streams._405A.data[6 * t_coc + 1:8 * t_coc])
y1 = np.array(cohort1_cocaine_day1_580.streams._470A.data[6 * t_coc + 1:8 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_580_cocaine_day1_20min_7 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x_580_cocaine_day1_20min = np.concatenate((x_580_cocaine_day1_20min_1,
                                           x_580_cocaine_day1_20min_3,
                                           x_580_cocaine_day1_20min_5,
                                           x_580_cocaine_day1_20min_7), axis=0)

# x1 = np.array(cohort1_cocaine_day3_580.streams._405A.data[0:8*t_coc])
# y1 = np.array(cohort1_cocaine_day3_580.streams._470A.data[0:8*t_coc])
# bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
# fit_line = np.multiply(bls[0],x1)+bls[1]
# x_580__cocaine_day3_20min = np.array(stats.zscore((np.array(y1-fit_line)/np.array(fit_line))))


x1 = np.array(cohort1_cocaine_day3_580.streams._405A.data[0:2 * t_coc])
y1 = np.array(cohort1_cocaine_day3_580.streams._470A.data[0:2 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_580_cocaine_day3_20min_1 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort1_cocaine_day3_580.streams._405A.data[2 * t_coc + 1:4 * t_coc])
y1 = np.array(cohort1_cocaine_day3_580.streams._470A.data[2 * t_coc + 1:4 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_580_cocaine_day3_20min_3 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort1_cocaine_day3_580.streams._405A.data[4 * t_coc + 1:6 * t_coc])
y1 = np.array(cohort1_cocaine_day3_580.streams._470A.data[4 * t_coc + 1:6 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_580_cocaine_day3_20min_5 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort1_cocaine_day3_580.streams._405A.data[6 * t_coc + 1:8 * t_coc])
y1 = np.array(cohort1_cocaine_day3_580.streams._470A.data[6 * t_coc + 1:8 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_580_cocaine_day3_20min_7 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x_580_cocaine_day3_20min = np.concatenate((x_580_cocaine_day3_20min_1,
                                           x_580_cocaine_day3_20min_3,
                                           x_580_cocaine_day3_20min_5,
                                           x_580_cocaine_day3_20min_7), axis=0)

# x1 = np.array(cohort1_saline_day1_580.streams._405A.data[0:8*t_coc])
# y1 = np.array(cohort1_saline_day1_580.streams._470A.data[0:8*t_coc])
# bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
# fit_line = np.multiply(bls[0],x1)+bls[1]
# x_580__saline_day1_20min = np.array(stats.zscore((np.array(y1-fit_line)/np.array(fit_line))))

x1 = np.array(cohort1_saline_day1_580.streams._405A.data[0:2 * t_coc])
y1 = np.array(cohort1_saline_day1_580.streams._470A.data[0:2 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_580_saline_day1_20min_1 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort1_saline_day1_580.streams._405A.data[2 * t_coc + 1:4 * t_coc])
y1 = np.array(cohort1_saline_day1_580.streams._470A.data[2 * t_coc + 1:4 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_580_saline_day1_20min_3 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort1_saline_day1_580.streams._405A.data[4 * t_coc + 1:6 * t_coc])
y1 = np.array(cohort1_saline_day1_580.streams._470A.data[4 * t_coc + 1:6 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_580_saline_day1_20min_5 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort1_saline_day1_580.streams._405A.data[6 * t_coc + 1:8 * t_coc])
y1 = np.array(cohort1_saline_day1_580.streams._470A.data[6 * t_coc + 1:8 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_580_saline_day1_20min_7 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x_580_saline_day1_20min = np.concatenate((x_580_saline_day1_20min_1,
                                          x_580_saline_day1_20min_3,
                                          x_580_saline_day1_20min_5,
                                          x_580_saline_day1_20min_7), axis=0)

# x1 = np.array(cohort1_saline_day3_580.streams._405A.data[0:8*t_coc])
# y1 = np.array(cohort1_saline_day3_580.streams._470A.data[0:8*t_coc])
# bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
# fit_line = np.multiply(bls[0],x1)+bls[1]
# x_580__saline_day3_20min = np.array(stats.zscore((np.array(y1-fit_line)/np.array(fit_line))))

x1 = np.array(cohort1_saline_day3_580.streams._405A.data[0:2 * t_coc])
y1 = np.array(cohort1_saline_day3_580.streams._470A.data[0:2 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_580_saline_day3_20min_1 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort1_saline_day3_580.streams._405A.data[2 * t_coc + 1:4 * t_coc])
y1 = np.array(cohort1_saline_day3_580.streams._470A.data[2 * t_coc + 1:4 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_580_saline_day3_20min_3 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort1_saline_day3_580.streams._405A.data[4 * t_coc + 1:6 * t_coc])
y1 = np.array(cohort1_saline_day3_580.streams._470A.data[4 * t_coc + 1:6 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_580_saline_day3_20min_5 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort1_saline_day3_580.streams._405A.data[6 * t_coc + 1:8 * t_coc])
y1 = np.array(cohort1_saline_day3_580.streams._470A.data[6 * t_coc + 1:8 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_580_saline_day3_20min_7 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x_580_saline_day3_20min = np.concatenate((x_580_saline_day3_20min_1,
                                          x_580_saline_day3_20min_3,
                                          x_580_saline_day3_20min_5,
                                          x_580_saline_day3_20min_7), axis=0)

# x1 = np.array(cohort1_cocaine_day1_549.streams._405A.data[0:8*t_coc])
# y1 = np.array(cohort1_cocaine_day1_549.streams._470A.data[0:8*t_coc])
# bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
# fit_line = np.multiply(bls[0],x1)+bls[1]
# x_549__cocaine_day1_20min = np.array(stats.zscore((np.array(y1-fit_line)/np.array(fit_line))))

x1 = np.array(cohort1_cocaine_day1_549.streams._405A.data[0:2 * t_coc])
y1 = np.array(cohort1_cocaine_day1_549.streams._470A.data[0:2 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_549_cocaine_day1_20min_1 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort1_cocaine_day1_549.streams._405A.data[2 * t_coc + 1:4 * t_coc])
y1 = np.array(cohort1_cocaine_day1_549.streams._470A.data[2 * t_coc + 1:4 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_549_cocaine_day1_20min_3 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort1_cocaine_day1_549.streams._405A.data[4 * t_coc + 1:6 * t_coc])
y1 = np.array(cohort1_cocaine_day1_549.streams._470A.data[4 * t_coc + 1:6 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_549_cocaine_day1_20min_5 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort1_cocaine_day1_549.streams._405A.data[6 * t_coc + 1:8 * t_coc])
y1 = np.array(cohort1_cocaine_day1_549.streams._470A.data[6 * t_coc + 1:8 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_549_cocaine_day1_20min_7 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x_549_cocaine_day1_20min = np.concatenate((x_549_cocaine_day1_20min_1,
                                           x_549_cocaine_day1_20min_3,
                                           x_549_cocaine_day1_20min_5,
                                           x_549_cocaine_day1_20min_7), axis=0)

# x1 = np.array(cohort1_cocaine_day3_549.streams._405A.data[0:8*t_coc])
# y1 = np.array(cohort1_cocaine_day3_549.streams._470A.data[0:8*t_coc])
# bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
# fit_line = np.multiply(bls[0],x1)+bls[1]
# x_549__cocaine_day3_20min = np.array(stats.zscore((np.array(y1-fit_line)/np.array(fit_line))))


x1 = np.array(cohort1_cocaine_day3_549.streams._405A.data[0:2 * t_coc])
y1 = np.array(cohort1_cocaine_day3_549.streams._470A.data[0:2 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_549_cocaine_day3_20min_1 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort1_cocaine_day3_549.streams._405A.data[2 * t_coc + 1:4 * t_coc])
y1 = np.array(cohort1_cocaine_day3_549.streams._470A.data[2 * t_coc + 1:4 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_549_cocaine_day3_20min_3 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort1_cocaine_day3_549.streams._405A.data[4 * t_coc + 1:6 * t_coc])
y1 = np.array(cohort1_cocaine_day3_549.streams._470A.data[4 * t_coc + 1:6 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_549_cocaine_day3_20min_5 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort1_cocaine_day3_549.streams._405A.data[6 * t_coc + 1:8 * t_coc])
y1 = np.array(cohort1_cocaine_day3_549.streams._470A.data[6 * t_coc + 1:8 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_549_cocaine_day3_20min_7 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x_549_cocaine_day3_20min = np.concatenate((x_549_cocaine_day3_20min_1,
                                           x_549_cocaine_day3_20min_3,
                                           x_549_cocaine_day3_20min_5,
                                           x_549_cocaine_day3_20min_7), axis=0)
# x1 = np.array(cohort1_saline_day1_549.streams._405A.data[0:8*t_coc])
# y1 = np.array(cohort1_saline_day1_549.streams._470A.data[0:8*t_coc])
# bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
# fit_line = np.multiply(bls[0],x1)+bls[1]
# x_549__saline_day1_20min = np.array(stats.zscore((np.array(y1-fit_line)/np.array(fit_line))))


x1 = np.array(cohort1_saline_day1_549.streams._405A.data[0:2 * t_coc])
y1 = np.array(cohort1_saline_day1_549.streams._470A.data[0:2 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_549_saline_day1_20min_1 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort1_saline_day1_549.streams._405A.data[2 * t_coc + 1:4 * t_coc])
y1 = np.array(cohort1_saline_day1_549.streams._470A.data[2 * t_coc + 1:4 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_549_saline_day1_20min_3 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort1_saline_day1_549.streams._405A.data[4 * t_coc + 1:6 * t_coc])
y1 = np.array(cohort1_saline_day1_549.streams._470A.data[4 * t_coc + 1:6 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_549_saline_day1_20min_5 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort1_saline_day1_549.streams._405A.data[6 * t_coc + 1:8 * t_coc])
y1 = np.array(cohort1_saline_day1_549.streams._470A.data[6 * t_coc + 1:8 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_549_saline_day1_20min_7 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x_549_saline_day1_20min = np.concatenate((x_549_saline_day1_20min_1,
                                          x_549_saline_day1_20min_3,
                                          x_549_saline_day1_20min_5,
                                          x_549_saline_day1_20min_7), axis=0)

# x1 = np.array(cohort1_saline_day3_549.streams._405A.data[0:8*t_coc])
# y1 = np.array(cohort1_saline_day3_549.streams._470A.data[0:8*t_coc])
# bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
# fit_line = np.multiply(bls[0],x1)+bls[1]
# x_549__saline_day3_20min = np.array(stats.zscore((np.array(y1-fit_line)/np.array(fit_line))))
x1 = np.array(cohort1_saline_day3_549.streams._405A.data[0:2 * t_coc])
y1 = np.array(cohort1_saline_day3_549.streams._470A.data[0:2 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_549_saline_day3_20min_1 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort1_saline_day3_549.streams._405A.data[2 * t_coc + 1:4 * t_coc])
y1 = np.array(cohort1_saline_day3_549.streams._470A.data[2 * t_coc + 1:4 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_549_saline_day3_20min_3 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort1_saline_day3_549.streams._405A.data[4 * t_coc + 1:6 * t_coc])
y1 = np.array(cohort1_saline_day3_549.streams._470A.data[4 * t_coc + 1:6 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_549_saline_day3_20min_5 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort1_saline_day3_549.streams._405A.data[6 * t_coc + 1:8 * t_coc])
y1 = np.array(cohort1_saline_day3_549.streams._470A.data[6 * t_coc + 1:8 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_549_saline_day3_20min_7 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x_549_saline_day3_20min = np.concatenate((x_549_saline_day3_20min_1,
                                          x_549_saline_day3_20min_3,
                                          x_549_saline_day3_20min_5,
                                          x_549_saline_day3_20min_7), axis=0)

x1 = np.array(cohort1_cocaine_day1_549.streams._405A.data[0:2 * t_coc])
y1 = np.array(cohort1_cocaine_day1_549.streams._470A.data[0:2 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_549_cocaine_day1_20min_1 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort1_cocaine_day1_549.streams._405A.data[2 * t_coc + 1:4 * t_coc])
y1 = np.array(cohort1_cocaine_day1_549.streams._470A.data[2 * t_coc + 1:4 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_549_cocaine_day1_20min_3 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort1_cocaine_day1_549.streams._405A.data[4 * t_coc + 1:6 * t_coc])
y1 = np.array(cohort1_cocaine_day1_549.streams._470A.data[4 * t_coc + 1:6 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_549_cocaine_day1_20min_5 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort1_cocaine_day1_549.streams._405A.data[6 * t_coc + 1:8 * t_coc])
y1 = np.array(cohort1_cocaine_day1_549.streams._470A.data[6 * t_coc + 1:8 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_549_cocaine_day1_20min_7 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x_549_cocaine_day1_20min = np.concatenate((x_549_cocaine_day1_20min_1,
                                           x_549_cocaine_day1_20min_3,
                                           x_549_cocaine_day1_20min_5,
                                           x_549_cocaine_day1_20min_7), axis=0)

# x1 = np.array(cohort1_cocaine_day1_325.streams._405A.data[0:8*t_coc])
# y1 = np.array(cohort1_cocaine_day1_325.streams._470A.data[0:8*t_coc])
# bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
# fit_line = np.multiply(bls[0],x1)+bls[1]
# x_325__cocaine_day1_20min = np.array(stats.zscore((np.array(y1-fit_line)/np.array(fit_line))))

x1 = np.array(cohort1_cocaine_day1_325.streams._405A.data[0:2 * t_coc])
y1 = np.array(cohort1_cocaine_day1_325.streams._470A.data[0:2 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_325_cocaine_day1_20min_1 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort1_cocaine_day1_325.streams._405A.data[2 * t_coc + 1:4 * t_coc])
y1 = np.array(cohort1_cocaine_day1_325.streams._470A.data[2 * t_coc + 1:4 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_325_cocaine_day1_20min_3 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort1_cocaine_day1_325.streams._405A.data[4 * t_coc + 1:6 * t_coc])
y1 = np.array(cohort1_cocaine_day1_325.streams._470A.data[4 * t_coc + 1:6 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_325_cocaine_day1_20min_5 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort1_cocaine_day1_325.streams._405A.data[6 * t_coc + 1:8 * t_coc])
y1 = np.array(cohort1_cocaine_day1_325.streams._470A.data[6 * t_coc + 1:8 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_325_cocaine_day1_20min_7 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x_325_cocaine_day1_20min = np.concatenate((x_325_cocaine_day1_20min_1,
                                           x_325_cocaine_day1_20min_3,
                                           x_325_cocaine_day1_20min_5,
                                           x_325_cocaine_day1_20min_7), axis=0)

# x1 = np.array(cohort1_cocaine_day3_325.streams._405A.data[0:8*t_coc])
# y1 = np.array(cohort1_cocaine_day3_325.streams._470A.data[0:8*t_coc])
# bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
# fit_line = np.multiply(bls[0],x1)+bls[1]
# x_325__cocaine_day3_20min = np.array(stats.zscore((np.array(y1-fit_line)/np.array(fit_line))))


x1 = np.array(cohort1_cocaine_day3_325.streams._405A.data[0:2 * t_coc])
y1 = np.array(cohort1_cocaine_day3_325.streams._470A.data[0:2 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_325_cocaine_day3_20min_1 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort1_cocaine_day3_325.streams._405A.data[2 * t_coc + 1:4 * t_coc])
y1 = np.array(cohort1_cocaine_day3_325.streams._470A.data[2 * t_coc + 1:4 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_325_cocaine_day3_20min_3 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort1_cocaine_day3_325.streams._405A.data[4 * t_coc + 1:6 * t_coc])
y1 = np.array(cohort1_cocaine_day3_325.streams._470A.data[4 * t_coc + 1:6 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_325_cocaine_day3_20min_5 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort1_cocaine_day3_325.streams._405A.data[6 * t_coc + 1:8 * t_coc])
y1 = np.array(cohort1_cocaine_day3_325.streams._470A.data[6 * t_coc + 1:8 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_325_cocaine_day3_20min_7 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x_325_cocaine_day3_20min = np.concatenate((x_325_cocaine_day3_20min_1,
                                           x_325_cocaine_day3_20min_3,
                                           x_325_cocaine_day3_20min_5,
                                           x_325_cocaine_day3_20min_7), axis=0)

# x1 = np.array(cohort1_saline_day1_325.streams._405A.data[0:8*t_coc])
# y1 = np.array(cohort1_saline_day1_325.streams._470A.data[0:8*t_coc])
# bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
# fit_line = np.multiply(bls[0],x1)+bls[1]
# x_325__saline_day1_20min = np.array(stats.zscore((np.array(y1-fit_line)/np.array(fit_line))))

x1 = np.array(cohort1_saline_day1_325.streams._405A.data[0:2 * t_coc])
y1 = np.array(cohort1_saline_day1_325.streams._470A.data[0:2 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_325_saline_day1_20min_1 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort1_saline_day1_325.streams._405A.data[2 * t_coc + 1:4 * t_coc])
y1 = np.array(cohort1_saline_day1_325.streams._470A.data[2 * t_coc + 1:4 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_325_saline_day1_20min_3 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort1_saline_day1_325.streams._405A.data[4 * t_coc + 1:6 * t_coc])
y1 = np.array(cohort1_saline_day1_325.streams._470A.data[4 * t_coc + 1:6 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_325_saline_day1_20min_5 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort1_saline_day1_325.streams._405A.data[6 * t_coc + 1:8 * t_coc])
y1 = np.array(cohort1_saline_day1_325.streams._470A.data[6 * t_coc + 1:8 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_325_saline_day1_20min_7 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x_325_saline_day1_20min = np.concatenate((x_325_saline_day1_20min_1,
                                          x_325_saline_day1_20min_3,
                                          x_325_saline_day1_20min_5,
                                          x_325_saline_day1_20min_7), axis=0)

# x1 = np.array(cohort1_saline_day3_325.streams._405A.data[0:8*t_coc])
# y1 = np.array(cohort1_saline_day3_325.streams._470A.data[0:8*t_coc])
# bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
# fit_line = np.multiply(bls[0],x1)+bls[1]
# x_325__saline_day3_20min = np.array(stats.zscore((np.array(y1-fit_line)/np.array(fit_line))))
x1 = np.array(cohort1_saline_day3_325.streams._405A.data[0:2 * t_coc])
y1 = np.array(cohort1_saline_day3_325.streams._470A.data[0:2 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_325_saline_day3_20min_1 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort1_saline_day3_325.streams._405A.data[2 * t_coc + 1:4 * t_coc])
y1 = np.array(cohort1_saline_day3_325.streams._470A.data[2 * t_coc + 1:4 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_325_saline_day3_20min_3 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort1_saline_day3_325.streams._405A.data[4 * t_coc + 1:6 * t_coc])
y1 = np.array(cohort1_saline_day3_325.streams._470A.data[4 * t_coc + 1:6 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_325_saline_day3_20min_5 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort1_saline_day3_325.streams._405A.data[6 * t_coc + 1:8 * t_coc])
y1 = np.array(cohort1_saline_day3_325.streams._470A.data[6 * t_coc + 1:8 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_325_saline_day3_20min_7 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x_325_saline_day3_20min = np.concatenate((x_325_saline_day3_20min_1,
                                          x_325_saline_day3_20min_3,
                                          x_325_saline_day3_20min_5,
                                          x_325_saline_day3_20min_7), axis=0)

# x1 = np.array(cohort1_cocaine_day1_552.streams._405A.data[0:8*t_coc])
# y1 = np.array(cohort1_cocaine_day1_552.streams._470A.data[0:8*t_coc])
# bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
# fit_line = np.multiply(bls[0],x1)+bls[1]
# x_552__cocaine_day1_20min = np.array(stats.zscore((np.array(y1-fit_line)/np.array(fit_line))))

x1 = np.array(cohort1_cocaine_day1_552.streams._405A.data[0:2 * t_coc])
y1 = np.array(cohort1_cocaine_day1_552.streams._470A.data[0:2 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_552_cocaine_day1_20min_1 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort1_cocaine_day1_552.streams._405A.data[2 * t_coc + 1:4 * t_coc])
y1 = np.array(cohort1_cocaine_day1_552.streams._470A.data[2 * t_coc + 1:4 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_552_cocaine_day1_20min_3 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort1_cocaine_day1_552.streams._405A.data[4 * t_coc + 1:6 * t_coc])
y1 = np.array(cohort1_cocaine_day1_552.streams._470A.data[4 * t_coc + 1:6 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_552_cocaine_day1_20min_5 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort1_cocaine_day1_552.streams._405A.data[6 * t_coc + 1:8 * t_coc])
y1 = np.array(cohort1_cocaine_day1_552.streams._470A.data[6 * t_coc + 1:8 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_552_cocaine_day1_20min_7 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x_552_cocaine_day1_20min = np.concatenate((x_552_cocaine_day1_20min_1,
                                           x_552_cocaine_day1_20min_3,
                                           x_552_cocaine_day1_20min_5,
                                           x_552_cocaine_day1_20min_7), axis=0)

# x1 = np.array(cohort1_cocaine_day3_552.streams._405A.data[0:8*t_coc])
# y1 = np.array(cohort1_cocaine_day3_552.streams._470A.data[0:8*t_coc])
# bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
# fit_line = np.multiply(bls[0],x1)+bls[1]
# x_552__cocaine_day3_20min = np.array(stats.zscore((np.array(y1-fit_line)/np.array(fit_line))))
x1 = np.array(cohort1_cocaine_day3_552.streams._405A.data[0:2 * t_coc])
y1 = np.array(cohort1_cocaine_day3_552.streams._470A.data[0:2 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_552_cocaine_day3_20min_1 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort1_cocaine_day3_552.streams._405A.data[2 * t_coc + 1:4 * t_coc])
y1 = np.array(cohort1_cocaine_day3_552.streams._470A.data[2 * t_coc + 1:4 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_552_cocaine_day3_20min_3 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort1_cocaine_day3_552.streams._405A.data[4 * t_coc + 1:6 * t_coc])
y1 = np.array(cohort1_cocaine_day3_552.streams._470A.data[4 * t_coc + 1:6 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_552_cocaine_day3_20min_5 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort1_cocaine_day3_552.streams._405A.data[6 * t_coc + 1:8 * t_coc])
y1 = np.array(cohort1_cocaine_day3_552.streams._470A.data[6 * t_coc + 1:8 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_552_cocaine_day3_20min_7 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x_552_cocaine_day3_20min = np.concatenate((x_552_cocaine_day3_20min_1,
                                           x_552_cocaine_day3_20min_3,
                                           x_552_cocaine_day3_20min_5,
                                           x_552_cocaine_day3_20min_7), axis=0)

# x1 = np.array(cohort1_saline_day1_552.streams._405A.data[0:8*t_coc])
# y1 = np.array(cohort1_saline_day1_552.streams._470A.data[0:8*t_coc])
# bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
# fit_line = np.multiply(bls[0],x1)+bls[1]
# x_552__saline_day1_20min = np.array(stats.zscore((np.array(y1-fit_line)/np.array(fit_line))))


x1 = np.array(cohort1_saline_day1_552.streams._405A.data[0:2 * t_coc])
y1 = np.array(cohort1_saline_day1_552.streams._470A.data[0:2 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_552_saline_day1_20min_1 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort1_saline_day1_552.streams._405A.data[2 * t_coc + 1:4 * t_coc])
y1 = np.array(cohort1_saline_day1_552.streams._470A.data[2 * t_coc + 1:4 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_552_saline_day1_20min_3 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort1_saline_day1_552.streams._405A.data[4 * t_coc + 1:6 * t_coc])
y1 = np.array(cohort1_saline_day1_552.streams._470A.data[4 * t_coc + 1:6 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_552_saline_day1_20min_5 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort1_saline_day1_552.streams._405A.data[6 * t_coc + 1:8 * t_coc])
y1 = np.array(cohort1_saline_day1_552.streams._470A.data[6 * t_coc + 1:8 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_552_saline_day1_20min_7 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x_552_saline_day1_20min = np.concatenate((x_552_saline_day1_20min_1,
                                          x_552_saline_day1_20min_3,
                                          x_552_saline_day1_20min_5,
                                          x_552_saline_day1_20min_7), axis=0)

# x1 = np.array(cohort1_saline_day3_552.streams._405A.data[0:8*t_coc])
# y1 = np.array(cohort1_saline_day3_552.streams._470A.data[0:8*t_coc])
# bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
# fit_line = np.multiply(bls[0],x1)+bls[1]
# x_552__saline_day3_20min = np.array(stats.zscore((np.array(y1-fit_line)/np.array(fit_line))))

x1 = np.array(cohort1_saline_day3_552.streams._405A.data[0:2 * t_coc])
y1 = np.array(cohort1_saline_day3_552.streams._470A.data[0:2 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_552_saline_day3_20min_1 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort1_saline_day3_552.streams._405A.data[2 * t_coc + 1:4 * t_coc])
y1 = np.array(cohort1_saline_day3_552.streams._470A.data[2 * t_coc + 1:4 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_552_saline_day3_20min_3 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort1_saline_day3_552.streams._405A.data[4 * t_coc + 1:6 * t_coc])
y1 = np.array(cohort1_saline_day3_552.streams._470A.data[4 * t_coc + 1:6 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_552_saline_day3_20min_5 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort1_saline_day3_552.streams._405A.data[6 * t_coc + 1:8 * t_coc])
y1 = np.array(cohort1_saline_day3_552.streams._470A.data[6 * t_coc + 1:8 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_552_saline_day3_20min_7 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x_552_saline_day3_20min = np.concatenate((x_552_saline_day3_20min_1,
                                          x_552_saline_day3_20min_3,
                                          x_552_saline_day3_20min_5,
                                          x_552_saline_day3_20min_7), axis=0)

# In[ ]:


# In[ ]:


# In[ ]:


# In[ ]:


# In[ ]:


# In[ ]:


# In[ ]:


# read_block is an all-in-one function for reading TDT data into Python. It needs only one input: the block path.
data1 = tdt.read_block(COHORT2_BLOCK_PATH1)
data2 = tdt.read_block(COHORT2_BLOCK_PATH2)
data3 = tdt.read_block(COHORT2_BLOCK_PATH3)
data4 = tdt.read_block(COHORT2_BLOCK_PATH4)
data5 = tdt.read_block(COHORT2_BLOCK_PATH5)
data6 = tdt.read_block(COHORT2_BLOCK_PATH6)
data7 = tdt.read_block(COHORT2_BLOCK_PATH7)
data8 = tdt.read_block(COHORT2_BLOCK_PATH8)
data9 = tdt.read_block(COHORT2_BLOCK_PATH9)
data10 = tdt.read_block(COHORT2_BLOCK_PATH10)
data11 = tdt.read_block(COHORT2_BLOCK_PATH11)
data12 = tdt.read_block(COHORT2_BLOCK_PATH12)
data13 = tdt.read_block(COHORT2_BLOCK_PATH13)
data14 = tdt.read_block(COHORT2_BLOCK_PATH14)
data15 = tdt.read_block(COHORT2_BLOCK_PATH15)
data16 = tdt.read_block(COHORT2_BLOCK_PATH16)
data17 = tdt.read_block(COHORT2_BLOCK_PATH17)
data18 = tdt.read_block(COHORT2_BLOCK_PATH18)
data19 = tdt.read_block(COHORT2_BLOCK_PATH19)
data20 = tdt.read_block(COHORT2_BLOCK_PATH20)
data21 = tdt.read_block(COHORT2_BLOCK_PATH21)
data22 = tdt.read_block(COHORT2_BLOCK_PATH22)

data23 = tdt.read_block(COHORT2_BLOCK_PATH23)
data24 = tdt.read_block(COHORT2_BLOCK_PATH24)
data25 = tdt.read_block(COHORT2_BLOCK_PATH25)
data26 = tdt.read_block(COHORT2_BLOCK_PATH26)
data27 = tdt.read_block(COHORT2_BLOCK_PATH27)
data28 = tdt.read_block(COHORT2_BLOCK_PATH28)
data29 = tdt.read_block(COHORT2_BLOCK_PATH29)
data30 = tdt.read_block(COHORT2_BLOCK_PATH30)
data31 = tdt.read_block(COHORT2_BLOCK_PATH31)
data32 = tdt.read_block(COHORT2_BLOCK_PATH32)
data33 = tdt.read_block(COHORT2_BLOCK_PATH33)
data34 = tdt.read_block(COHORT2_BLOCK_PATH34)
data35 = tdt.read_block(COHORT2_BLOCK_PATH35)
data36 = tdt.read_block(COHORT2_BLOCK_PATH36)
data37 = tdt.read_block(COHORT2_BLOCK_PATH37)
data38 = tdt.read_block(COHORT2_BLOCK_PATH38)
data39 = tdt.read_block(COHORT2_BLOCK_PATH39)
data40 = tdt.read_block(COHORT2_BLOCK_PATH40)
data41 = tdt.read_block(COHORT2_BLOCK_PATH41)
data42 = tdt.read_block(COHORT2_BLOCK_PATH42)
data43 = tdt.read_block(COHORT2_BLOCK_PATH43)
data44 = tdt.read_block(COHORT2_BLOCK_PATH44)

# In[ ]:


COHORT2_COCAINE_DAY1_616 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Cocaine Days/Cocaine Day 1_616"
COHORT2_COCAINE_DAY1_620 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Cocaine Days/Cocaine Day 1_620"
COHORT2_COCAINE_DAY1_621 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Cocaine Days/Cocaine Day 1_621"
COHORT2_COCAINE_DAY1_628 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Cocaine Days/Cocaine Day 1_628"
COHORT2_COCAINE_DAY1_638 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Cocaine Days/Cocaine Day 1_638"
COHORT2_COCAINE_DAY1_641 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Cocaine Days/Cocaine Day 1_641"
COHORT2_COCAINE_DAY1_642 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Cocaine Days/Cocaine Day 1_642"
COHORT2_COCAINE_DAY1_657 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Cocaine Days/Cocaine Day 1_657"
COHORT2_COCAINE_DAY1_660 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Cocaine Days/Cocaine Day 1_660"
COHORT2_COCAINE_DAY1_674 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Cocaine Days/Cocaine Day 1_674"
COHORT2_COCAINE_DAY1_675 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Cocaine Days/Cocaine Day 1_675"
COHORT2_SALINE_DAY1_616 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Saline Days/Saline Day 1_616"
COHORT2_SALINE_DAY1_620 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Saline Days/Saline Day 1_620"
COHORT2_SALINE_DAY1_621 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Saline Days/Saline Day 1_621"
COHORT2_SALINE_DAY1_628 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Saline Days/Saline Day 1_628"
COHORT2_SALINE_DAY1_638 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Saline Days/Saline Day 1_638"
COHORT2_SALINE_DAY1_641 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Saline Days/Saline Day 1_641"
COHORT2_SALINE_DAY1_642 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Saline Days/Saline Day 1_642"
COHORT2_SALINE_DAY1_657 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Saline Days/Saline Day 1_657"
COHORT2_SALINE_DAY1_660 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Saline Days/Saline Day 1_660"
COHORT2_SALINE_DAY1_674 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Saline Days/Saline Day 1_674"
COHORT2_SALINE_DAY1_675 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Saline Days/Saline Day 1_675"

COHORT2_COCAINE_DAY3_616 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Cocaine Days/Cocaine Day 3_616"
COHORT2_COCAINE_DAY3_620 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Cocaine Days/Cocaine Day 3_620"
COHORT2_COCAINE_DAY3_621 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Cocaine Days/Cocaine Day 3_621"
COHORT2_COCAINE_DAY3_628 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Cocaine Days/Cocaine Day 3_628"
COHORT2_COCAINE_DAY3_638 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Cocaine Days/Cocaine Day 3_638"
COHORT2_COCAINE_DAY3_641 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Cocaine Days/Cocaine Day 3_641"
COHORT2_COCAINE_DAY3_642 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Cocaine Days/Cocaine Day 3_642"
COHORT2_COCAINE_DAY3_657 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Cocaine Days/Cocaine Day 3_657"
COHORT2_COCAINE_DAY3_660 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Cocaine Days/Cocaine Day 3_660"
COHORT2_COCAINE_DAY3_674 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Cocaine Days/Cocaine Day 3_674"
COHORT2_COCAINE_DAY3_675 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Cocaine Days/Cocaine Day 3_675"
COHORT2_SALINE_DAY3_616 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Saline Days/Saline Day 3_616"
COHORT2_SALINE_DAY3_620 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Saline Days/Saline Day 3_620"
COHORT2_SALINE_DAY3_621 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Saline Days/Saline Day 3_621"
COHORT2_SALINE_DAY3_628 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Saline Days/Saline Day 3_628"
COHORT2_SALINE_DAY3_638 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Saline Days/Saline Day 3_638"
COHORT2_SALINE_DAY3_641 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Saline Days/Saline Day 3_641"
COHORT2_SALINE_DAY3_642 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Saline Days/Saline Day 3_642"
COHORT2_SALINE_DAY3_657 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Saline Days/Saline Day 3_657"
COHORT2_SALINE_DAY3_660 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Saline Days/Saline Day 3_660"
COHORT2_SALINE_DAY3_674 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Saline Days/Saline Day 3_674"
COHORT2_SALINE_DAY3_675 = "VTA FP DA_cohort 1 and 2/VTA FP DA_cohort 1 and 2/Cohort 2_500 ms pulse arduino/Saline Days/Saline Day 3_675"

# read_block is an all-in-one function for reading TDT data into Python. It needs only one input: the block path.
cohort2_cocaine_day1_616 = tdt.read_block(COHORT2_COCAINE_DAY1_616)
cohort2_cocaine_day1_620 = tdt.read_block(COHORT2_COCAINE_DAY1_620)
cohort2_cocaine_day1_621 = tdt.read_block(COHORT2_COCAINE_DAY1_621)
cohort2_cocaine_day1_628 = tdt.read_block(COHORT2_COCAINE_DAY1_628)
cohort2_cocaine_day1_638 = tdt.read_block(COHORT2_COCAINE_DAY1_638)
cohort2_cocaine_day1_641 = tdt.read_block(COHORT2_COCAINE_DAY1_641)
cohort2_cocaine_day1_642 = tdt.read_block(COHORT2_COCAINE_DAY1_642)
cohort2_cocaine_day1_657 = tdt.read_block(COHORT2_COCAINE_DAY1_657)
cohort2_cocaine_day1_660 = tdt.read_block(COHORT2_COCAINE_DAY1_660)
cohort2_cocaine_day1_674 = tdt.read_block(COHORT2_COCAINE_DAY1_674)
cohort2_cocaine_day1_675 = tdt.read_block(COHORT2_COCAINE_DAY1_675)
cohort2_cocaine_day3_616 = tdt.read_block(COHORT2_COCAINE_DAY3_616)
cohort2_cocaine_day3_620 = tdt.read_block(COHORT2_COCAINE_DAY3_620)
cohort2_cocaine_day3_621 = tdt.read_block(COHORT2_COCAINE_DAY3_621)
cohort2_cocaine_day3_628 = tdt.read_block(COHORT2_COCAINE_DAY3_628)
cohort2_cocaine_day3_638 = tdt.read_block(COHORT2_COCAINE_DAY3_638)
cohort2_cocaine_day3_641 = tdt.read_block(COHORT2_COCAINE_DAY3_641)
cohort2_cocaine_day3_642 = tdt.read_block(COHORT2_COCAINE_DAY3_642)
cohort2_cocaine_day3_657 = tdt.read_block(COHORT2_COCAINE_DAY3_657)
cohort2_cocaine_day3_660 = tdt.read_block(COHORT2_COCAINE_DAY3_660)
cohort2_cocaine_day3_674 = tdt.read_block(COHORT2_COCAINE_DAY3_674)
cohort2_cocaine_day3_675 = tdt.read_block(COHORT2_COCAINE_DAY3_675)

cohort2_saline_day1_616 = tdt.read_block(COHORT2_SALINE_DAY1_616)
cohort2_saline_day1_620 = tdt.read_block(COHORT2_SALINE_DAY1_620)
cohort2_saline_day1_621 = tdt.read_block(COHORT2_SALINE_DAY1_621)
cohort2_saline_day1_628 = tdt.read_block(COHORT2_SALINE_DAY1_628)
cohort2_saline_day1_638 = tdt.read_block(COHORT2_SALINE_DAY1_638)
cohort2_saline_day1_641 = tdt.read_block(COHORT2_SALINE_DAY1_641)
cohort2_saline_day1_642 = tdt.read_block(COHORT2_SALINE_DAY1_642)
cohort2_saline_day1_657 = tdt.read_block(COHORT2_SALINE_DAY1_657)
cohort2_saline_day1_660 = tdt.read_block(COHORT2_SALINE_DAY1_660)
cohort2_saline_day1_674 = tdt.read_block(COHORT2_SALINE_DAY1_674)
cohort2_saline_day1_675 = tdt.read_block(COHORT2_SALINE_DAY1_675)
cohort2_saline_day3_616 = tdt.read_block(COHORT2_SALINE_DAY3_616)
cohort2_saline_day3_620 = tdt.read_block(COHORT2_SALINE_DAY3_620)
cohort2_saline_day3_621 = tdt.read_block(COHORT2_SALINE_DAY3_621)
cohort2_saline_day3_628 = tdt.read_block(COHORT2_SALINE_DAY3_628)
cohort2_saline_day3_638 = tdt.read_block(COHORT2_SALINE_DAY3_638)
cohort2_saline_day3_641 = tdt.read_block(COHORT2_SALINE_DAY3_641)
cohort2_saline_day3_642 = tdt.read_block(COHORT2_SALINE_DAY3_642)
cohort2_saline_day3_657 = tdt.read_block(COHORT2_SALINE_DAY3_657)
cohort2_saline_day3_660 = tdt.read_block(COHORT2_SALINE_DAY3_660)
cohort2_saline_day3_674 = tdt.read_block(COHORT2_SALINE_DAY3_674)
cohort2_saline_day3_675 = tdt.read_block(COHORT2_SALINE_DAY3_675)

# ### Day 1 Baseline Recording Plots for 11 mice for the first 2 minutes

# In[ ]:


x1 = np.array(cohort3_data4.streams._405A.data[0:2 * t_coc])
y1 = np.array(cohort3_data4.streams._470A.data[0:2 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_3321_coc_day1_20min_1 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort3_data4.streams._405A.data[2 * t_coc + 1:4 * t_coc])
y1 = np.array(cohort3_data4.streams._470A.data[2 * t_coc + 1:4 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_3321_coc_day1_20min_3 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort3_data4.streams._405A.data[4 * t_coc + 1:6 * t_coc])
y1 = np.array(cohort3_data4.streams._470A.data[4 * t_coc + 1:6 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_3321_coc_day1_20min_5 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort3_data4.streams._405A.data[6 * t_coc + 1:8 * t_coc])
y1 = np.array(cohort3_data4.streams._470A.data[6 * t_coc + 1:8 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_3321_coc_day1_20min_7 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x_3321_coc_day1_20min = np.concatenate((x_3321_coc_day1_20min_1,
                                        x_3321_coc_day1_20min_3,
                                        x_3321_coc_day1_20min_5,
                                        x_3321_coc_day1_20min_7), axis=0)

x1 = np.array(cohort3_data5.streams._405A.data[0:2 * t_coc])
y1 = np.array(cohort3_data5.streams._470A.data[0:2 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_3336_coc_day1_20min_1 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort3_data5.streams._405A.data[2 * t_coc + 1:4 * t_coc])
y1 = np.array(cohort3_data5.streams._470A.data[2 * t_coc + 1:4 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_3336_coc_day1_20min_3 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort3_data5.streams._405A.data[4 * t_coc + 1:6 * t_coc])
y1 = np.array(cohort3_data5.streams._470A.data[4 * t_coc + 1:6 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_3336_coc_day1_20min_5 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort3_data5.streams._405A.data[6 * t_coc + 1:8 * t_coc])
y1 = np.array(cohort3_data5.streams._470A.data[6 * t_coc + 1:8 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_3336_coc_day1_20min_7 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x_3336_coc_day1_20min = np.concatenate((x_3336_coc_day1_20min_1,
                                        x_3336_coc_day1_20min_3,
                                        x_3336_coc_day1_20min_5,
                                        x_3336_coc_day1_20min_7), axis=0)

x1 = np.array(cohort3_data6.streams._405A.data[0:2 * t_coc])
y1 = np.array(cohort3_data6.streams._470A.data[0:2 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_3337_coc_day1_20min_1 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort3_data6.streams._405A.data[2 * t_coc + 1:4 * t_coc])
y1 = np.array(cohort3_data6.streams._470A.data[2 * t_coc + 1:4 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_3337_coc_day1_20min_3 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort3_data6.streams._405A.data[4 * t_coc + 1:6 * t_coc])
y1 = np.array(cohort3_data6.streams._470A.data[4 * t_coc + 1:6 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_3337_coc_day1_20min_5 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort3_data6.streams._405A.data[6 * t_coc + 1:8 * t_coc])
y1 = np.array(cohort3_data6.streams._470A.data[6 * t_coc + 1:8 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_3337_coc_day1_20min_7 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x_3337_coc_day1_20min = np.concatenate((x_3337_coc_day1_20min_1,
                                        x_3337_coc_day1_20min_3,
                                        x_3337_coc_day1_20min_5,
                                        x_3337_coc_day1_20min_7), axis=0)

x1 = np.array(cohort3_data9.streams._405A.data[0:2 * t_coc])
y1 = np.array(cohort3_data9.streams._470A.data[0:2 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_3341_coc_day1_20min_1 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort3_data9.streams._405A.data[2 * t_coc + 1:4 * t_coc])
y1 = np.array(cohort3_data9.streams._470A.data[2 * t_coc + 1:4 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_3341_coc_day1_20min_3 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort3_data9.streams._405A.data[4 * t_coc + 1:6 * t_coc])
y1 = np.array(cohort3_data9.streams._470A.data[4 * t_coc + 1:6 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_3341_coc_day1_20min_5 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort3_data9.streams._405A.data[6 * t_coc + 1:8 * t_coc])
y1 = np.array(cohort3_data9.streams._470A.data[6 * t_coc + 1:8 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_3341_coc_day1_20min_7 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x_3341_coc_day1_20min = np.concatenate((x_3341_coc_day1_20min_1,
                                        x_3341_coc_day1_20min_3,
                                        x_3341_coc_day1_20min_5,
                                        x_3341_coc_day1_20min_7), axis=0)

x1 = np.array(cohort3_data10.streams._405A.data[0:2 * t_coc])
y1 = np.array(cohort3_data10.streams._470A.data[0:2 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_3346_coc_day1_20min_1 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort3_data10.streams._405A.data[2 * t_coc + 1:4 * t_coc])
y1 = np.array(cohort3_data10.streams._470A.data[2 * t_coc + 1:4 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_3346_coc_day1_20min_3 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort3_data10.streams._405A.data[4 * t_coc + 1:6 * t_coc])
y1 = np.array(cohort3_data10.streams._470A.data[4 * t_coc + 1:6 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_3346_coc_day1_20min_5 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort3_data10.streams._405A.data[6 * t_coc + 1:8 * t_coc])
y1 = np.array(cohort3_data10.streams._470A.data[6 * t_coc + 1:8 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_3346_coc_day1_20min_7 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x_3346_coc_day1_20min = np.concatenate((x_3346_coc_day1_20min_1,
                                        x_3346_coc_day1_20min_3,
                                        x_3346_coc_day1_20min_5,
                                        x_3346_coc_day1_20min_7), axis=0)

x1 = np.array(cohort3_data14.streams._405A.data[0:2 * t_coc])
y1 = np.array(cohort3_data14.streams._470A.data[0:2 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_3321_coc_day3_20min_1 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort3_data14.streams._405A.data[2 * t_coc + 1:4 * t_coc])
y1 = np.array(cohort3_data14.streams._470A.data[2 * t_coc + 1:4 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_3321_coc_day3_20min_3 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort3_data14.streams._405A.data[4 * t_coc + 1:6 * t_coc])
y1 = np.array(cohort3_data14.streams._470A.data[4 * t_coc + 1:6 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_3321_coc_day3_20min_5 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort3_data14.streams._405A.data[6 * t_coc + 1:8 * t_coc])
y1 = np.array(cohort3_data14.streams._470A.data[6 * t_coc + 1:8 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_3321_coc_day3_20min_7 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x_3321_coc_day3_20min = np.concatenate((x_3321_coc_day3_20min_1,
                                        x_3321_coc_day3_20min_3,
                                        x_3321_coc_day3_20min_5,
                                        x_3321_coc_day3_20min_7), axis=0)

x1 = np.array(cohort3_data15.streams._405A.data[0:2 * t_coc])
y1 = np.array(cohort3_data15.streams._470A.data[0:2 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_3336_coc_day3_20min_1 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort3_data15.streams._405A.data[2 * t_coc + 1:4 * t_coc])
y1 = np.array(cohort3_data15.streams._470A.data[2 * t_coc + 1:4 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_3336_coc_day3_20min_3 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort3_data15.streams._405A.data[4 * t_coc + 1:6 * t_coc])
y1 = np.array(cohort3_data15.streams._470A.data[4 * t_coc + 1:6 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_3336_coc_day3_20min_5 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort3_data15.streams._405A.data[6 * t_coc + 1:8 * t_coc])
y1 = np.array(cohort3_data15.streams._470A.data[6 * t_coc + 1:8 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_3336_coc_day3_20min_7 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x_3336_coc_day3_20min = np.concatenate((x_3336_coc_day3_20min_1,
                                        x_3336_coc_day3_20min_3,
                                        x_3336_coc_day3_20min_5,
                                        x_3336_coc_day3_20min_7), axis=0)

x1 = np.array(cohort3_data16.streams._405A.data[0:2 * t_coc])
y1 = np.array(cohort3_data16.streams._470A.data[0:2 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_3337_coc_day3_20min_1 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort3_data16.streams._405A.data[2 * t_coc + 1:4 * t_coc])
y1 = np.array(cohort3_data16.streams._470A.data[2 * t_coc + 1:4 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_3337_coc_day3_20min_3 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort3_data16.streams._405A.data[4 * t_coc + 1:6 * t_coc])
y1 = np.array(cohort3_data16.streams._470A.data[4 * t_coc + 1:6 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_3337_coc_day3_20min_5 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort3_data16.streams._405A.data[6 * t_coc + 1:8 * t_coc])
y1 = np.array(cohort3_data16.streams._470A.data[6 * t_coc + 1:8 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_3337_coc_day3_20min_7 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x_3337_coc_day3_20min = np.concatenate((x_3337_coc_day3_20min_1,
                                        x_3337_coc_day3_20min_3,
                                        x_3337_coc_day3_20min_5,
                                        x_3337_coc_day3_20min_7), axis=0)

x1 = np.array(cohort3_data19.streams._405A.data[0:2 * t_coc])
y1 = np.array(cohort3_data19.streams._470A.data[0:2 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_3341_coc_day3_20min_1 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort3_data19.streams._405A.data[2 * t_coc + 1:4 * t_coc])
y1 = np.array(cohort3_data19.streams._470A.data[2 * t_coc + 1:4 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_3341_coc_day3_20min_3 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort3_data19.streams._405A.data[4 * t_coc + 1:6 * t_coc])
y1 = np.array(cohort3_data19.streams._470A.data[4 * t_coc + 1:6 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_3341_coc_day3_20min_5 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort3_data19.streams._405A.data[6 * t_coc + 1:8 * t_coc])
y1 = np.array(cohort3_data19.streams._470A.data[6 * t_coc + 1:8 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_3341_coc_day3_20min_7 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x_3341_coc_day3_20min = np.concatenate((x_3341_coc_day3_20min_1,
                                        x_3341_coc_day3_20min_3,
                                        x_3341_coc_day3_20min_5,
                                        x_3341_coc_day3_20min_7), axis=0)

x1 = np.array(cohort3_data20.streams._405A.data[0:2 * t_coc])
y1 = np.array(cohort3_data20.streams._470A.data[0:2 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_3346_coc_day3_20min_1 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort3_data20.streams._405A.data[2 * t_coc + 1:4 * t_coc])
y1 = np.array(cohort3_data20.streams._470A.data[2 * t_coc + 1:4 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_3346_coc_day3_20min_3 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort3_data20.streams._405A.data[4 * t_coc + 1:6 * t_coc])
y1 = np.array(cohort3_data20.streams._470A.data[4 * t_coc + 1:6 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_3346_coc_day3_20min_5 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort3_data20.streams._405A.data[6 * t_coc + 1:8 * t_coc])
y1 = np.array(cohort3_data20.streams._470A.data[6 * t_coc + 1:8 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_3346_coc_day3_20min_7 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x_3346_coc_day3_20min = np.concatenate((x_3346_coc_day3_20min_1,
                                        x_3346_coc_day3_20min_3,
                                        x_3346_coc_day3_20min_5,
                                        x_3346_coc_day3_20min_7), axis=0)

# x1 = np.array(cohort3_data24.streams._405A.data[0:8*t_coc])
# y1 = np.array(cohort3_data24.streams._470A.data[0:8*t_coc])
# bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
# fit_line = np.multiply(bls[0],x1)+bls[1]
# x_3321_sal_day1_20min = np.array(stats.zscore((np.array(y1-fit_line)/np.array(fit_line))))


x1 = np.array(cohort3_data24.streams._405A.data[0:2 * t_coc])
y1 = np.array(cohort3_data24.streams._470A.data[0:2 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_3321_sal_day1_20min_1 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort3_data24.streams._405A.data[2 * t_coc + 1:4 * t_coc])
y1 = np.array(cohort3_data24.streams._470A.data[2 * t_coc + 1:4 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_3321_sal_day1_20min_3 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort3_data24.streams._405A.data[4 * t_coc + 1:6 * t_coc])
y1 = np.array(cohort3_data24.streams._470A.data[4 * t_coc + 1:6 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_3321_sal_day1_20min_5 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort3_data24.streams._405A.data[6 * t_coc + 1:8 * t_coc])
y1 = np.array(cohort3_data24.streams._470A.data[6 * t_coc + 1:8 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_3321_sal_day1_20min_7 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x_3321_sal_day1_20min = np.concatenate((x_3321_sal_day1_20min_1,
                                        x_3321_sal_day1_20min_3,
                                        x_3321_sal_day1_20min_5,
                                        x_3321_sal_day1_20min_7), axis=0)

# x1 = np.array(cohort3_data25.streams._405A.data[0:8*t_coc])
# y1 = np.array(cohort3_data25.streams._470A.data[0:8*t_coc])
# bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
# fit_line = np.multiply(bls[0],x1)+bls[1]
# x_3336_sal_day1_20min = np.array(stats.zscore((np.array(y1-fit_line)/np.array(fit_line))))
x1 = np.array(cohort3_data25.streams._405A.data[0:2 * t_coc])
y1 = np.array(cohort3_data25.streams._470A.data[0:2 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_3336_sal_day1_20min_1 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort3_data25.streams._405A.data[2 * t_coc + 1:4 * t_coc])
y1 = np.array(cohort3_data25.streams._470A.data[2 * t_coc + 1:4 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_3336_sal_day1_20min_3 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort3_data25.streams._405A.data[4 * t_coc + 1:6 * t_coc])
y1 = np.array(cohort3_data25.streams._470A.data[4 * t_coc + 1:6 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_3336_sal_day1_20min_5 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort3_data25.streams._405A.data[6 * t_coc + 1:8 * t_coc])
y1 = np.array(cohort3_data25.streams._470A.data[6 * t_coc + 1:8 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_3336_sal_day1_20min_7 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x_3336_sal_day1_20min = np.concatenate((x_3336_coc_day3_20min_1,
                                        x_3336_coc_day3_20min_3,
                                        x_3336_coc_day3_20min_5,
                                        x_3336_coc_day3_20min_7), axis=0)

# x1 = np.array(cohort3_data26.streams._405A.data[0:8*t_coc])
# y1 = np.array(cohort3_data26.streams._470A.data[0:8*t_coc])
# bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
# fit_line = np.multiply(bls[0],x1)+bls[1]
# x_3337_sal_day1_20min = np.array(stats.zscore((np.array(y1-fit_line)/np.array(fit_line))))

x1 = np.array(cohort3_data26.streams._405A.data[0:2 * t_coc])
y1 = np.array(cohort3_data26.streams._470A.data[0:2 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_3337_sal_day1_20min_1 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort3_data26.streams._405A.data[2 * t_coc + 1:4 * t_coc])
y1 = np.array(cohort3_data26.streams._470A.data[2 * t_coc + 1:4 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_3337_sal_day1_20min_3 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort3_data26.streams._405A.data[4 * t_coc + 1:6 * t_coc])
y1 = np.array(cohort3_data26.streams._470A.data[4 * t_coc + 1:6 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_3337_sal_day1_20min_5 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort3_data26.streams._405A.data[6 * t_coc + 1:8 * t_coc])
y1 = np.array(cohort3_data26.streams._470A.data[6 * t_coc + 1:8 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_3337_sal_day1_20min_7 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x_3337_sal_day1_20min = np.concatenate((x_3337_sal_day1_20min_1,
                                        x_3337_sal_day1_20min_3,
                                        x_3337_sal_day1_20min_5,
                                        x_3337_sal_day1_20min_7), axis=0)

# x1 = np.array(cohort3_data29.streams._405A.data[0:2*t_coc])
# y1 = np.array(cohort3_data29.streams._470A.data[0:2*t_coc])
# bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
# fit_line = np.multiply(bls[0],x1)+bls[1]
# x_3341_sal_day1_20min_1 = np.array(stats.zscore((np.array(y1-fit_line)/np.array(fit_line))))


x1 = np.array(cohort3_data29.streams._405A.data[0:2 * t_coc])
y1 = np.array(cohort3_data29.streams._470A.data[0:2 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_3341_sal_day1_20min_1 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort3_data29.streams._405A.data[2 * t_coc + 1:4 * t_coc])
y1 = np.array(cohort3_data29.streams._470A.data[2 * t_coc + 1:4 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_3341_sal_day1_20min_3 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort3_data29.streams._405A.data[4 * t_coc + 1:6 * t_coc])
y1 = np.array(cohort3_data29.streams._470A.data[4 * t_coc + 1:6 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_3341_sal_day1_20min_5 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort3_data29.streams._405A.data[6 * t_coc + 1:8 * t_coc])
y1 = np.array(cohort3_data29.streams._470A.data[6 * t_coc + 1:8 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_3341_sal_day1_20min_7 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x_3341_sal_day1_20min = np.concatenate((x_3341_sal_day1_20min_1,
                                        x_3341_sal_day1_20min_3,
                                        x_3341_sal_day1_20min_5,
                                        x_3341_sal_day1_20min_7), axis=0)

x1 = np.array(cohort3_data30.streams._405A.data[0:2 * t_coc])
y1 = np.array(cohort3_data30.streams._470A.data[0:2 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_3346_sal_day1_20min_1 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort3_data30.streams._405A.data[2 * t_coc + 1:4 * t_coc])
y1 = np.array(cohort3_data30.streams._470A.data[2 * t_coc + 1:4 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_3346_sal_day1_20min_3 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort3_data30.streams._405A.data[4 * t_coc + 1:6 * t_coc])
y1 = np.array(cohort3_data30.streams._470A.data[4 * t_coc + 1:6 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_3346_sal_day1_20min_5 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort3_data30.streams._405A.data[6 * t_coc + 1:8 * t_coc])
y1 = np.array(cohort3_data30.streams._470A.data[6 * t_coc + 1:8 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_3346_sal_day1_20min_7 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x_3346_sal_day1_20min = np.concatenate((x_3346_sal_day1_20min_1,
                                        x_3346_sal_day1_20min_3,
                                        x_3346_sal_day1_20min_5,
                                        x_3346_sal_day1_20min_7), axis=0)
# x1 = np.array(cohort3_data30.streams._405A.data[0:8*t_coc])
# y1 = np.array(cohort3_data30.streams._470A.data[0:8*t_coc])
# bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
# fit_line = np.multiply(bls[0],x1)+bls[1]
# x_3346_sal_day1_20min = np.array(stats.zscore((np.array(y1-fit_line)/np.array(fit_line))))


x1 = np.array(cohort3_data34.streams._405A.data[0:2 * t_coc])
y1 = np.array(cohort3_data34.streams._470A.data[0:2 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_3321_sal_day3_20min_1 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))
# x_3321_sal_day3_20min_1[825729:976560] = np.full((150831,),np.mean(x_3321_sal_day3_20min[0:825727],axis=0))


x1 = np.array(cohort3_data34.streams._405A.data[2 * t_coc + 1:4 * t_coc])
y1 = np.array(cohort3_data34.streams._470A.data[2 * t_coc + 1:4 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_3321_sal_day3_20min_3 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))
# x_3321_sal_day3_20min_3[825729:976560] = np.full((150831,),np.mean(x_3321_sal_day3_20min[0:825727],axis=0))


x1 = np.array(cohort3_data34.streams._405A.data[4 * t_coc + 1:6 * t_coc])
y1 = np.array(cohort3_data34.streams._470A.data[4 * t_coc + 1:6 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_3321_sal_day3_20min_5 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))
# x_3321_sal_day3_20min_5[825729:976560] = np.full((150831,),np.mean(x_3321_sal_day3_20min[0:825727],axis=0))


x1 = np.array(cohort3_data34.streams._405A.data[6 * t_coc + 1:7 * t_coc])
y1 = np.array(cohort3_data34.streams._470A.data[6 * t_coc + 1:7 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_3321_sal_day3_20min_7 = np.empty([122069, ])
x_3321_sal_day3_20min_7[0:93307] = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))
x_3321_sal_day3_20min_7[93308:122069] = np.full((28761,), np.mean(np.concatenate((x_3321_sal_day3_20min_1,

                                                                                  x_3321_sal_day3_20min_3,

                                                                                  x_3321_sal_day3_20min_5,

                                                                                  x_3321_sal_day3_20min_7[0:99307]),
                                                                                 axis=0), axis=0))

x_3321_sal_day3_20min_8 = np.empty([122070, ])
# x_3321_sal_day3_20min_8[0:825728] = np.ray(stats.zscore((np.array(y1-fit_line)/np.array(fit_line))))
x_3321_sal_day3_20min_8 = np.full((122070,), np.mean(np.concatenate((x_3321_sal_day3_20min_1,

                                                                     x_3321_sal_day3_20min_3,

                                                                     x_3321_sal_day3_20min_5,

                                                                     x_3321_sal_day3_20min_7[0:99307]), axis=0),
                                                     axis=0))

x_3321_sal_day3_20min = np.concatenate((x_3321_sal_day3_20min_1,
                                        x_3321_sal_day3_20min_3,
                                        x_3321_sal_day3_20min_5,
                                        x_3321_sal_day3_20min_7, x_3321_sal_day3_20min_8), axis=0)

# x1 = np.array(cohort3_data35.streams._405A.data[0:8*t_coc])
# y1 = np.array(cohort3_data35.streams._470A.data[0:8*t_coc])
# bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
# fit_line = np.multiply(bls[0],x1)+bls[1]
# x_3336_sal_day3_20min = np.array(stats.zscore((np.array(y1-fit_line)/np.array(fit_line))))
x1 = np.array(cohort3_data35.streams._405A.data[0:2 * t_coc])
y1 = np.array(cohort3_data35.streams._470A.data[0:2 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_3336_sal_day3_20min_1 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort3_data35.streams._405A.data[2 * t_coc + 1:4 * t_coc])
y1 = np.array(cohort3_data35.streams._470A.data[2 * t_coc + 1:4 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_3336_sal_day3_20min_3 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort3_data35.streams._405A.data[4 * t_coc + 1:6 * t_coc])
y1 = np.array(cohort3_data35.streams._470A.data[4 * t_coc + 1:6 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_3336_sal_day3_20min_5 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort3_data35.streams._405A.data[6 * t_coc + 1:8 * t_coc])
y1 = np.array(cohort3_data35.streams._470A.data[6 * t_coc + 1:8 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_3336_sal_day3_20min_7 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x_3336_sal_day3_20min = np.concatenate((x_3336_sal_day3_20min_1,
                                        x_3336_sal_day3_20min_3,
                                        x_3336_sal_day3_20min_5,
                                        x_3336_sal_day3_20min_7), axis=0)

# x1 = np.array(cohort3_data36.streams._405A.data[0:8*t_coc])
# y1 = np.array(cohort3_data36.streams._470A.data[0:8*t_coc])
# bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
# fit_line = np.multiply(bls[0],x1)+bls[1]
# x_3337_sal_day3_20min = np.array(stats.zscore((np.array(y1-fit_line)/np.array(fit_line))))


x1 = np.array(cohort3_data36.streams._405A.data[0:2 * t_coc])
y1 = np.array(cohort3_data36.streams._470A.data[0:2 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_3337_sal_day3_20min_1 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort3_data36.streams._405A.data[2 * t_coc + 1:4 * t_coc])
y1 = np.array(cohort3_data36.streams._470A.data[2 * t_coc + 1:4 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_3337_sal_day3_20min_3 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort3_data36.streams._405A.data[4 * t_coc + 1:6 * t_coc])
y1 = np.array(cohort3_data36.streams._470A.data[4 * t_coc + 1:6 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_3337_sal_day3_20min_5 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort3_data36.streams._405A.data[6 * t_coc + 1:8 * t_coc])
y1 = np.array(cohort3_data36.streams._470A.data[6 * t_coc + 1:8 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_3337_sal_day3_20min_7 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x_3337_sal_day3_20min = np.concatenate((x_3337_sal_day3_20min_1,
                                        x_3337_sal_day3_20min_3,
                                        x_3337_sal_day3_20min_5,
                                        x_3337_sal_day3_20min_7), axis=0)

# x1 = np.array(cohort3_data39.streams._405A.data[0:8*t_coc])
# y1 = np.array(cohort3_data39.streams._470A.data[0:8*t_coc])
# bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
# fit_line = np.multiply(bls[0],x1)+bls[1]
# x_3341_sal_day3_20min = np.array(stats.zscore((np.array(y1-fit_line)/np.array(fit_line))))

x1 = np.array(cohort3_data39.streams._405A.data[0:2 * t_coc])
y1 = np.array(cohort3_data39.streams._470A.data[0:2 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_3341_sal_day3_20min_1 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort3_data39.streams._405A.data[2 * t_coc + 1:4 * t_coc])
y1 = np.array(cohort3_data39.streams._470A.data[2 * t_coc + 1:4 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_3341_sal_day3_20min_3 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort3_data39.streams._405A.data[4 * t_coc + 1:6 * t_coc])
y1 = np.array(cohort3_data39.streams._470A.data[4 * t_coc + 1:6 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_3341_sal_day3_20min_5 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort3_data39.streams._405A.data[6 * t_coc + 1:8 * t_coc])
y1 = np.array(cohort3_data39.streams._470A.data[6 * t_coc + 1:8 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_3341_sal_day3_20min_7 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x_3341_sal_day3_20min = np.concatenate((x_3341_sal_day3_20min_1,
                                        x_3341_sal_day3_20min_3,
                                        x_3341_sal_day3_20min_5,
                                        x_3341_sal_day3_20min_7), axis=0)

# x1 = np.array(cohort3_data40.streams._405A.data[0:8*t_coc])
# y1 = np.array(cohort3_data40.streams._470A.data[0:8*t_coc])
# bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
# fit_line = np.multiply(bls[0],x1)+bls[1]
# x_3346_sal_day3_20min = np.array(stats.zscore((np.array(y1-fit_line)/np.array(fit_line))))

x1 = np.array(cohort3_data40.streams._405A.data[0:2 * t_coc])
y1 = np.array(cohort3_data40.streams._470A.data[0:2 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_3346_sal_day3_20min_1 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort3_data40.streams._405A.data[2 * t_coc + 1:4 * t_coc])
y1 = np.array(cohort3_data40.streams._470A.data[2 * t_coc + 1:4 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_3346_sal_day3_20min_3 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort3_data40.streams._405A.data[4 * t_coc + 1:6 * t_coc])
y1 = np.array(cohort3_data40.streams._470A.data[4 * t_coc + 1:6 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_3346_sal_day3_20min_5 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort3_data40.streams._405A.data[6 * t_coc + 1:8 * t_coc])
y1 = np.array(cohort3_data40.streams._470A.data[6 * t_coc + 1:8 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_3346_sal_day3_20min_7 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x_3346_sal_day3_20min = np.concatenate((x_3346_sal_day3_20min_1,
                                        x_3346_sal_day3_20min_3,
                                        x_3346_sal_day3_20min_5,
                                        x_3346_sal_day3_20min_7), axis=0)

# In[ ]:


# In[ ]:


# In[ ]:


# In[ ]:


t_coc = 122070

x1 = np.array(cohort2_cocaine_day3_616.streams._405A.data[0:2 * t_coc])
y1 = np.array(cohort2_cocaine_day3_616.streams._470A.data[0:2 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_616_coc_day3_20min_1 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_cocaine_day3_616.streams._405A.data[2 * t_coc + 1:4 * t_coc])
y1 = np.array(cohort2_cocaine_day3_616.streams._470A.data[2 * t_coc + 1:4 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_616_coc_day3_20min_3 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_cocaine_day3_616.streams._405A.data[4 * t_coc + 1:6 * t_coc])
y1 = np.array(cohort2_cocaine_day3_616.streams._470A.data[4 * t_coc + 1:6 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_616_coc_day3_20min_5 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_cocaine_day3_616.streams._405A.data[6 * t_coc + 1:8 * t_coc])
y1 = np.array(cohort2_cocaine_day3_616.streams._470A.data[6 * t_coc + 1:8 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_616_coc_day3_20min_7 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x_616_coc_day3_20min = np.concatenate((x_616_coc_day3_20min_1,
                                       x_616_coc_day3_20min_3,
                                       x_616_coc_day3_20min_5,
                                       x_616_coc_day3_20min_7), axis=0)

x1 = np.array(cohort2_saline_day3_616.streams._405A.data[0:2 * t_coc])
y1 = np.array(cohort2_saline_day3_616.streams._470A.data[0:2 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_616_sal_day3_20min_1 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_saline_day3_616.streams._405A.data[2 * t_coc + 1:4 * t_coc])
y1 = np.array(cohort2_saline_day3_616.streams._470A.data[2 * t_coc + 1:4 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_616_sal_day3_20min_3 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_saline_day3_616.streams._405A.data[4 * t_coc + 1:6 * t_coc])
y1 = np.array(cohort2_saline_day3_616.streams._470A.data[4 * t_coc + 1:6 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_616_sal_day3_20min_5 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_saline_day3_616.streams._405A.data[6 * t_coc + 1:8 * t_coc])
y1 = np.array(cohort2_saline_day3_616.streams._470A.data[6 * t_coc + 1:8 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_616_sal_day3_20min_7 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x_616_sal_day3_20min = np.concatenate((x_616_sal_day3_20min_1,
                                       x_616_sal_day3_20min_3,
                                       x_616_sal_day3_20min_5,
                                       x_616_sal_day3_20min_7), axis=0)

x1 = np.array(cohort2_cocaine_day3_620.streams._405A.data[0:2 * t_coc])
y1 = np.array(cohort2_cocaine_day3_620.streams._470A.data[0:2 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_620_coc_day3_20min_1 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_cocaine_day3_620.streams._405A.data[2 * t_coc + 1:4 * t_coc])
y1 = np.array(cohort2_cocaine_day3_620.streams._470A.data[2 * t_coc + 1:4 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_620_coc_day3_20min_3 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_cocaine_day3_620.streams._405A.data[4 * t_coc + 1:6 * t_coc])
y1 = np.array(cohort2_cocaine_day3_620.streams._470A.data[4 * t_coc + 1:6 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_620_coc_day3_20min_5 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_cocaine_day3_620.streams._405A.data[6 * t_coc + 1:8 * t_coc])
y1 = np.array(cohort2_cocaine_day3_620.streams._470A.data[6 * t_coc + 1:8 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_620_coc_day3_20min_7 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x_620_coc_day3_20min = np.concatenate((x_620_coc_day3_20min_1,
                                       x_620_coc_day3_20min_3,
                                       x_620_coc_day3_20min_5,
                                       x_620_coc_day3_20min_7), axis=0)

x1 = np.array(cohort2_saline_day3_620.streams._405A.data[0:2 * t_coc])
y1 = np.array(cohort2_saline_day3_620.streams._470A.data[0:2 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_620_sal_day3_20min_1 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_saline_day3_620.streams._405A.data[2 * t_coc + 1:4 * t_coc])
y1 = np.array(cohort2_saline_day3_620.streams._470A.data[2 * t_coc + 1:4 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_620_sal_day3_20min_3 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_saline_day3_620.streams._405A.data[4 * t_coc + 1:6 * t_coc])
y1 = np.array(cohort2_saline_day3_620.streams._470A.data[4 * t_coc + 1:6 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_620_sal_day3_20min_5 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_saline_day3_620.streams._405A.data[6 * t_coc + 1:8 * t_coc])
y1 = np.array(cohort2_saline_day3_620.streams._470A.data[6 * t_coc + 1:8 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_620_sal_day3_20min_7 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x_620_sal_day3_20min = np.concatenate((x_620_sal_day3_20min_1,
                                       x_620_sal_day3_20min_3,
                                       x_620_sal_day3_20min_5,
                                       x_620_sal_day3_20min_7), axis=0)

x1 = np.array(cohort2_cocaine_day3_621.streams._405A.data[0:2 * t_coc])
y1 = np.array(cohort2_cocaine_day3_621.streams._470A.data[0:2 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_621_coc_day3_20min_1 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_cocaine_day3_621.streams._405A.data[2 * t_coc + 1:4 * t_coc])
y1 = np.array(cohort2_cocaine_day3_621.streams._470A.data[2 * t_coc + 1:4 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_621_coc_day3_20min_3 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_cocaine_day3_621.streams._405A.data[4 * t_coc + 1:6 * t_coc])
y1 = np.array(cohort2_cocaine_day3_621.streams._470A.data[4 * t_coc + 1:6 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_621_coc_day3_20min_5 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_cocaine_day3_621.streams._405A.data[6 * t_coc + 1:8 * t_coc])
y1 = np.array(cohort2_cocaine_day3_621.streams._470A.data[6 * t_coc + 1:8 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_621_coc_day3_20min_7 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x_621_coc_day3_20min = np.concatenate((x_621_coc_day3_20min_1,
                                       x_621_coc_day3_20min_3,
                                       x_621_coc_day3_20min_5,
                                       x_621_coc_day3_20min_7), axis=0)

x1 = np.array(cohort2_saline_day3_621.streams._405A.data[0:2 * t_coc])
y1 = np.array(cohort2_saline_day3_621.streams._470A.data[0:2 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_621_sal_day3_20min_1 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_saline_day3_621.streams._405A.data[2 * t_coc + 1:4 * t_coc])
y1 = np.array(cohort2_saline_day3_621.streams._470A.data[2 * t_coc + 1:4 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_621_sal_day3_20min_3 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_saline_day3_621.streams._405A.data[4 * t_coc + 1:6 * t_coc])
y1 = np.array(cohort2_saline_day3_621.streams._470A.data[4 * t_coc + 1:6 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_621_sal_day3_20min_5 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_saline_day3_621.streams._405A.data[6 * t_coc + 1:8 * t_coc])
y1 = np.array(cohort2_saline_day3_621.streams._470A.data[6 * t_coc + 1:8 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_621_sal_day3_20min_7 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x_621_sal_day3_20min = np.concatenate((x_621_sal_day3_20min_1,
                                       x_621_sal_day3_20min_3,
                                       x_621_sal_day3_20min_5,
                                       x_621_sal_day3_20min_7), axis=0)

x1 = np.array(cohort2_cocaine_day3_628.streams._405A.data[0:2 * t_coc])
y1 = np.array(cohort2_cocaine_day3_628.streams._470A.data[0:2 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_628_coc_day3_20min_1 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_cocaine_day3_628.streams._405A.data[2 * t_coc + 1:4 * t_coc])
y1 = np.array(cohort2_cocaine_day3_628.streams._470A.data[2 * t_coc + 1:4 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_628_coc_day3_20min_3 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_cocaine_day3_628.streams._405A.data[4 * t_coc + 1:6 * t_coc])
y1 = np.array(cohort2_cocaine_day3_628.streams._470A.data[4 * t_coc + 1:6 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_628_coc_day3_20min_5 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_cocaine_day3_628.streams._405A.data[6 * t_coc + 1:8 * t_coc])
y1 = np.array(cohort2_cocaine_day3_628.streams._470A.data[6 * t_coc + 1:8 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_628_coc_day3_20min_7 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x_628_coc_day3_20min = np.concatenate((x_628_coc_day3_20min_1,
                                       x_628_coc_day3_20min_3,
                                       x_628_coc_day3_20min_5,
                                       x_628_coc_day3_20min_7), axis=0)

x1 = np.array(cohort2_saline_day3_628.streams._405A.data[0:2 * t_coc])
y1 = np.array(cohort2_saline_day3_628.streams._470A.data[0:2 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_628_sal_day3_20min_1 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_saline_day3_628.streams._405A.data[2 * t_coc + 1:4 * t_coc])
y1 = np.array(cohort2_saline_day3_628.streams._470A.data[2 * t_coc + 1:4 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_628_sal_day3_20min_3 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_saline_day3_628.streams._405A.data[4 * t_coc + 1:6 * t_coc])
y1 = np.array(cohort2_saline_day3_628.streams._470A.data[4 * t_coc + 1:6 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_628_sal_day3_20min_5 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_saline_day3_628.streams._405A.data[6 * t_coc + 1:8 * t_coc])
y1 = np.array(cohort2_saline_day3_628.streams._470A.data[6 * t_coc + 1:8 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_628_sal_day3_20min_7 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x_628_sal_day3_20min = np.concatenate((x_628_sal_day3_20min_1,
                                       x_628_sal_day3_20min_3,
                                       x_628_sal_day3_20min_5,
                                       x_628_sal_day3_20min_7), axis=0)

x1 = np.array(cohort2_cocaine_day3_638.streams._405A.data[0:2 * t_coc])
y1 = np.array(cohort2_cocaine_day3_638.streams._470A.data[0:2 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_638_coc_day3_20min_1 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_cocaine_day3_638.streams._405A.data[2 * t_coc + 1:4 * t_coc])
y1 = np.array(cohort2_cocaine_day3_638.streams._470A.data[2 * t_coc + 1:4 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_638_coc_day3_20min_3 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_cocaine_day3_638.streams._405A.data[4 * t_coc + 1:6 * t_coc])
y1 = np.array(cohort2_cocaine_day3_638.streams._470A.data[4 * t_coc + 1:6 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_638_coc_day3_20min_5 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_cocaine_day3_638.streams._405A.data[6 * t_coc + 1:8 * t_coc])
y1 = np.array(cohort2_cocaine_day3_638.streams._470A.data[6 * t_coc + 1:8 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_638_coc_day3_20min_7 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x_638_coc_day3_20min = np.concatenate((x_638_coc_day3_20min_1,
                                       x_638_coc_day3_20min_3,
                                       x_638_coc_day3_20min_5,
                                       x_638_coc_day3_20min_7), axis=0)

x1 = np.array(cohort2_saline_day3_638.streams._405A.data[0:2 * t_coc])
y1 = np.array(cohort2_saline_day3_638.streams._470A.data[0:2 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_638_sal_day3_20min_1 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_saline_day3_638.streams._405A.data[2 * t_coc + 1:4 * t_coc])
y1 = np.array(cohort2_saline_day3_638.streams._470A.data[2 * t_coc + 1:4 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_638_sal_day3_20min_3 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_saline_day3_638.streams._405A.data[4 * t_coc + 1:6 * t_coc])
y1 = np.array(cohort2_saline_day3_638.streams._470A.data[4 * t_coc + 1:6 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_638_sal_day3_20min_5 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_saline_day3_638.streams._405A.data[6 * t_coc + 1:8 * t_coc])
y1 = np.array(cohort2_saline_day3_638.streams._470A.data[6 * t_coc + 1:8 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_638_sal_day3_20min_7 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x_638_sal_day3_20min = np.concatenate((x_638_sal_day3_20min_1,
                                       x_638_sal_day3_20min_3,
                                       x_638_sal_day3_20min_5,
                                       x_638_sal_day3_20min_7), axis=0)

x1 = np.array(cohort2_cocaine_day3_641.streams._405A.data[0:2 * t_coc])
y1 = np.array(cohort2_cocaine_day3_641.streams._470A.data[0:2 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_641_coc_day3_20min_1 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_cocaine_day3_641.streams._405A.data[2 * t_coc + 1:4 * t_coc])
y1 = np.array(cohort2_cocaine_day3_641.streams._470A.data[2 * t_coc + 1:4 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_641_coc_day3_20min_3 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_cocaine_day3_641.streams._405A.data[4 * t_coc + 1:6 * t_coc])
y1 = np.array(cohort2_cocaine_day3_641.streams._470A.data[4 * t_coc + 1:6 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_641_coc_day3_20min_5 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_cocaine_day3_641.streams._405A.data[6 * t_coc + 1:8 * t_coc])
y1 = np.array(cohort2_cocaine_day3_641.streams._470A.data[6 * t_coc + 1:8 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_641_coc_day3_20min_7 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x_641_coc_day3_20min = np.concatenate((x_641_coc_day3_20min_1,
                                       x_641_coc_day3_20min_3,
                                       x_641_coc_day3_20min_5,
                                       x_641_coc_day3_20min_7), axis=0)

x1 = np.array(cohort2_saline_day3_641.streams._405A.data[0:2 * t_coc])
y1 = np.array(cohort2_saline_day3_641.streams._470A.data[0:2 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_641_sal_day3_20min_1 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_saline_day3_641.streams._405A.data[2 * t_coc + 1:4 * t_coc])
y1 = np.array(cohort2_saline_day3_641.streams._470A.data[2 * t_coc + 1:4 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_641_sal_day3_20min_3 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_saline_day3_641.streams._405A.data[4 * t_coc + 1:6 * t_coc])
y1 = np.array(cohort2_saline_day3_641.streams._470A.data[4 * t_coc + 1:6 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_641_sal_day3_20min_5 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_saline_day3_641.streams._405A.data[6 * t_coc + 1:8 * t_coc])
y1 = np.array(cohort2_saline_day3_641.streams._470A.data[6 * t_coc + 1:8 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_641_sal_day3_20min_7 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x_641_sal_day3_20min = np.concatenate((x_641_sal_day3_20min_1,
                                       x_641_sal_day3_20min_3,
                                       x_641_sal_day3_20min_5,
                                       x_641_sal_day3_20min_7), axis=0)

x1 = np.array(cohort2_cocaine_day3_642.streams._405A.data[0:2 * t_coc])
y1 = np.array(cohort2_cocaine_day3_642.streams._470A.data[0:2 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_642_coc_day3_20min_1 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_cocaine_day3_642.streams._405A.data[2 * t_coc + 1:4 * t_coc])
y1 = np.array(cohort2_cocaine_day3_642.streams._470A.data[2 * t_coc + 1:4 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_642_coc_day3_20min_3 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_cocaine_day3_642.streams._405A.data[4 * t_coc + 1:6 * t_coc])
y1 = np.array(cohort2_cocaine_day3_642.streams._470A.data[4 * t_coc + 1:6 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_642_coc_day3_20min_5 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_cocaine_day3_642.streams._405A.data[6 * t_coc + 1:8 * t_coc])
y1 = np.array(cohort2_cocaine_day3_642.streams._470A.data[6 * t_coc + 1:8 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_642_coc_day3_20min_7 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x_642_coc_day3_20min = np.concatenate((x_642_coc_day3_20min_1,
                                       x_642_coc_day3_20min_3,
                                       x_642_coc_day3_20min_5,
                                       x_642_coc_day3_20min_7), axis=0)

x1 = np.array(cohort2_saline_day3_642.streams._405A.data[0:2 * t_coc])
y1 = np.array(cohort2_saline_day3_642.streams._470A.data[0:2 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_642_sal_day3_20min_1 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_saline_day3_642.streams._405A.data[2 * t_coc + 1:4 * t_coc])
y1 = np.array(cohort2_saline_day3_642.streams._470A.data[2 * t_coc + 1:4 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_642_sal_day3_20min_3 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_saline_day3_642.streams._405A.data[4 * t_coc + 1:6 * t_coc])
y1 = np.array(cohort2_saline_day3_642.streams._470A.data[4 * t_coc + 1:6 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_642_sal_day3_20min_5 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_saline_day3_642.streams._405A.data[6 * t_coc + 1:8 * t_coc])
y1 = np.array(cohort2_saline_day3_642.streams._470A.data[6 * t_coc + 1:8 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_642_sal_day3_20min_7 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x_642_sal_day3_20min = np.concatenate((x_642_sal_day3_20min_1,
                                       x_642_sal_day3_20min_3,
                                       x_642_sal_day3_20min_5,
                                       x_642_sal_day3_20min_7), axis=0)

x1 = np.array(cohort2_cocaine_day3_657.streams._405A.data[0:2 * t_coc])
y1 = np.array(cohort2_cocaine_day3_657.streams._470A.data[0:2 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_657_coc_day3_20min_1 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_cocaine_day3_657.streams._405A.data[2 * t_coc + 1:4 * t_coc])
y1 = np.array(cohort2_cocaine_day3_657.streams._470A.data[2 * t_coc + 1:4 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_657_coc_day3_20min_3 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_cocaine_day3_657.streams._405A.data[4 * t_coc + 1:6 * t_coc])
y1 = np.array(cohort2_cocaine_day3_657.streams._470A.data[4 * t_coc + 1:6 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_657_coc_day3_20min_5 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_cocaine_day3_657.streams._405A.data[6 * t_coc + 1:8 * t_coc])
y1 = np.array(cohort2_cocaine_day3_657.streams._470A.data[6 * t_coc + 1:8 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_657_coc_day3_20min_7 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x_657_coc_day3_20min = np.concatenate((x_657_coc_day3_20min_1,
                                       x_657_coc_day3_20min_3,
                                       x_657_coc_day3_20min_5,
                                       x_657_coc_day3_20min_7), axis=0)

x1 = np.array(cohort2_saline_day3_657.streams._405A.data[0:2 * t_coc])
y1 = np.array(cohort2_saline_day3_657.streams._470A.data[0:2 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_657_sal_day3_20min_1 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_saline_day3_657.streams._405A.data[2 * t_coc + 1:4 * t_coc])
y1 = np.array(cohort2_saline_day3_657.streams._470A.data[2 * t_coc + 1:4 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_657_sal_day3_20min_3 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_saline_day3_657.streams._405A.data[4 * t_coc + 1:6 * t_coc])
y1 = np.array(cohort2_saline_day3_657.streams._470A.data[4 * t_coc + 1:6 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_657_sal_day3_20min_5 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_saline_day3_657.streams._405A.data[6 * t_coc + 1:8 * t_coc])
y1 = np.array(cohort2_saline_day3_657.streams._470A.data[6 * t_coc + 1:8 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_657_sal_day3_20min_7 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x_657_sal_day3_20min = np.concatenate((x_657_sal_day3_20min_1,
                                       x_657_sal_day3_20min_3,
                                       x_657_sal_day3_20min_5,
                                       x_657_sal_day3_20min_7), axis=0)

x1 = np.array(cohort2_cocaine_day3_660.streams._405A.data[0:2 * t_coc])
y1 = np.array(cohort2_cocaine_day3_660.streams._470A.data[0:2 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_660_coc_day3_20min_1 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_cocaine_day3_660.streams._405A.data[2 * t_coc + 1:4 * t_coc])
y1 = np.array(cohort2_cocaine_day3_660.streams._470A.data[2 * t_coc + 1:4 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_660_coc_day3_20min_3 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_cocaine_day3_660.streams._405A.data[4 * t_coc + 1:6 * t_coc])
y1 = np.array(cohort2_cocaine_day3_660.streams._470A.data[4 * t_coc + 1:6 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_660_coc_day3_20min_5 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_cocaine_day3_660.streams._405A.data[6 * t_coc + 1:8 * t_coc])
y1 = np.array(cohort2_cocaine_day3_660.streams._470A.data[6 * t_coc + 1:8 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_660_coc_day3_20min_7 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x_660_coc_day3_20min = np.concatenate((x_660_coc_day3_20min_1,
                                       x_660_coc_day3_20min_3,
                                       x_660_coc_day3_20min_5,
                                       x_660_coc_day3_20min_7), axis=0)

x1 = np.array(cohort2_saline_day3_660.streams._405A.data[0:2 * t_coc])
y1 = np.array(cohort2_saline_day3_660.streams._470A.data[0:2 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_660_sal_day3_20min_1 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_saline_day3_660.streams._405A.data[2 * t_coc + 1:4 * t_coc])
y1 = np.array(cohort2_saline_day3_660.streams._470A.data[2 * t_coc + 1:4 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_660_sal_day3_20min_3 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_saline_day3_660.streams._405A.data[4 * t_coc + 1:6 * t_coc])
y1 = np.array(cohort2_saline_day3_660.streams._470A.data[4 * t_coc + 1:6 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_660_sal_day3_20min_5 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_saline_day3_660.streams._405A.data[6 * t_coc + 1:8 * t_coc])
y1 = np.array(cohort2_saline_day3_660.streams._470A.data[6 * t_coc + 1:8 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_660_sal_day3_20min_7 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x_660_sal_day3_20min = np.concatenate((x_660_sal_day3_20min_1,
                                       x_660_sal_day3_20min_3,
                                       x_660_sal_day3_20min_5,
                                       x_660_sal_day3_20min_7), axis=0)

x1 = np.array(cohort2_cocaine_day3_674.streams._405A.data[0:2 * t_coc])
y1 = np.array(cohort2_cocaine_day3_674.streams._470A.data[0:2 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_674_coc_day3_20min_1 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_cocaine_day3_674.streams._405A.data[2 * t_coc + 1:4 * t_coc])
y1 = np.array(cohort2_cocaine_day3_674.streams._470A.data[2 * t_coc + 1:4 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_674_coc_day3_20min_3 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_cocaine_day3_674.streams._405A.data[4 * t_coc + 1:6 * t_coc])
y1 = np.array(cohort2_cocaine_day3_674.streams._470A.data[4 * t_coc + 1:6 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_674_coc_day3_20min_5 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_cocaine_day3_674.streams._405A.data[6 * t_coc + 1:8 * t_coc])
y1 = np.array(cohort2_cocaine_day3_674.streams._470A.data[6 * t_coc + 1:8 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_674_coc_day3_20min_7 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x_674_coc_day3_20min = np.concatenate((x_674_coc_day3_20min_1,
                                       x_674_coc_day3_20min_3,
                                       x_674_coc_day3_20min_5,
                                       x_674_coc_day3_20min_7), axis=0)

x1 = np.array(cohort2_saline_day3_674.streams._405A.data[0:2 * t_coc])
y1 = np.array(cohort2_saline_day3_674.streams._470A.data[0:2 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_674_sal_day3_20min_1 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_saline_day3_674.streams._405A.data[2 * t_coc + 1:4 * t_coc])
y1 = np.array(cohort2_saline_day3_674.streams._470A.data[2 * t_coc + 1:4 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_674_sal_day3_20min_3 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_saline_day3_674.streams._405A.data[4 * t_coc + 1:6 * t_coc])
y1 = np.array(cohort2_saline_day3_674.streams._470A.data[4 * t_coc + 1:6 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_674_sal_day3_20min_5 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_saline_day3_674.streams._405A.data[6 * t_coc + 1:8 * t_coc])
y1 = np.array(cohort2_saline_day3_674.streams._470A.data[6 * t_coc + 1:8 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_674_sal_day3_20min_7 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x_674_sal_day3_20min = np.concatenate((x_674_sal_day3_20min_1,
                                       x_674_sal_day3_20min_3,
                                       x_674_sal_day3_20min_5,
                                       x_674_sal_day3_20min_7), axis=0)

x1 = np.array(cohort2_cocaine_day3_675.streams._405A.data[0:2 * t_coc])
y1 = np.array(cohort2_cocaine_day3_675.streams._470A.data[0:2 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_675_coc_day3_20min_1 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_cocaine_day3_675.streams._405A.data[2 * t_coc + 1:4 * t_coc])
y1 = np.array(cohort2_cocaine_day3_675.streams._470A.data[2 * t_coc + 1:4 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_675_coc_day3_20min_3 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_cocaine_day3_675.streams._405A.data[4 * t_coc + 1:6 * t_coc])
y1 = np.array(cohort2_cocaine_day3_675.streams._470A.data[4 * t_coc + 1:6 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_675_coc_day3_20min_5 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_cocaine_day3_675.streams._405A.data[6 * t_coc + 1:8 * t_coc])
y1 = np.array(cohort2_cocaine_day3_675.streams._470A.data[6 * t_coc + 1:8 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_675_coc_day3_20min_7 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x_675_coc_day3_20min = np.concatenate((x_675_coc_day3_20min_1,
                                       x_675_coc_day3_20min_3,
                                       x_675_coc_day3_20min_5,
                                       x_675_coc_day3_20min_7), axis=0)

x1 = np.array(cohort2_saline_day3_675.streams._405A.data[0:2 * t_coc])
y1 = np.array(cohort2_saline_day3_675.streams._470A.data[0:2 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_675_sal_day3_20min_1 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_saline_day3_675.streams._405A.data[2 * t_coc + 1:4 * t_coc])
y1 = np.array(cohort2_saline_day3_675.streams._470A.data[2 * t_coc + 1:4 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_675_sal_day3_20min_3 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_saline_day3_675.streams._405A.data[4 * t_coc + 1:6 * t_coc])
y1 = np.array(cohort2_saline_day3_675.streams._470A.data[4 * t_coc + 1:6 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_675_sal_day3_20min_5 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_saline_day3_675.streams._405A.data[6 * t_coc + 1:8 * t_coc])
y1 = np.array(cohort2_saline_day3_675.streams._470A.data[6 * t_coc + 1:8 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_675_sal_day3_20min_7 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x_675_sal_day3_20min = np.concatenate((x_675_sal_day3_20min_1,
                                       x_675_sal_day3_20min_3,
                                       x_675_sal_day3_20min_5,
                                       x_675_sal_day3_20min_7), axis=0)

x1 = np.array(cohort2_cocaine_day1_616.streams._405A.data[0:2 * t_coc])
y1 = np.array(cohort2_cocaine_day1_616.streams._470A.data[0:2 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_616_coc_day1_20min_1 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_cocaine_day1_616.streams._405A.data[2 * t_coc + 1:4 * t_coc])
y1 = np.array(cohort2_cocaine_day1_616.streams._470A.data[2 * t_coc + 1:4 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_616_coc_day1_20min_3 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_cocaine_day1_616.streams._405A.data[4 * t_coc + 1:6 * t_coc])
y1 = np.array(cohort2_cocaine_day1_616.streams._470A.data[4 * t_coc + 1:6 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_616_coc_day1_20min_5 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_cocaine_day1_616.streams._405A.data[6 * t_coc + 1:8 * t_coc])
y1 = np.array(cohort2_cocaine_day1_616.streams._470A.data[6 * t_coc + 1:8 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_616_coc_day1_20min_7 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x_616_coc_day1_20min = np.concatenate((x_616_coc_day1_20min_1,
                                       x_616_coc_day1_20min_3,
                                       x_616_coc_day1_20min_5,
                                       x_616_coc_day1_20min_7), axis=0)

x1 = np.array(cohort2_saline_day1_616.streams._405A.data[0:2 * t_coc])
y1 = np.array(cohort2_saline_day1_616.streams._470A.data[0:2 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_616_sal_day1_20min_1 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_saline_day1_616.streams._405A.data[2 * t_coc + 1:4 * t_coc])
y1 = np.array(cohort2_saline_day1_616.streams._470A.data[2 * t_coc + 1:4 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_616_sal_day1_20min_3 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_saline_day1_616.streams._405A.data[4 * t_coc + 1:6 * t_coc])
y1 = np.array(cohort2_saline_day1_616.streams._470A.data[4 * t_coc + 1:6 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_616_sal_day1_20min_5 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_saline_day1_616.streams._405A.data[6 * t_coc + 1:8 * t_coc])
y1 = np.array(cohort2_saline_day1_616.streams._470A.data[6 * t_coc + 1:8 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_616_sal_day1_20min_7 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x_616_sal_day1_20min = np.concatenate((x_616_sal_day1_20min_1,
                                       x_616_sal_day1_20min_3,
                                       x_616_sal_day1_20min_5,
                                       x_616_sal_day1_20min_7), axis=0)

x1 = np.array(cohort2_cocaine_day1_620.streams._405A.data[0:2 * t_coc])
y1 = np.array(cohort2_cocaine_day1_620.streams._470A.data[0:2 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_620_coc_day1_20min_1 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_cocaine_day1_620.streams._405A.data[2 * t_coc + 1:4 * t_coc])
y1 = np.array(cohort2_cocaine_day1_620.streams._470A.data[2 * t_coc + 1:4 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_620_coc_day1_20min_3 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_cocaine_day1_620.streams._405A.data[4 * t_coc + 1:6 * t_coc])
y1 = np.array(cohort2_cocaine_day1_620.streams._470A.data[4 * t_coc + 1:6 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_620_coc_day1_20min_5 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_cocaine_day1_620.streams._405A.data[6 * t_coc + 1:8 * t_coc])
y1 = np.array(cohort2_cocaine_day1_620.streams._470A.data[6 * t_coc + 1:8 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_620_coc_day1_20min_7 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x_620_coc_day1_20min = np.concatenate((x_620_coc_day1_20min_1,
                                       x_620_coc_day1_20min_3,
                                       x_620_coc_day1_20min_5,
                                       x_620_coc_day1_20min_7), axis=0)

x1 = np.array(cohort2_saline_day1_620.streams._405A.data[0:2 * t_coc])
y1 = np.array(cohort2_saline_day1_620.streams._470A.data[0:2 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_620_sal_day1_20min_1 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_saline_day1_620.streams._405A.data[2 * t_coc + 1:4 * t_coc])
y1 = np.array(cohort2_saline_day1_620.streams._470A.data[2 * t_coc + 1:4 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_620_sal_day1_20min_3 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_saline_day1_620.streams._405A.data[4 * t_coc + 1:6 * t_coc])
y1 = np.array(cohort2_saline_day1_620.streams._470A.data[4 * t_coc + 1:6 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_620_sal_day1_20min_5 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_saline_day1_620.streams._405A.data[6 * t_coc + 1:8 * t_coc])
y1 = np.array(cohort2_saline_day1_620.streams._470A.data[6 * t_coc + 1:8 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_620_sal_day1_20min_7 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x_620_sal_day1_20min = np.concatenate((x_620_sal_day1_20min_1,
                                       x_620_sal_day1_20min_3,
                                       x_620_sal_day1_20min_5,
                                       x_620_sal_day1_20min_7), axis=0)

x1 = np.array(cohort2_cocaine_day1_621.streams._405A.data[0:2 * t_coc])
y1 = np.array(cohort2_cocaine_day1_621.streams._470A.data[0:2 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_621_coc_day1_20min_1 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_cocaine_day1_621.streams._405A.data[2 * t_coc + 1:4 * t_coc])
y1 = np.array(cohort2_cocaine_day1_621.streams._470A.data[2 * t_coc + 1:4 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_621_coc_day1_20min_3 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_cocaine_day1_621.streams._405A.data[4 * t_coc + 1:6 * t_coc])
y1 = np.array(cohort2_cocaine_day1_621.streams._470A.data[4 * t_coc + 1:6 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_621_coc_day1_20min_5 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_cocaine_day1_621.streams._405A.data[6 * t_coc + 1:8 * t_coc])
y1 = np.array(cohort2_cocaine_day1_621.streams._470A.data[6 * t_coc + 1:8 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_621_coc_day1_20min_7 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x_621_coc_day1_20min = np.concatenate((x_621_coc_day1_20min_1,
                                       x_621_coc_day1_20min_3,
                                       x_621_coc_day1_20min_5,
                                       x_621_coc_day1_20min_7), axis=0)

x1 = np.array(cohort2_saline_day1_621.streams._405A.data[0:2 * t_coc])
y1 = np.array(cohort2_saline_day1_621.streams._470A.data[0:2 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_621_sal_day1_20min_1 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_saline_day1_621.streams._405A.data[2 * t_coc + 1:4 * t_coc])
y1 = np.array(cohort2_saline_day1_621.streams._470A.data[2 * t_coc + 1:4 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_621_sal_day1_20min_3 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_saline_day1_621.streams._405A.data[4 * t_coc + 1:6 * t_coc])
y1 = np.array(cohort2_saline_day1_621.streams._470A.data[4 * t_coc + 1:6 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_621_sal_day1_20min_5 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_saline_day1_621.streams._405A.data[6 * t_coc + 1:8 * t_coc])
y1 = np.array(cohort2_saline_day1_621.streams._470A.data[6 * t_coc + 1:8 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_621_sal_day1_20min_7 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x_621_sal_day1_20min = np.concatenate((x_621_sal_day1_20min_1,
                                       x_621_sal_day1_20min_3,
                                       x_621_sal_day1_20min_5,
                                       x_621_sal_day1_20min_7), axis=0)

x1 = np.array(cohort2_cocaine_day1_628.streams._405A.data[0:2 * t_coc])
y1 = np.array(cohort2_cocaine_day1_628.streams._470A.data[0:2 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_628_coc_day1_20min_1 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_cocaine_day1_628.streams._405A.data[2 * t_coc + 1:4 * t_coc])
y1 = np.array(cohort2_cocaine_day1_628.streams._470A.data[2 * t_coc + 1:4 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_628_coc_day1_20min_3 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_cocaine_day1_628.streams._405A.data[4 * t_coc + 1:6 * t_coc])
y1 = np.array(cohort2_cocaine_day1_628.streams._470A.data[4 * t_coc + 1:6 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_628_coc_day1_20min_5 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_cocaine_day1_628.streams._405A.data[6 * t_coc + 1:8 * t_coc])
y1 = np.array(cohort2_cocaine_day1_628.streams._470A.data[6 * t_coc + 1:8 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_628_coc_day1_20min_7 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x_628_coc_day1_20min = np.concatenate((x_628_coc_day1_20min_1,
                                       x_628_coc_day1_20min_3,
                                       x_628_coc_day1_20min_5,
                                       x_628_coc_day1_20min_7), axis=0)

x1 = np.array(cohort2_saline_day1_628.streams._405A.data[0:2 * t_coc])
y1 = np.array(cohort2_saline_day1_628.streams._470A.data[0:2 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_628_sal_day1_20min_1 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_saline_day1_628.streams._405A.data[2 * t_coc + 1:4 * t_coc])
y1 = np.array(cohort2_saline_day1_628.streams._470A.data[2 * t_coc + 1:4 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_628_sal_day1_20min_3 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_saline_day1_628.streams._405A.data[4 * t_coc + 1:6 * t_coc])
y1 = np.array(cohort2_saline_day1_628.streams._470A.data[4 * t_coc + 1:6 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_628_sal_day1_20min_5 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_saline_day1_628.streams._405A.data[6 * t_coc + 1:8 * t_coc])
y1 = np.array(cohort2_saline_day1_628.streams._470A.data[6 * t_coc + 1:8 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_628_sal_day1_20min_7 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x_628_sal_day1_20min = np.concatenate((x_628_sal_day1_20min_1,
                                       x_628_sal_day1_20min_3,
                                       x_628_sal_day1_20min_5,
                                       x_628_sal_day1_20min_7), axis=0)

x1 = np.array(cohort2_cocaine_day1_638.streams._405A.data[0:2 * t_coc])
y1 = np.array(cohort2_cocaine_day1_638.streams._470A.data[0:2 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_638_coc_day1_20min_1 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_cocaine_day1_638.streams._405A.data[2 * t_coc + 1:4 * t_coc])
y1 = np.array(cohort2_cocaine_day1_638.streams._470A.data[2 * t_coc + 1:4 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_638_coc_day1_20min_3 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_cocaine_day1_638.streams._405A.data[4 * t_coc + 1:6 * t_coc])
y1 = np.array(cohort2_cocaine_day1_638.streams._470A.data[4 * t_coc + 1:6 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_638_coc_day1_20min_5 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_cocaine_day1_638.streams._405A.data[6 * t_coc + 1:8 * t_coc])
y1 = np.array(cohort2_cocaine_day1_638.streams._470A.data[6 * t_coc + 1:8 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_638_coc_day1_20min_7 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x_638_coc_day1_20min = np.concatenate((x_638_coc_day1_20min_1,
                                       x_638_coc_day1_20min_3,
                                       x_638_coc_day1_20min_5,
                                       x_638_coc_day1_20min_7), axis=0)

x1 = np.array(cohort2_saline_day1_638.streams._405A.data[0:2 * t_coc])
y1 = np.array(cohort2_saline_day1_638.streams._470A.data[0:2 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_638_sal_day1_20min_1 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_saline_day1_638.streams._405A.data[2 * t_coc + 1:4 * t_coc])
y1 = np.array(cohort2_saline_day1_638.streams._470A.data[2 * t_coc + 1:4 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_638_sal_day1_20min_3 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_saline_day1_638.streams._405A.data[4 * t_coc + 1:6 * t_coc])
y1 = np.array(cohort2_saline_day1_638.streams._470A.data[4 * t_coc + 1:6 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_638_sal_day1_20min_5 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_saline_day1_638.streams._405A.data[6 * t_coc + 1:8 * t_coc])
y1 = np.array(cohort2_saline_day1_638.streams._470A.data[6 * t_coc + 1:8 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_638_sal_day1_20min_7 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x_638_sal_day1_20min = np.concatenate((x_638_sal_day1_20min_1,
                                       x_638_sal_day1_20min_3,
                                       x_638_sal_day1_20min_5,
                                       x_638_sal_day1_20min_7), axis=0)

x1 = np.array(cohort2_cocaine_day1_641.streams._405A.data[0:2 * t_coc])
y1 = np.array(cohort2_cocaine_day1_641.streams._470A.data[0:2 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_641_coc_day1_20min_1 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_cocaine_day1_641.streams._405A.data[2 * t_coc + 1:4 * t_coc])
y1 = np.array(cohort2_cocaine_day1_641.streams._470A.data[2 * t_coc + 1:4 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_641_coc_day1_20min_3 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_cocaine_day1_641.streams._405A.data[4 * t_coc + 1:6 * t_coc])
y1 = np.array(cohort2_cocaine_day1_641.streams._470A.data[4 * t_coc + 1:6 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_641_coc_day1_20min_5 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_cocaine_day1_641.streams._405A.data[6 * t_coc + 1:8 * t_coc])
y1 = np.array(cohort2_cocaine_day1_641.streams._470A.data[6 * t_coc + 1:8 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_641_coc_day1_20min_7 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x_641_coc_day1_20min = np.concatenate((x_641_coc_day1_20min_1,
                                       x_641_coc_day1_20min_3,
                                       x_641_coc_day1_20min_5,
                                       x_641_coc_day1_20min_7), axis=0)

x1 = np.array(cohort2_saline_day1_641.streams._405A.data[0:2 * t_coc])
y1 = np.array(cohort2_saline_day1_641.streams._470A.data[0:2 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_641_sal_day1_20min_1 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_saline_day1_641.streams._405A.data[2 * t_coc + 1:4 * t_coc])
y1 = np.array(cohort2_saline_day1_641.streams._470A.data[2 * t_coc + 1:4 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_641_sal_day1_20min_3 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_saline_day1_641.streams._405A.data[4 * t_coc + 1:6 * t_coc])
y1 = np.array(cohort2_saline_day1_641.streams._470A.data[4 * t_coc + 1:6 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_641_sal_day1_20min_5 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_saline_day1_641.streams._405A.data[6 * t_coc + 1:8 * t_coc])
y1 = np.array(cohort2_saline_day1_641.streams._470A.data[6 * t_coc + 1:8 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_641_sal_day1_20min_7 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x_641_sal_day1_20min = np.concatenate((x_641_sal_day1_20min_1,
                                       x_641_sal_day1_20min_3,
                                       x_641_sal_day1_20min_5,
                                       x_641_sal_day1_20min_7), axis=0)

x1 = np.array(cohort2_cocaine_day1_642.streams._405A.data[0:2 * t_coc])
y1 = np.array(cohort2_cocaine_day1_642.streams._470A.data[0:2 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_642_coc_day1_20min_1 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_cocaine_day1_642.streams._405A.data[2 * t_coc + 1:4 * t_coc])
y1 = np.array(cohort2_cocaine_day1_642.streams._470A.data[2 * t_coc + 1:4 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_642_coc_day1_20min_3 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_cocaine_day1_642.streams._405A.data[4 * t_coc + 1:6 * t_coc])
y1 = np.array(cohort2_cocaine_day1_642.streams._470A.data[4 * t_coc + 1:6 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_642_coc_day1_20min_5 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_cocaine_day1_642.streams._405A.data[6 * t_coc + 1:8 * t_coc])
y1 = np.array(cohort2_cocaine_day1_642.streams._470A.data[6 * t_coc + 1:8 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_642_coc_day1_20min_7 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x_642_coc_day1_20min = np.concatenate((x_642_coc_day1_20min_1,
                                       x_642_coc_day1_20min_3,
                                       x_642_coc_day1_20min_5,
                                       x_642_coc_day1_20min_7), axis=0)

x1 = np.array(cohort2_saline_day1_642.streams._405A.data[0:2 * t_coc])
y1 = np.array(cohort2_saline_day1_642.streams._470A.data[0:2 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_642_sal_day1_20min_1 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_saline_day1_642.streams._405A.data[2 * t_coc + 1:4 * t_coc])
y1 = np.array(cohort2_saline_day1_642.streams._470A.data[2 * t_coc + 1:4 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_642_sal_day1_20min_3 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_saline_day1_642.streams._405A.data[4 * t_coc + 1:6 * t_coc])
y1 = np.array(cohort2_saline_day1_642.streams._470A.data[4 * t_coc + 1:6 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_642_sal_day1_20min_5 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_saline_day1_642.streams._405A.data[6 * t_coc + 1:8 * t_coc])
y1 = np.array(cohort2_saline_day1_642.streams._470A.data[6 * t_coc + 1:8 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_642_sal_day1_20min_7 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x_642_sal_day1_20min = np.concatenate((x_642_sal_day1_20min_1,
                                       x_642_sal_day1_20min_3,
                                       x_642_sal_day1_20min_5,
                                       x_642_sal_day1_20min_7), axis=0)

x1 = np.array(cohort2_cocaine_day1_657.streams._405A.data[0:2 * t_coc])
y1 = np.array(cohort2_cocaine_day1_657.streams._470A.data[0:2 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_657_coc_day1_20min_1 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_cocaine_day1_657.streams._405A.data[2 * t_coc + 1:4 * t_coc])
y1 = np.array(cohort2_cocaine_day1_657.streams._470A.data[2 * t_coc + 1:4 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_657_coc_day1_20min_3 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_cocaine_day1_657.streams._405A.data[4 * t_coc + 1:6 * t_coc])
y1 = np.array(cohort2_cocaine_day1_657.streams._470A.data[4 * t_coc + 1:6 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_657_coc_day1_20min_5 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_cocaine_day1_657.streams._405A.data[6 * t_coc + 1:8 * t_coc])
y1 = np.array(cohort2_cocaine_day1_657.streams._470A.data[6 * t_coc + 1:8 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_657_coc_day1_20min_7 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x_657_coc_day1_20min = np.concatenate((x_657_coc_day1_20min_1,
                                       x_657_coc_day1_20min_3,
                                       x_657_coc_day1_20min_5,
                                       x_657_coc_day1_20min_7), axis=0)

x1 = np.array(cohort2_saline_day1_657.streams._405A.data[0:2 * t_coc])
y1 = np.array(cohort2_saline_day1_657.streams._470A.data[0:2 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_657_sal_day1_20min_1 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_saline_day1_657.streams._405A.data[2 * t_coc + 1:4 * t_coc])
y1 = np.array(cohort2_saline_day1_657.streams._470A.data[2 * t_coc + 1:4 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_657_sal_day1_20min_3 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_saline_day1_657.streams._405A.data[4 * t_coc + 1:6 * t_coc])
y1 = np.array(cohort2_saline_day1_657.streams._470A.data[4 * t_coc + 1:6 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_657_sal_day1_20min_5 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_saline_day1_657.streams._405A.data[6 * t_coc + 1:8 * t_coc])
y1 = np.array(cohort2_saline_day1_657.streams._470A.data[6 * t_coc + 1:8 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_657_sal_day1_20min_7 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x_657_sal_day1_20min = np.concatenate((x_657_sal_day1_20min_1,
                                       x_657_sal_day1_20min_3,
                                       x_657_sal_day1_20min_5,
                                       x_657_sal_day1_20min_7), axis=0)

x1 = np.array(cohort2_cocaine_day1_660.streams._405A.data[0:2 * t_coc])
y1 = np.array(cohort2_cocaine_day1_660.streams._470A.data[0:2 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_660_coc_day1_20min_1 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_cocaine_day1_660.streams._405A.data[2 * t_coc + 1:4 * t_coc])
y1 = np.array(cohort2_cocaine_day1_660.streams._470A.data[2 * t_coc + 1:4 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_660_coc_day1_20min_3 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_cocaine_day1_660.streams._405A.data[4 * t_coc + 1:6 * t_coc])
y1 = np.array(cohort2_cocaine_day1_660.streams._470A.data[4 * t_coc + 1:6 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_660_coc_day1_20min_5 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_cocaine_day1_660.streams._405A.data[6 * t_coc + 1:8 * t_coc])
y1 = np.array(cohort2_cocaine_day1_660.streams._470A.data[6 * t_coc + 1:8 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_660_coc_day1_20min_7 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x_660_coc_day1_20min = np.concatenate((x_660_coc_day1_20min_1,
                                       x_660_coc_day1_20min_3,
                                       x_660_coc_day1_20min_5,
                                       x_660_coc_day1_20min_7), axis=0)

x1 = np.array(cohort2_saline_day1_660.streams._405A.data[0:2 * t_coc])
y1 = np.array(cohort2_saline_day1_660.streams._470A.data[0:2 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_660_sal_day1_20min_1 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_saline_day1_660.streams._405A.data[2 * t_coc + 1:4 * t_coc])
y1 = np.array(cohort2_saline_day1_660.streams._470A.data[2 * t_coc + 1:4 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_660_sal_day1_20min_3 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_saline_day1_660.streams._405A.data[4 * t_coc + 1:6 * t_coc])
y1 = np.array(cohort2_saline_day1_660.streams._470A.data[4 * t_coc + 1:6 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_660_sal_day1_20min_5 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_saline_day1_660.streams._405A.data[6 * t_coc + 1:8 * t_coc])
y1 = np.array(cohort2_saline_day1_660.streams._470A.data[6 * t_coc + 1:8 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_660_sal_day1_20min_7 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x_660_sal_day1_20min = np.concatenate((x_660_sal_day1_20min_1,
                                       x_660_sal_day1_20min_3,
                                       x_660_sal_day1_20min_5,
                                       x_660_sal_day1_20min_7), axis=0)

x1 = np.array(cohort2_cocaine_day1_674.streams._405A.data[0:2 * t_coc])
y1 = np.array(cohort2_cocaine_day1_674.streams._470A.data[0:2 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_674_coc_day1_20min_1 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_cocaine_day1_674.streams._405A.data[2 * t_coc + 1:4 * t_coc])
y1 = np.array(cohort2_cocaine_day1_674.streams._470A.data[2 * t_coc + 1:4 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_674_coc_day1_20min_3 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_cocaine_day1_674.streams._405A.data[4 * t_coc + 1:6 * t_coc])
y1 = np.array(cohort2_cocaine_day1_674.streams._470A.data[4 * t_coc + 1:6 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_674_coc_day1_20min_5 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_cocaine_day1_674.streams._405A.data[6 * t_coc + 1:8 * t_coc])
y1 = np.array(cohort2_cocaine_day1_674.streams._470A.data[6 * t_coc + 1:8 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_674_coc_day1_20min_7 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x_674_coc_day1_20min = np.concatenate((x_674_coc_day1_20min_1,
                                       x_674_coc_day1_20min_3,
                                       x_674_coc_day1_20min_5,
                                       x_674_coc_day1_20min_7), axis=0)

x1 = np.array(cohort2_saline_day1_674.streams._405A.data[0:2 * t_coc])
y1 = np.array(cohort2_saline_day1_674.streams._470A.data[0:2 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_674_sal_day1_20min_1 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_saline_day1_674.streams._405A.data[2 * t_coc + 1:4 * t_coc])
y1 = np.array(cohort2_saline_day1_674.streams._470A.data[2 * t_coc + 1:4 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_674_sal_day1_20min_3 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_saline_day1_674.streams._405A.data[4 * t_coc + 1:6 * t_coc])
y1 = np.array(cohort2_saline_day1_674.streams._470A.data[4 * t_coc + 1:6 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_674_sal_day1_20min_5 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_saline_day1_674.streams._405A.data[6 * t_coc + 1:8 * t_coc])
y1 = np.array(cohort2_saline_day1_674.streams._470A.data[6 * t_coc + 1:8 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_674_sal_day1_20min_7 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x_674_sal_day1_20min = np.concatenate((x_674_sal_day1_20min_1,
                                       x_674_sal_day1_20min_3,
                                       x_674_sal_day1_20min_5,
                                       x_674_sal_day1_20min_7), axis=0)

x1 = np.array(cohort2_cocaine_day1_675.streams._405A.data[0:2 * t_coc])
y1 = np.array(cohort2_cocaine_day1_675.streams._470A.data[0:2 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_675_coc_day1_20min_1 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_cocaine_day1_675.streams._405A.data[2 * t_coc + 1:4 * t_coc])
y1 = np.array(cohort2_cocaine_day1_675.streams._470A.data[2 * t_coc + 1:4 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_675_coc_day1_20min_3 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_cocaine_day1_675.streams._405A.data[4 * t_coc + 1:6 * t_coc])
y1 = np.array(cohort2_cocaine_day1_675.streams._470A.data[4 * t_coc + 1:6 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_675_coc_day1_20min_5 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_cocaine_day1_675.streams._405A.data[6 * t_coc + 1:8 * t_coc])
y1 = np.array(cohort2_cocaine_day1_675.streams._470A.data[6 * t_coc + 1:8 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_675_coc_day1_20min_7 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x_675_coc_day1_20min = np.concatenate((x_675_coc_day1_20min_1,
                                       x_675_coc_day1_20min_3,
                                       x_675_coc_day1_20min_5,
                                       x_675_coc_day1_20min_7), axis=0)

x1 = np.array(cohort2_saline_day1_675.streams._405A.data[0:2 * t_coc])
y1 = np.array(cohort2_saline_day1_675.streams._470A.data[0:2 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_675_sal_day1_20min_1 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_saline_day1_675.streams._405A.data[2 * t_coc + 1:4 * t_coc])
y1 = np.array(cohort2_saline_day1_675.streams._470A.data[2 * t_coc + 1:4 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_675_sal_day1_20min_3 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_saline_day1_675.streams._405A.data[4 * t_coc + 1:6 * t_coc])
y1 = np.array(cohort2_saline_day1_675.streams._470A.data[4 * t_coc + 1:6 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_675_sal_day1_20min_5 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x1 = np.array(cohort2_saline_day1_675.streams._405A.data[6 * t_coc + 1:8 * t_coc])
y1 = np.array(cohort2_saline_day1_675.streams._470A.data[6 * t_coc + 1:8 * t_coc])
bls = np.flip(np.polynomial.polynomial.polyfit(x1, y1, 1))
fit_line = np.multiply(bls[0], x1) + bls[1]
x_675_sal_day1_20min_7 = np.array(stats.zscore((np.array(y1 - fit_line) / np.array(fit_line))))

x_675_sal_day1_20min = np.concatenate((x_675_sal_day1_20min_1,
                                       x_675_sal_day1_20min_3,
                                       x_675_sal_day1_20min_5,
                                       x_675_sal_day1_20min_7), axis=0)

# In[ ]:


# In[ ]:


#
# ## 20min recording post drug injection

# In[ ]:


# In[ ]:


# In[ ]:


# In[ ]:


# In[ ]:


# In[ ]:


# In[ ]:


# In[ ]:


# In[ ]:


# 1200
num_samples_470A_coc = len(cohort3_data5.streams._470A.data)
num_samples_405A_coc = len(cohort3_data5.streams._405A.data)
print("i a here")
_470A_time_coc = np.linspace(1, num_samples_470A_coc, num_samples_470A_coc) / cohort3_data5.streams._470A.fs

average_df_f_flx = np.mean(np.array([x_550_cocaine_day3_20min, x_580_cocaine_day3_20min, x_574_cocaine_day3_20min,
                                     x_330_cocaine_day3_20min, x_621_coc_day3_20min, x_628_coc_day3_20min,
                                     x_660_coc_day3_20min,
                                     x_675_coc_day3_20min, x_3321_coc_day3_20min, x_3336_coc_day3_20min,
                                     x_3346_coc_day3_20min]), axis=0)

average_df_f_gbr = np.mean(np.array(
    [x_331_cocaine_day3_20min, x_549_cocaine_day3_20min, x_620_coc_day3_20min, x_638_coc_day3_20min,
     x_641_coc_day3_20min, x_3337_coc_day3_20min, x_3341_coc_day3_20min]), axis=0)

average_df_f_sal = np.mean(np.array(
    [x_325_cocaine_day3_20min, x_552_cocaine_day3_20min, x_616_coc_day3_20min, x_642_coc_day3_20min,
     x_657_coc_day3_20min, x_674_coc_day3_20min]), axis=0)

flxMean = np.mean(average_df_f_flx);
flxSem = np.std(average_df_f_flx) / np.sqrt(average_df_f_flx[300:2 * t_coc].shape);
gbrMean = np.mean(average_df_f_gbr);
gbrSem = np.std(average_df_f_gbr) / np.sqrt(average_df_f_gbr[300:2 * t_coc].shape);
salMean = np.mean(average_df_f_sal);
salSem = np.std(average_df_f_sal) / np.sqrt(average_df_f_sal[300:2 * t_coc].shape);
flxError = np.random.normal(flxMean, flxSem, size=average_df_f_flx[300:2 * t_coc].shape)
gbrError = np.random.normal(gbrMean, gbrSem, size=average_df_f_gbr[300:2 * t_coc].shape)
salError = np.random.normal(salMean, salSem, size=average_df_f_sal[300:2 * t_coc].shape)

fig, axs = plt.subplots(3, 2)
axs[0, 0].plot(np.array(_470A_time_coc[300:2 * t_coc]), np.array(average_df_f_flx[300:2 * t_coc]), color='coral')
axs[0, 0].fill_between(np.array(_470A_time_coc[300:2 * t_coc]), np.array(average_df_f_flx[300:2 * t_coc]) - flxError,
                       np.array(average_df_f_flx[300:2 * t_coc]) + flxError, alpha=0.2, edgecolor='#1B2ACC',
                       facecolor='#089FFF',
                       linewidth=4, linestyle='dashdot', antialiased=True)

axs[0, 0].set_title('FLX Cocaine Day 3 (0-4min)')

axs[1, 0].plot(np.array(_470A_time_coc[300:2 * t_coc]), np.array(average_df_f_gbr[300:2 * t_coc]), color='blue')
axs[1, 0].set_title('GBR Cocaine Day 3 (0-4min)')
axs[1, 0].fill_between(np.array(_470A_time_coc[300:2 * t_coc]), np.array(average_df_f_gbr[300:2 * t_coc]) - gbrError,
                       np.array(average_df_f_gbr[300:2 * t_coc]) + gbrError, alpha=0.2, edgecolor='#1B2ACC',
                       facecolor='#089FFF',
                       linewidth=4, linestyle='dashdot', antialiased=True)

axs[2, 0].plot(np.array(_470A_time_coc[300:2 * t_coc]), np.array(average_df_f_sal[300:2 * t_coc]), color='red')
axs[2, 0].set_title('SAL Cocaine Day 3 (0-4min)')
axs[2, 0].fill_between(np.array(_470A_time_coc[300:2 * t_coc]), np.array(average_df_f_sal[300:2 * t_coc]) - salError,
                       np.array(average_df_f_sal[300:2 * t_coc]) + salError, alpha=0.2, edgecolor='#1B2ACC',
                       facecolor='#089FFF',
                       linewidth=4, linestyle='dashdot', antialiased=True)

average_df_f_flx_sal = np.mean(np.array(
    [x_550_saline_day3_20min, x_330_saline_day3_20min, x_574_saline_day3_20min, x_580_saline_day3_20min,
     x_621_sal_day3_20min, x_628_sal_day3_20min, x_660_sal_day3_20min, x_675_sal_day3_20min, x_3336_sal_day3_20min,
     x_3346_sal_day3_20min]), axis=0)

average_df_f_gbr_sal = np.mean(np.array(
    [x_331_saline_day3_20min, x_549_saline_day3_20min, x_620_sal_day3_20min, x_638_sal_day3_20min, x_641_sal_day3_20min,
     x_3321_sal_day3_20min, x_3337_sal_day3_20min, x_3341_sal_day3_20min]), axis=0)

average_df_f_sal_sal = np.mean(np.array(
    [x_325_saline_day3_20min, x_552_saline_day3_20min, x_616_sal_day3_20min, x_642_sal_day3_20min, x_657_sal_day3_20min,
     x_674_sal_day3_20min]), axis=0)

flxMean = np.mean(average_df_f_flx_sal);
flxSem = np.std(average_df_f_flx_sal) / np.sqrt(average_df_f_flx_sal[300:2 * t_coc].shape);
gbrMean = np.mean(average_df_f_gbr_sal);
gbrSem = np.std(average_df_f_gbr_sal) / np.sqrt(average_df_f_gbr_sal[300:2 * t_coc].shape);
salMean = np.mean(average_df_f_sal_sal);
salSem = np.std(average_df_f_sal_sal) / np.sqrt(average_df_f_sal_sal[300:2 * t_coc].shape);
flxError = np.random.normal(flxMean, flxSem, size=average_df_f_flx_sal[300:2 * t_coc].shape)
gbrError = np.random.normal(gbrMean, gbrSem, size=average_df_f_gbr_sal[300:2 * t_coc].shape)
salError = np.random.normal(salMean, salSem, size=average_df_f_sal_sal[300:2 * t_coc].shape)

axs[0, 1].plot(np.array(_470A_time_coc[300:2 * t_coc]), np.array(average_df_f_flx_sal[300:2 * t_coc]), color='coral')
axs[0, 1].fill_between(np.array(_470A_time_coc[300:2 * t_coc]),
                       np.array(average_df_f_flx_sal[300:2 * t_coc]) - flxError,
                       np.array(average_df_f_flx_sal[300:2 * t_coc]) + flxError, alpha=0.2, edgecolor='#1B2ACC',
                       facecolor='#089FFF',
                       linewidth=4, linestyle='dashdot', antialiased=True)

axs[0, 1].set_title('FLX Saline Day 3 (0-4min)')

axs[1, 1].plot(np.array(_470A_time_coc[300:2 * t_coc]), np.array(average_df_f_gbr_sal[300:2 * t_coc]), color='blue')
axs[1, 1].set_title('GBR Saline Day 3 (0-4min)')
axs[1, 1].fill_between(np.array(_470A_time_coc[300:2 * t_coc]),
                       np.array(average_df_f_gbr_sal[300:2 * t_coc]) - gbrError,
                       np.array(average_df_f_gbr_sal[300:2 * t_coc]) + gbrError, alpha=0.2, edgecolor='#1B2ACC',
                       facecolor='#089FFF',
                       linewidth=4, linestyle='dashdot', antialiased=True)

axs[2, 1].plot(np.array(_470A_time_coc[300:2 * t_coc]), np.array(average_df_f_sal_sal[300:2 * t_coc]), color='red')
axs[2, 1].set_title('SAL Saline Day 3 (0-4min)')
axs[2, 1].fill_between(np.array(_470A_time_coc[300:2 * t_coc]),
                       np.array(average_df_f_sal_sal[300:2 * t_coc]) - salError,
                       np.array(average_df_f_sal_sal[300:2 * t_coc]) + salError, alpha=0.2, edgecolor='#1B2ACC',
                       facecolor='#089FFF',
                       linewidth=4, linestyle='dashdot', antialiased=True)

for ax in axs.flat:
    ax.set(xlabel='seconds', ylabel='normalized dF/F')

for ax in axs.flat:
    ax.set_ylim(-1, 2)
# Hide x labels and tick labels for top plots and y ticks for right plots.
for ax in axs.flat:
    ax.label_outer()
plt.savefig('plot1.png')
# In[ ]:


# 1200
# num_samples_470A_coc = len(cohort3_data4.streams._470A.data)
# num_samples_405A_coc = len(cohort3_data4.streams._405A.data)
# _470A_time_coc = np.linspace(1, num_samples_470A_coc, num_samples_470A_coc) / cohort3_data1.streams._470A.fs

average_df_f_flx = np.mean(np.array([x_550_cocaine_day3_20min, x_580_cocaine_day3_20min, x_574_cocaine_day3_20min,
                                     x_330_cocaine_day3_20min, x_621_coc_day3_20min, x_628_coc_day3_20min,
                                     x_660_coc_day3_20min,
                                     x_675_coc_day3_20min, x_3321_coc_day3_20min, x_3336_coc_day3_20min,
                                     x_3346_coc_day3_20min]), axis=0)
# plt.plot(np.array(_470A_time_coc[2*t_coc+1*8:t_coc]),np.array(average_df_f_flx[2*t_coc+1*8:t_coc]),color='coral')
# plot the line using slices
average_df_f_gbr = np.mean(np.array(
    [x_331_cocaine_day3_20min, x_549_cocaine_day3_20min, x_620_coc_day3_20min, x_638_coc_day3_20min,
     x_641_coc_day3_20min, x_3337_coc_day3_20min, x_3341_coc_day3_20min]), axis=0)
# plt.plot(np.array(_470A_time_coc[2*t_coc+1*8:t_coc]),np.array(average_df_f_gbr[2*t_coc+1*8:t_coc]),color='coral')
# plot the line using slices
average_df_f_sal = np.mean(np.array(
    [x_325_cocaine_day3_20min, x_552_cocaine_day3_20min, x_616_coc_day3_20min, x_642_coc_day3_20min,
     x_657_coc_day3_20min, x_674_coc_day3_20min]), axis=0)
# plt.plot(np.array(_470A_time_coc[2*t_coc+1*8:t_coc]),np.array(average_df_f_sal[2*t_coc+1*8:t_coc]),color='coral')
# plot the line using slices

flxMean = np.mean(average_df_f_flx);
flxSem = np.std(average_df_f_flx) / np.sqrt(average_df_f_flx[2 * t_coc + 1:4 * t_coc].shape);
gbrMean = np.mean(average_df_f_gbr);
gbrSem = np.std(average_df_f_gbr) / np.sqrt(average_df_f_gbr[2 * t_coc + 1:4 * t_coc].shape);
salMean = np.mean(average_df_f_sal);
salSem = np.std(average_df_f_sal) / np.sqrt(average_df_f_sal[2 * t_coc + 1:4 * t_coc].shape);
flxError = np.random.normal(flxMean, flxSem, size=average_df_f_flx[2 * t_coc + 1:4 * t_coc].shape)
gbrError = np.random.normal(gbrMean, gbrSem, size=average_df_f_gbr[2 * t_coc + 1:4 * t_coc].shape)
salError = np.random.normal(salMean, salSem, size=average_df_f_sal[2 * t_coc + 1:4 * t_coc].shape)
# y += np.random.normal(0, 0.1, size=y.shape)

# plt.plot(x, y, 'k-')


fig, axs = plt.subplots(3, 2)
axs[0, 0].plot(np.array(_470A_time_coc[2 * t_coc + 1:4 * t_coc]), np.array(average_df_f_flx[2 * t_coc + 1:4 * t_coc]),
               color='coral')
axs[0, 0].fill_between(np.array(_470A_time_coc[2 * t_coc + 1:4 * t_coc]),
                       np.array(average_df_f_flx[2 * t_coc + 1:4 * t_coc]) - flxError,
                       np.array(average_df_f_flx[2 * t_coc + 1:4 * t_coc]) + flxError, alpha=0.2, edgecolor='#1B2ACC',
                       facecolor='#089FFF',
                       linewidth=4, linestyle='dashdot', antialiased=True)

axs[0, 0].set_title('FLX Cocaine Day 3 (4-8min)')

axs[1, 0].plot(np.array(_470A_time_coc[2 * t_coc + 1:4 * t_coc]), np.array(average_df_f_gbr[2 * t_coc + 1:4 * t_coc]),
               color='blue')
axs[1, 0].set_title('GBR Cocaine Day 3 (4-8min)')
axs[1, 0].fill_between(np.array(_470A_time_coc[2 * t_coc + 1:4 * t_coc]),
                       np.array(average_df_f_gbr[2 * t_coc + 1:4 * t_coc]) - gbrError,
                       np.array(average_df_f_gbr[2 * t_coc + 1:4 * t_coc]) + gbrError, alpha=0.2, edgecolor='#1B2ACC',
                       facecolor='#089FFF',
                       linewidth=4, linestyle='dashdot', antialiased=True)

axs[2, 0].plot(np.array(_470A_time_coc[2 * t_coc + 1:4 * t_coc]), np.array(average_df_f_sal[2 * t_coc + 1:4 * t_coc]),
               color='red')
axs[2, 0].set_title('SAL Cocaine Day 3 (4-8min)')
axs[2, 0].fill_between(np.array(_470A_time_coc[2 * t_coc + 1:4 * t_coc]),
                       np.array(average_df_f_sal[2 * t_coc + 1:4 * t_coc]) - salError,
                       np.array(average_df_f_sal[2 * t_coc + 1:4 * t_coc]) + salError, alpha=0.2, edgecolor='#1B2ACC',
                       facecolor='#089FFF',
                       linewidth=4, linestyle='dashdot', antialiased=True)

# for ax in axs.flat:
#   ax.set(xlabel='secs', ylabel='normalized dF/F')

# Hide x labels and tick labels for top plots and y ticks for right plots.
# for ax in axs.flat:
#   ax.label_outer()
# for ax in axs.flat:
#   ax.set_ylim(-1,2)

average_df_f_flx_sal = np.mean(np.array(
    [x_550_saline_day3_20min, x_330_saline_day3_20min, x_574_saline_day3_20min, x_580_saline_day3_20min,
     x_621_sal_day3_20min, x_628_sal_day3_20min, x_660_sal_day3_20min, x_675_sal_day3_20min, x_3336_sal_day3_20min,
     x_3346_sal_day3_20min]), axis=0)
# plt.plot(np.array(_470A_time_coc[2*t_coc+1*8:t_coc]),np.array(average_df_f_flx[2*t_coc+1*8:t_coc]),color='coral')
# plot the line using slices


average_df_f_gbr_sal = np.mean(np.array(
    [x_331_saline_day3_20min, x_549_saline_day3_20min, x_620_sal_day3_20min, x_638_sal_day3_20min, x_641_sal_day3_20min,
     x_3321_sal_day3_20min, x_3337_sal_day3_20min, x_3341_sal_day3_20min]), axis=0)
# plt.plot(np.array(_470A_time_coc[2*t_coc+1*8:t_coc]),np.array(average_df_f_gbr[2*t_coc+1*8:t_coc]),color='coral')
# plot the line using slices
average_df_f_sal_sal = np.mean(np.array(
    [x_325_saline_day3_20min, x_552_saline_day3_20min, x_616_sal_day3_20min, x_642_sal_day3_20min, x_657_sal_day3_20min,
     x_674_sal_day3_20min]), axis=0)
# plt.plot(np.array(_470A_time_coc[2*t_coc+1*8:t_coc]),np.array(average_df_f_sal[2*t_coc+1*8:t_coc]),color='coral')
# plot the line using slices

flxMean = np.mean(average_df_f_flx_sal);
flxSem = np.std(average_df_f_flx_sal) / np.sqrt(average_df_f_flx_sal[2 * t_coc + 1:4 * t_coc].shape);
gbrMean = np.mean(average_df_f_gbr_sal);
gbrSem = np.std(average_df_f_gbr_sal) / np.sqrt(average_df_f_gbr_sal[2 * t_coc + 1:4 * t_coc].shape);
salMean = np.mean(average_df_f_sal_sal);
salSem = np.std(average_df_f_sal_sal) / np.sqrt(average_df_f_sal_sal[2 * t_coc + 1:4 * t_coc].shape);
flxError = np.random.normal(flxMean, flxSem, size=average_df_f_flx_sal[2 * t_coc + 1:4 * t_coc].shape)
gbrError = np.random.normal(gbrMean, gbrSem, size=average_df_f_gbr_sal[2 * t_coc + 1:4 * t_coc].shape)
salError = np.random.normal(salMean, salSem, size=average_df_f_sal_sal[2 * t_coc + 1:4 * t_coc].shape)
# y += np.random.normal(0, 0.1, size=y.shape)
axs[0, 1].plot(np.array(_470A_time_coc[2 * t_coc + 1:4 * t_coc]),
               np.array(average_df_f_flx_sal[2 * t_coc + 1:4 * t_coc]), color='coral')
axs[0, 1].fill_between(np.array(_470A_time_coc[2 * t_coc + 1:4 * t_coc]),
                       np.array(average_df_f_flx_sal[2 * t_coc + 1:4 * t_coc]) - flxError,
                       np.array(average_df_f_flx_sal[2 * t_coc + 1:4 * t_coc]) + flxError, alpha=0.2,
                       edgecolor='#1B2ACC', facecolor='#089FFF',
                       linewidth=4, linestyle='dashdot', antialiased=True)

axs[0, 1].set_title('FLX Saline Day 3 (4-8min)')

axs[1, 1].plot(np.array(_470A_time_coc[2 * t_coc + 1:4 * t_coc]),
               np.array(average_df_f_gbr_sal[2 * t_coc + 1:4 * t_coc]), color='blue')
axs[1, 1].set_title('GBR Saline Day 3 (4-8min)')
axs[1, 1].fill_between(np.array(_470A_time_coc[2 * t_coc + 1:4 * t_coc]),
                       np.array(average_df_f_gbr_sal[2 * t_coc + 1:4 * t_coc]) - gbrError,
                       np.array(average_df_f_gbr_sal[2 * t_coc + 1:4 * t_coc]) + gbrError, alpha=0.2,
                       edgecolor='#1B2ACC', facecolor='#089FFF',
                       linewidth=4, linestyle='dashdot', antialiased=True)

axs[2, 1].plot(np.array(_470A_time_coc[2 * t_coc + 1:4 * t_coc]),
               np.array(average_df_f_sal_sal[2 * t_coc + 1:4 * t_coc]), color='red')
axs[2, 1].set_title('SAL Saline Day 3 (4-8min)')
axs[2, 1].fill_between(np.array(_470A_time_coc[2 * t_coc + 1:4 * t_coc]),
                       np.array(average_df_f_sal_sal[2 * t_coc + 1:4 * t_coc]) - salError,
                       np.array(average_df_f_sal_sal[2 * t_coc + 1:4 * t_coc]) + salError, alpha=0.2,
                       edgecolor='#1B2ACC', facecolor='#089FFF',
                       linewidth=4, linestyle='dashdot', antialiased=True)

for ax in axs.flat:
    ax.set(xlabel='seconds', ylabel='normalized dF/F')

for ax in axs.flat:
    ax.set_ylim(-1, 2)
# Hide x labels and tick labels for top plots and y ticks for right plots.
for ax in axs.flat:
    ax.label_outer()
plt.savefig('plot2.png')
# In[ ]:


# 1200
# num_samples_470A_coc = len(cohort3_data4.streams._470A.data)
# num_samples_405A_coc = len(cohort3_data4.streams._405A.data)
# _470A_time_coc = np.linspace(1, num_samples_470A_coc, num_samples_470A_coc) / cohort3_data1.streams._470A.fs

average_df_f_flx = np.mean(np.array([x_550_cocaine_day3_20min, x_580_cocaine_day3_20min, x_574_cocaine_day3_20min,
                                     x_330_cocaine_day3_20min, x_621_coc_day3_20min, x_628_coc_day3_20min,
                                     x_660_coc_day3_20min,
                                     x_675_coc_day3_20min, x_3321_coc_day3_20min, x_3336_coc_day3_20min,
                                     x_3346_coc_day3_20min]), axis=0)
# plt.plot(np.array(_470A_time_coc[4*t_coc+1*8:t_coc]),np.array(average_df_f_flx[4*t_coc+1*8:t_coc]),color='coral')
# plot the line using slices
average_df_f_gbr = np.mean(np.array(
    [x_331_cocaine_day3_20min, x_549_cocaine_day3_20min, x_620_coc_day3_20min, x_638_coc_day3_20min,
     x_641_coc_day3_20min, x_3337_coc_day3_20min, x_3341_coc_day3_20min]), axis=0)
# plt.plot(np.array(_470A_time_coc[4*t_coc+1*8:t_coc]),np.array(average_df_f_gbr[4*t_coc+1*8:t_coc]),color='coral')
# plot the line using slices
average_df_f_sal = np.mean(np.array(
    [x_325_cocaine_day3_20min, x_552_cocaine_day3_20min, x_616_coc_day3_20min, x_642_coc_day3_20min,
     x_657_coc_day3_20min, x_674_coc_day3_20min]), axis=0)
# plt.plot(np.array(_470A_time_coc[4*t_coc+1*8:t_coc]),np.array(average_df_f_sal[4*t_coc+1*8:t_coc]),color='coral')
# plot the line using slices

flxMean = np.mean(average_df_f_flx);
flxSem = np.std(average_df_f_flx) / np.sqrt(average_df_f_flx[4 * t_coc + 1:6 * t_coc].shape);
gbrMean = np.mean(average_df_f_gbr);
gbrSem = np.std(average_df_f_gbr) / np.sqrt(average_df_f_gbr[4 * t_coc + 1:6 * t_coc].shape);
salMean = np.mean(average_df_f_sal);
salSem = np.std(average_df_f_sal) / np.sqrt(average_df_f_sal[4 * t_coc + 1:6 * t_coc].shape);
flxError = np.random.normal(flxMean, flxSem, size=average_df_f_flx[4 * t_coc + 1:6 * t_coc].shape)
gbrError = np.random.normal(gbrMean, gbrSem, size=average_df_f_gbr[4 * t_coc + 1:6 * t_coc].shape)
salError = np.random.normal(salMean, salSem, size=average_df_f_sal[4 * t_coc + 1:6 * t_coc].shape)
# y += np.random.normal(0, 0.1, size=y.shape)

# plt.plot(x, y, 'k-')


fig, axs = plt.subplots(3, 2)
axs[0, 0].plot(np.array(_470A_time_coc[4 * t_coc + 1:6 * t_coc]), np.array(average_df_f_flx[4 * t_coc + 1:6 * t_coc]),
               color='coral')
axs[0, 0].fill_between(np.array(_470A_time_coc[4 * t_coc + 1:6 * t_coc]),
                       np.array(average_df_f_flx[4 * t_coc + 1:6 * t_coc]) - flxError,
                       np.array(average_df_f_flx[4 * t_coc + 1:6 * t_coc]) + flxError, alpha=0.2, edgecolor='#1B2ACC',
                       facecolor='#089FFF',
                       linewidth=4, linestyle='dashdot', antialiased=True)

axs[0, 0].set_title('FLX Cocaine Day 3 (8-12min)')

axs[1, 0].plot(np.array(_470A_time_coc[4 * t_coc + 1:6 * t_coc]), np.array(average_df_f_gbr[4 * t_coc + 1:6 * t_coc]),
               color='blue')
axs[1, 0].set_title('GBR Cocaine Day 3 (8-12min)')
axs[1, 0].fill_between(np.array(_470A_time_coc[4 * t_coc + 1:6 * t_coc]),
                       np.array(average_df_f_gbr[4 * t_coc + 1:6 * t_coc]) - gbrError,
                       np.array(average_df_f_gbr[4 * t_coc + 1:6 * t_coc]) + gbrError, alpha=0.2, edgecolor='#1B2ACC',
                       facecolor='#089FFF',
                       linewidth=4, linestyle='dashdot', antialiased=True)

axs[2, 0].plot(np.array(_470A_time_coc[4 * t_coc + 1:6 * t_coc]), np.array(average_df_f_sal[4 * t_coc + 1:6 * t_coc]),
               color='red')
axs[2, 0].set_title('SAL Cocaine Day 3 (8-12min)')
axs[2, 0].fill_between(np.array(_470A_time_coc[4 * t_coc + 1:6 * t_coc]),
                       np.array(average_df_f_sal[4 * t_coc + 1:6 * t_coc]) - salError,
                       np.array(average_df_f_sal[4 * t_coc + 1:6 * t_coc]) + salError, alpha=0.2, edgecolor='#1B2ACC',
                       facecolor='#089FFF',
                       linewidth=4, linestyle='dashdot', antialiased=True)

# for ax in axs.flat:
#   ax.set(xlabel='secs', ylabel='normalized dF/F')

# Hide x labels and tick labels for top plots and y ticks for right plots.
# for ax in axs.flat:
#   ax.label_outer()
# for ax in axs.flat:
#   ax.set_ylim(-1,2)

average_df_f_flx_sal = np.mean(np.array(
    [x_550_saline_day3_20min, x_330_saline_day3_20min, x_574_saline_day3_20min, x_580_saline_day3_20min,
     x_621_sal_day3_20min, x_628_sal_day3_20min, x_660_sal_day3_20min, x_675_sal_day3_20min, x_3336_sal_day3_20min,
     x_3346_sal_day3_20min]), axis=0)
# plt.plot(np.array(_470A_time_coc[4*t_coc+1*8:t_coc]),np.array(average_df_f_flx[4*t_coc+1*8:t_coc]),color='coral')
# plot the line using slices


average_df_f_gbr_sal = np.mean(np.array(
    [x_331_saline_day3_20min, x_549_saline_day3_20min, x_620_sal_day3_20min, x_638_sal_day3_20min, x_641_sal_day3_20min,
     x_3321_sal_day3_20min, x_3337_sal_day3_20min, x_3341_sal_day3_20min]), axis=0)
# plt.plot(np.array(_470A_time_coc[4*t_coc+1*8:t_coc]),np.array(average_df_f_gbr[4*t_coc+1*8:t_coc]),color='coral')
# plot the line using slices
average_df_f_sal_sal = np.mean(np.array(
    [x_325_saline_day3_20min, x_552_saline_day3_20min, x_616_sal_day3_20min, x_642_sal_day3_20min, x_657_sal_day3_20min,
     x_674_sal_day3_20min]), axis=0)
# plt.plot(np.array(_470A_time_coc[4*t_coc+1*8:t_coc]),np.array(average_df_f_sal[4*t_coc+1*8:t_coc]),color='coral')
# plot the line using slices

flxMean = np.mean(average_df_f_flx_sal);
flxSem = np.std(average_df_f_flx_sal) / np.sqrt(average_df_f_flx_sal[4 * t_coc + 1:6 * t_coc].shape);
gbrMean = np.mean(average_df_f_gbr_sal);
gbrSem = np.std(average_df_f_gbr_sal) / np.sqrt(average_df_f_gbr_sal[4 * t_coc + 1:6 * t_coc].shape);
salMean = np.mean(average_df_f_sal_sal);
salSem = np.std(average_df_f_sal_sal) / np.sqrt(average_df_f_sal_sal[4 * t_coc + 1:6 * t_coc].shape);
flxError = np.random.normal(flxMean, flxSem, size=average_df_f_flx_sal[4 * t_coc + 1:6 * t_coc].shape)
gbrError = np.random.normal(gbrMean, gbrSem, size=average_df_f_gbr_sal[4 * t_coc + 1:6 * t_coc].shape)
salError = np.random.normal(salMean, salSem, size=average_df_f_sal_sal[4 * t_coc + 1:6 * t_coc].shape)
# y += np.random.normal(0, 0.1, size=y.shape)
axs[0, 1].plot(np.array(_470A_time_coc[4 * t_coc + 1:6 * t_coc]),
               np.array(average_df_f_flx_sal[4 * t_coc + 1:6 * t_coc]), color='coral')
axs[0, 1].fill_between(np.array(_470A_time_coc[4 * t_coc + 1:6 * t_coc]),
                       np.array(average_df_f_flx_sal[4 * t_coc + 1:6 * t_coc]) - flxError,
                       np.array(average_df_f_flx_sal[4 * t_coc + 1:6 * t_coc]) + flxError, alpha=0.2,
                       edgecolor='#1B2ACC', facecolor='#089FFF',
                       linewidth=4, linestyle='dashdot', antialiased=True)

axs[0, 1].set_title('FLX Saline Day 3 (8-12min)')

axs[1, 1].plot(np.array(_470A_time_coc[4 * t_coc + 1:6 * t_coc]),
               np.array(average_df_f_gbr_sal[4 * t_coc + 1:6 * t_coc]), color='blue')
axs[1, 1].set_title('GBR Saline Day 3 (8-12min)')
axs[1, 1].fill_between(np.array(_470A_time_coc[4 * t_coc + 1:6 * t_coc]),
                       np.array(average_df_f_gbr_sal[4 * t_coc + 1:6 * t_coc]) - gbrError,
                       np.array(average_df_f_gbr_sal[4 * t_coc + 1:6 * t_coc]) + gbrError, alpha=0.2,
                       edgecolor='#1B2ACC', facecolor='#089FFF',
                       linewidth=4, linestyle='dashdot', antialiased=True)

axs[2, 1].plot(np.array(_470A_time_coc[4 * t_coc + 1:6 * t_coc]),
               np.array(average_df_f_sal_sal[4 * t_coc + 1:6 * t_coc]), color='red')
axs[2, 1].set_title('SAL Saline Day 3 (8-12min)')
axs[2, 1].fill_between(np.array(_470A_time_coc[4 * t_coc + 1:6 * t_coc]),
                       np.array(average_df_f_sal_sal[4 * t_coc + 1:6 * t_coc]) - salError,
                       np.array(average_df_f_sal_sal[4 * t_coc + 1:6 * t_coc]) + salError, alpha=0.2,
                       edgecolor='#1B2ACC', facecolor='#089FFF',
                       linewidth=4, linestyle='dashdot', antialiased=True)

for ax in axs.flat:
    ax.set(xlabel='seconds', ylabel='normalized dF/F')

for ax in axs.flat:
    ax.set_ylim(-1, 2)
# Hide x labels and tick labels for top plots and y ticks for right plots.
for ax in axs.flat:
    ax.label_outer()
plt.savefig('plot3.png')
# In[ ]:


# 1200
# num_samples_470A_coc = len(cohort3_data4.streams._470A.data)
# num_samples_405A_coc = len(cohort3_data4.streams._405A.data)
# _470A_time_coc = np.linspace(1, num_samples_470A_coc, num_samples_470A_coc) / cohort3_data1.streams._470A.fs

average_df_f_flx = np.mean(np.array([x_550_cocaine_day3_20min, x_580_cocaine_day3_20min, x_574_cocaine_day3_20min,
                                     x_330_cocaine_day3_20min, x_621_coc_day3_20min, x_628_coc_day3_20min,
                                     x_660_coc_day3_20min,
                                     x_675_coc_day3_20min, x_3321_coc_day3_20min, x_3336_coc_day3_20min,
                                     x_3346_coc_day3_20min]), axis=0)
# plt.plot(np.array(_470A_time_coc[6*t_coc+1*8:t_coc]),np.array(average_df_f_flx[6*t_coc+1*8:t_coc]),color='coral')
# plot the line using slices
average_df_f_gbr = np.mean(np.array(
    [x_331_cocaine_day3_20min, x_549_cocaine_day3_20min, x_620_coc_day3_20min, x_638_coc_day3_20min,
     x_641_coc_day3_20min, x_3337_coc_day3_20min, x_3341_coc_day3_20min]), axis=0)
# plt.plot(np.array(_470A_time_coc[6*t_coc+1*8:t_coc]),np.array(average_df_f_gbr[6*t_coc+1*8:t_coc]),color='coral')
# plot the line using slices
average_df_f_sal = np.mean(np.array(
    [x_325_cocaine_day3_20min, x_552_cocaine_day3_20min, x_616_coc_day3_20min, x_642_coc_day3_20min,
     x_657_coc_day3_20min, x_674_coc_day3_20min]), axis=0)
# plt.plot(np.array(_470A_time_coc[6*t_coc+1*8:t_coc]),np.array(average_df_f_sal[6*t_coc+1*8:t_coc]),color='coral')
# plot the line using slices

flxMean = np.mean(average_df_f_flx);
flxSem = np.std(average_df_f_flx) / np.sqrt(average_df_f_flx[6 * t_coc + 1:8 * t_coc].shape);
gbrMean = np.mean(average_df_f_gbr);
gbrSem = np.std(average_df_f_gbr) / np.sqrt(average_df_f_gbr[6 * t_coc + 1:8 * t_coc].shape);
salMean = np.mean(average_df_f_sal);
salSem = np.std(average_df_f_sal) / np.sqrt(average_df_f_sal[6 * t_coc + 1:8 * t_coc].shape);
flxError = np.random.normal(flxMean, flxSem, size=average_df_f_flx[6 * t_coc + 1:8 * t_coc].shape)
gbrError = np.random.normal(gbrMean, gbrSem, size=average_df_f_gbr[6 * t_coc + 1:8 * t_coc].shape)
salError = np.random.normal(salMean, salSem, size=average_df_f_sal[6 * t_coc + 1:8 * t_coc].shape)
# y += np.random.normal(0, 0.1, size=y.shape)

# plt.plot(x, y, 'k-')


fig, axs = plt.subplots(3, 2)
axs[0, 0].plot(np.array(_470A_time_coc[6 * t_coc + 1:8 * t_coc]), np.array(average_df_f_flx[6 * t_coc + 1:8 * t_coc]),
               color='coral')
axs[0, 0].fill_between(np.array(_470A_time_coc[6 * t_coc + 1:8 * t_coc]),
                       np.array(average_df_f_flx[6 * t_coc + 1:8 * t_coc]) - flxError,
                       np.array(average_df_f_flx[6 * t_coc + 1:8 * t_coc]) + flxError, alpha=0.2, edgecolor='#1B2ACC',
                       facecolor='#089FFF',
                       linewidth=4, linestyle='dashdot', antialiased=True)

axs[0, 0].set_title('FLX Cocaine Day 3 (12-16min)')

axs[1, 0].plot(np.array(_470A_time_coc[6 * t_coc + 1:8 * t_coc]), np.array(average_df_f_gbr[6 * t_coc + 1:8 * t_coc]),
               color='blue')
axs[1, 0].set_title('GBR Cocaine Day 3 (12-16min)')
axs[1, 0].fill_between(np.array(_470A_time_coc[6 * t_coc + 1:8 * t_coc]),
                       np.array(average_df_f_gbr[6 * t_coc + 1:8 * t_coc]) - gbrError,
                       np.array(average_df_f_gbr[6 * t_coc + 1:8 * t_coc]) + gbrError, alpha=0.2, edgecolor='#1B2ACC',
                       facecolor='#089FFF',
                       linewidth=4, linestyle='dashdot', antialiased=True)

axs[2, 0].plot(np.array(_470A_time_coc[6 * t_coc + 1:8 * t_coc]), np.array(average_df_f_sal[6 * t_coc + 1:8 * t_coc]),
               color='red')
axs[2, 0].set_title('SAL Cocaine Day 3 (12-16min)')
axs[2, 0].fill_between(np.array(_470A_time_coc[6 * t_coc + 1:8 * t_coc]),
                       np.array(average_df_f_sal[6 * t_coc + 1:8 * t_coc]) - salError,
                       np.array(average_df_f_sal[6 * t_coc + 1:8 * t_coc]) + salError, alpha=0.2, edgecolor='#1B2ACC',
                       facecolor='#089FFF',
                       linewidth=4, linestyle='dashdot', antialiased=True)

# for ax in axs.flat:
#   ax.set(xlabel='secs', ylabel='normalized dF/F')

# Hide x labels and tick labels for top plots and y ticks for right plots.
# for ax in axs.flat:
#   ax.label_outer()
# for ax in axs.flat:
#   ax.set_ylim(-1,2)

average_df_f_flx_sal = np.mean(np.array(
    [x_550_saline_day3_20min, x_330_saline_day3_20min, x_574_saline_day3_20min, x_580_saline_day3_20min,
     x_621_sal_day3_20min, x_628_sal_day3_20min, x_660_sal_day3_20min, x_675_sal_day3_20min, x_3336_sal_day3_20min,
     x_3346_sal_day3_20min]), axis=0)
# plt.plot(np.array(_470A_time_coc[6*t_coc+1*8:t_coc]),np.array(average_df_f_flx[6*t_coc+1*8:t_coc]),color='coral')
# plot the line using slices


average_df_f_gbr_sal = np.mean(np.array(
    [x_331_saline_day3_20min, x_549_saline_day3_20min, x_620_sal_day3_20min, x_638_sal_day3_20min, x_641_sal_day3_20min,
     x_3321_sal_day3_20min, x_3337_sal_day3_20min, x_3341_sal_day3_20min]), axis=0)
# plt.plot(np.array(_470A_time_coc[6*t_coc+1*8:t_coc]),np.array(average_df_f_gbr[6*t_coc+1*8:t_coc]),color='coral')
# plot the line using slices
average_df_f_sal_sal = np.mean(np.array(
    [x_325_saline_day3_20min, x_552_saline_day3_20min, x_616_sal_day3_20min, x_642_sal_day3_20min, x_657_sal_day3_20min,
     x_674_sal_day3_20min]), axis=0)
# plt.plot(np.array(_470A_time_coc[6*t_coc+1*8:t_coc]),np.array(average_df_f_sal[6*t_coc+1*8:t_coc]),color='coral')
# plot the line using slices

flxMean = np.mean(average_df_f_flx_sal);
flxSem = np.std(average_df_f_flx_sal) / np.sqrt(average_df_f_flx_sal[6 * t_coc + 1:8 * t_coc].shape);
gbrMean = np.mean(average_df_f_gbr_sal);
gbrSem = np.std(average_df_f_gbr_sal) / np.sqrt(average_df_f_gbr_sal[6 * t_coc + 1:8 * t_coc].shape);
salMean = np.mean(average_df_f_sal_sal);
salSem = np.std(average_df_f_sal_sal) / np.sqrt(average_df_f_sal_sal[6 * t_coc + 1:8 * t_coc].shape);
flxError = np.random.normal(flxMean, flxSem, size=average_df_f_flx_sal[6 * t_coc + 1:8 * t_coc].shape)
gbrError = np.random.normal(gbrMean, gbrSem, size=average_df_f_gbr_sal[6 * t_coc + 1:8 * t_coc].shape)
salError = np.random.normal(salMean, salSem, size=average_df_f_sal_sal[6 * t_coc + 1:8 * t_coc].shape)
# y += np.random.normal(0, 0.1, size=y.shape)
axs[0, 1].plot(np.array(_470A_time_coc[6 * t_coc + 1:8 * t_coc]),
               np.array(average_df_f_flx_sal[6 * t_coc + 1:8 * t_coc]), color='coral')
axs[0, 1].fill_between(np.array(_470A_time_coc[6 * t_coc + 1:8 * t_coc]),
                       np.array(average_df_f_flx_sal[6 * t_coc + 1:8 * t_coc]) - flxError,
                       np.array(average_df_f_flx_sal[6 * t_coc + 1:8 * t_coc]) + flxError, alpha=0.2,
                       edgecolor='#1B2ACC', facecolor='#089FFF',
                       linewidth=4, linestyle='dashdot', antialiased=True)

axs[0, 1].set_title('FLX Saline Day 3 (12-16min)')

axs[1, 1].plot(np.array(_470A_time_coc[6 * t_coc + 1:8 * t_coc]),
               np.array(average_df_f_gbr_sal[6 * t_coc + 1:8 * t_coc]), color='blue')
axs[1, 1].set_title('GBR Saline Day 3 (12-16min)')
axs[1, 1].fill_between(np.array(_470A_time_coc[6 * t_coc + 1:8 * t_coc]),
                       np.array(average_df_f_gbr_sal[6 * t_coc + 1:8 * t_coc]) - gbrError,
                       np.array(average_df_f_gbr_sal[6 * t_coc + 1:8 * t_coc]) + gbrError, alpha=0.2,
                       edgecolor='#1B2ACC', facecolor='#089FFF',
                       linewidth=4, linestyle='dashdot', antialiased=True)

axs[2, 1].plot(np.array(_470A_time_coc[6 * t_coc + 1:8 * t_coc]),
               np.array(average_df_f_sal_sal[6 * t_coc + 1:8 * t_coc]), color='red')
axs[2, 1].set_title('SAL Saline Day 3 (12-16min)')
axs[2, 1].fill_between(np.array(_470A_time_coc[6 * t_coc + 1:8 * t_coc]),
                       np.array(average_df_f_sal_sal[6 * t_coc + 1:8 * t_coc]) - salError,
                       np.array(average_df_f_sal_sal[6 * t_coc + 1:8 * t_coc]) + salError, alpha=0.2,
                       edgecolor='#1B2ACC', facecolor='#089FFF',
                       linewidth=4, linestyle='dashdot', antialiased=True)

for ax in axs.flat:
    ax.set(xlabel='seconds', ylabel='normalized dF/F')

for ax in axs.flat:
    ax.set_ylim(-1, 2)
# Hide x labels and tick labels for top plots and y ticks for right plots.
for ax in axs.flat:
    ax.label_outer()
plt.savefig('plot4.png')
# ###

#

#

# In[ ]:


#

# In[ ]:


#

#

# In[ ]:


#

# In[ ]:


#

# In[ ]:


#

# In[ ]:


#

# In[ ]:


#

# In[ ]:


#

# In[ ]:


#

# In[ ]:


#

# In[ ]:


#

# In[ ]:


#

# In[ ]:


#

# In[ ]:


#

# In[ ]:


#

# In[ ]:


#

# In[ ]:


#

# In[ ]:


#

# In[ ]:


#

# In[ ]:


#

# In[ ]:


#

# In[ ]:


#

# In[ ]:


#

# In[ ]:


# In[ ]:




