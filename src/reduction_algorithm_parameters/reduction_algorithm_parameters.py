from dataclasses import dataclass
from enum import Enum
from functools import total_ordering


@dataclass(frozen=True, kw_only=True)
class AttributeReductionAlgorithmParameters:
    """Базовый класс параметров алгоритма редукции атрибутов"""

    input_file: str
    output_file: str
    output_perf_file: str | None = None


@dataclass(frozen=True, kw_only=True)
class SupervisedAttributeReductionAlgorithmParameters(
    AttributeReductionAlgorithmParameters
):
    """Аргументы алгоритма сокращения атрибутов с учителем"""

    input_var_columns: list[str]
    output_var_columns: list[str]


@dataclass(frozen=True, kw_only=True)
class UnsupervisedAttributeReductionAlgorithmParameters(
    AttributeReductionAlgorithmParameters
):
    """Аргументы алгоритма сокращения атрибутов без учителя"""

    var_columns: list[str]


@total_ordering
class VarTypeEnum(Enum):
    NUMERICAL = "NUMERICAL"
    NOMINAL = "NOMINAL"

    def __lt__(self, other):
        if self.__class__ is other.__class__:
            return self.value < other.value
        return NotImplemented

    def __repr__(self):
        cls_name = self.__class__.__name__
        return f"{cls_name}.{self.name}"


@dataclass(frozen=True, kw_only=True)
class UnsupervisedNumericalProcessingAttributeReductionAlgorithmParameters(
    UnsupervisedAttributeReductionAlgorithmParameters
):
    """Аргументы алгоритма сокращения атрибутов без учителя, способного обрабатывать количественные атрибуты"""

    var_column_types: list[VarTypeEnum]
