#!/usr/bin/env python3

import aws_cdk as cdk

from cdk_trainig.cdk_trainig_stack import CdkTrainigStack


app = cdk.App()
CdkTrainigStack(app, "cdk-trainig")

app.synth()
