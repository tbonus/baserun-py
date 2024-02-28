import json
from typing import Optional, Any, Union

from baserun import Baserun


def convert_to_score(x):
    return x if isinstance(x, int) else int(x is True)


def check(
    name: str,
    actual: Any,
    expected: Any,
    score: float,
    metadata: Optional[dict[str, Any]] = None,
    eval_type: Optional[str] = None,
):
    Baserun.evals._store_eval_data(
        name=name,
        eval_type=eval_type or "match",
        result=json.dumps(actual),
        score=score,
        submission=json.dumps(expected),
        payload=metadata or {},
    )

    return actual


def check_equals(
    name: str,
    actual: str,
    expected: Union[str, list[str]],
    metadata: Optional[dict[str, Any]] = None,
):
    expected_list = [expected] if isinstance(expected, str) else expected
    result = any(actual == item for item in expected_list)

    return check(
        name=name,
        eval_type="match",
        metadata=metadata,
        actual=actual,
        expected=expected,
        score=1.0 if result else 0.0,
    )


def check_includes(
    name: str,
    actual: str,
    expected: Union[str, list[str]],
    metadata: Optional[dict[str, Any]] = None,
):
    expected_list = [expected] if isinstance(expected, str) else expected
    result = any(item in actual for item in expected_list)

    return check(
        name=name,
        eval_type="match",
        metadata=metadata,
        actual=actual,
        expected=expected,
        score=1 if result else 0,
    )
