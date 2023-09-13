#!/usr/bin/env python
from constructs import Construct
from cdktf import App, NamedRemoteWorkspace, TerraformStack, TerraformOutput, RemoteBackend
from cdktf_cdktf_provider_aws.provider import AwsProvider
from cdktf_cdktf_provider_aws.instance import Instance
from imports.aws.sns_topic import SnsTopic
from imports.terraform_aws_modules.aws import Vpc
from imports.aws.lambda_function import LambdaFunction
from imports.aws.iam_role import IamRole



class MyStack(TerraformStack):
    def __init__(self, scope: Construct, ns: str):
        super().__init__(scope, ns)

        AwsProvider(self, "AWS", region="eu-west-2")

        instance = Instance(self, "compute",
                            ami="ami-01456a894f71116f2",
                            instance_type="t2.micro",
                            tags={"Name": "CDKTF-Demo"},
                            )

        TerraformOutput(self, "public_ip",
                        value=instance.public_ip,
                        )

app = App()
stack = MyStack(app, "aws_instance")


app.synth()

