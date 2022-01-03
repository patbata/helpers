import inspect
import numpy as np
import pandas as pd
import math
import pickle
import seaborn as sns
import os
import matplotlib.colors
import subprocess

from scipy import stats
from tqdm import tqdm
from datetime import datetime

from matplotlib import pyplot as plt
from matplotlib import patches as mpatches
from DocuHelpers import DocuHelpers
from BokehPlots import BokehPlots

# Bokeh libraries
from bokeh.io import output_file, output_notebook
from bokeh.plotting import figure, show, save
from bokeh.models import ColumnDataSource, LabelSet, HoverTool, FactorRange, DataTable, DateFormatter, TableColumn
from bokeh.layouts import row, column, gridplot
from bokeh.models.widgets import Tabs, Panel
from bokeh.transform import dodge

# rndPy
from rndPy.plotting import set_theme
set_theme(theme="optum")
plt.rcParams['figure.dpi'] = 150

# Set color theme lists
themes = {'matplotlib': ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b", "#e377c2", "#7f7f7f", "#bcbd22", "#17becf"],
          'uhg': ["#003C72", "#0066F6", "#039009", "#B0D523", "#FCAE00", "#FFDA03", "#002444", "#003D93", "#005702"],
         'optum': ["#E87722", "#F2B411", "#A32A2E", "#422C88", "#078576", "#627D32", "#316BBE", "#D13F44", "#8061BC", "#6FC1B1", "#90BC53", "#282A2E", "#434448", "#63666A", "#888B8D", "#B1B3B3", "#D0D0CE", "#EFEFEE"
]}

timestamp_now = datetime.now().strftime("%A, %d %b %Y %I:%M %p")