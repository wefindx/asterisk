# -*- coding: utf-8 -*-

'''
=============================================================
 AI is no more than a process solving equation F(X)=Y for X.
=============================================================

This is an attempt to create an abstract framework for general purpose AI, in Python. :)

Implement the below classes of F(), X(), Y(), and run Process.collect() in parallel 
controlled by Process.predict() to continually model F(), optimize X() to achieve Y() 
to create an AI.

Note: F and Y could be defined in terms of some concepts, like WikiData IDs.
We probably need a Python package that implements association with WikiData IDs.
>>> import .wikidata as wd

The F
=====
F is the world's model. I would mainly use SymPy (sympy.org) to define deterministic 
relations, like laws of physics, and use Chainer (chainer.org) to learn non-deterministic, 
experiences as models:
>>> import sympy as S, chainer

The X
=====
X is the agent's actions. I would use this class to assmble all non-trivial actions, 
that an agent could take, such as even collect data actions, and perform some changes of the world. I would use things like gpio (RaspberryPI), mechanize 
(python.org/pypi/mechanize), requests (docs.python-requests.org), responses 
(pypi.python.org/pypi/responses):
>>> import gpio, mechanize, requests, responses

The Y
=====
Y is the agent's goals. These are ranges of assests that the agent is aiming for, and the 
reasons for these ranges, rooted in the requirement to retain information the most useful 
for retaining information in the presence of universe's entropy. (Which means, learning the 
properties of world's entropy, judging the utility of new constructs to retain information
in form of everything that exists and existed.)

For storing the ranges of assets, I would use:
>>> import plandf

For storing the reasons, I would use projection of the future world F', and probably
networkx for causal connections.
>>> import networkx

The Utils
=========
In order to put the data into right format for analysis (i.e., do
ETL=Extract-Transform-Load), we need to use some package to align it, and I would use 
Pandas (pandas.pydata.org).
>>> import pandas as pd, xarray as xr

# Note on ETL:
    # https://en.wikipedia.org/wiki/Extract,_transform,_load

The Stats
=========
In order to put the features into right format for deciding (i.e., do 
EWA=Extract-Weight-Act), we need to use some packages to incrementally extract features, 
and I would use StatsModels, Sci-Kit Learn, Scikit Image, and others, in combination 
with plandf, to arrive at comparison between goals and predictions.
>>> import plandf, statsmodels as sm, sklearn

# Note on EWA - (it's my own made-up concept)
    # 1. Extract: mainly uses Stats to extract and set features of F (world).
    # 2. Weight: uses Y to produce "eventual features" -- goal-based risk-weighted feature 
    # predictions F'.
    # 3. Act: uses a choice function to compute "final features" -- instances of actions (X) 
    # with smallest risk.

Basic Usage
===========

>>> import multiprocessing
>>> agent = Process()

>>> c = multiprocessing.Process( target=agent.collect )
>>> p = multiprocessing.Process( target=agent.predict )
>>> c.start(); p.start()
>>> c.join(); p.join()

'''

import multiprocessing
import logging
import time
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)

class F(object):
    ''' World Model: this is data, concepts as features and relationships between them. '''
    pass

class X(object):
    ''' Actions: these are automation scripts for complex pre-programmed routines. '''
    pass

class Y(object):
    ''' Goals: loss functions to extract risk features. '''
    pass

class Utils(object):
    ''' Operating system level I/O, and data transformation tools. '''
    pass

class Stats(object):
    ''' Primitive predictive models and visualization tools. '''
    pass

class Process(object):
    def __init__(self):
        self.F = F()
        self.X = X()
        self.Y = Y()

    def collect(self):
        ''' Mostly uses Utils, to collect data. '''
        while True:
            ''' ETL: Extract(data)-Transform(data)-Load(data). '''
            logging.info('collect')
            time.sleep(1)
            
    def predict(self):
        ''' Mostly uses Stats, to extract features. '''
        while True:
            ''' EWA: Extract(features)-Weight(evaluate risk)-Act(parametrize actions). '''
            logging.info('predict')
            time.sleep(2)

if __name__ == '__main__':

    agent = Process()

    collecting = multiprocessing.Process( target=agent.collect )
    predicting = multiprocessing.Process( target=agent.predict )

    collecting.start(); predicting.start()
    collecting.join(); predicting.join()

