# Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License").
# You may not use this file except in compliance with the License.
# A copy of the License is located at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# or in the "license" file accompanying this file. This file is distributed
# on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
# express or implied. See the License for the specific language governing
# permissions and limitations under the License.
from benchmarking.commons.hpo_main_simulator import main
from benchmarking.nursery.benchmark_hypertune.baselines import methods
from benchmarking.nursery.benchmark_hypertune.benchmark_definitions import (
    benchmark_definitions,
)


extra_args = [
    dict(
        name="--num_brackets",
        type=int,
        help="Number of brackets",
    ),
    dict(
        name="--num_samples",
        type=int,
        default=50,
        help="Number of samples for Hyper-Tune distribution",
    ),
]


def map_extra_args(args) -> dict:
    return dict(
        num_brackets=args.num_brackets,
        num_samples=args.num_samples,
    )


if __name__ == "__main__":
    main(methods, benchmark_definitions, extra_args, map_extra_args)
