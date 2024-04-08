"""The module contains interfaces for attribute reduction algorithms"""

__version__ = "0.1"

__all__ = [
    "SupervisedAttributeReductionAlgorithmParameters",
    "UnsupervisedAttributeReductionAlgorithmParameters",
    "UnsupervisedNumericalProcessingAttributeReductionAlgorithmParameters",
    "VarTypeEnum"
]

from .reduction_algorithm_parameters import (
    SupervisedAttributeReductionAlgorithmParameters,
    UnsupervisedAttributeReductionAlgorithmParameters,
    UnsupervisedNumericalProcessingAttributeReductionAlgorithmParameters,
    VarTypeEnum,
)
