# -*- coding: utf-8 -*-

import metalibm_functions.ml_log10
import metalibm_functions.ml_log1p
import metalibm_functions.ml_log2
import metalibm_functions.ml_log
import metalibm_functions.ml_exp
import metalibm_functions.ml_cbrt
import metalibm_functions.ml_vectorizable_log

from metalibm_core.core.ml_formats import ML_Binary32, ML_Binary64, ML_Int32
from metalibm_core.targets.common.vector_backend import VectorBackend

from valid.test_utils import *

# list of non-regression tests
# details on NewSchemeTest object can be found in valid.test_utils module
#   Each object requires a title, a function constructor and a list
#   of test cases (each is a dictionnary of parameters -> values)
new_scheme_function_list = [
  NewSchemeTest(
    "basic log test",
    metalibm_functions.ml_log.ML_Log,
    [{"precision": ML_Binary32}, {"precision": ML_Binary64}]
  ), 
  NewSchemeTest(
    "basic log1p test",
    metalibm_functions.ml_log1p.ML_Log1p,
    [{"precision": ML_Binary32}, {"precision": ML_Binary64}]
  ), 
  NewSchemeTest(
    "basic log2 test",
    metalibm_functions.ml_log2.ML_Log2,
    [{"precision": ML_Binary32}, {"precision": ML_Binary64}]
  ), 
  NewSchemeTest(
    "basic log10 test",
    metalibm_functions.ml_log10.ML_Log10,
    [{"precision": ML_Binary32}, {"precision": ML_Binary64}]
  ), 
  NewSchemeTest(
    "basic exp test",
    metalibm_functions.ml_exp.ML_Exponential,
    [{"precision": ML_Binary32}, {"precision": ML_Binary64}]
  ), 
  NewSchemeTest(
    "basic cubic square test",
    metalibm_functions.ml_cbrt.ML_Cbrt,
    [{"precision": ML_Binary32}, {"precision": ML_Binary64}]
  ), 
  NewSchemeTest(
    "basic vectorizable log scalar test",
    metalibm_functions.ml_vectorizable_log.ML_Log,
    [
      {"precision": ML_Binary32}, 
      {"precision": ML_Binary64},
    ]
  ), 
  NewSchemeTest(
    "vector exp test",
    metalibm_functions.ml_exp.ML_Exponential,
    [{"precision": ML_Binary32, "vector_size": 2, "target": VectorBackend()}, ]
  ), 
]


success = True
# list of TestResult objects generated by execution
# of new scheme tests
result_details = []

for test_scheme in new_scheme_function_list:
  test_result = test_scheme.perform_all_test()
  result_details.append(test_result)
  if not test_result.get_result(): 
    success = False

# Printing test summary for new scheme
for result in result_details:
  print result.get_details()

if success:
  print "OVERALL SUCCESS"
  exit(0)
else:
  print "OVERALL FAILURE"
  exit(1)
