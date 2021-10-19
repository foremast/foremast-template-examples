# This file should live in your home directory at ~/.foremast/config.py
# When developing locally you can reference this via symlink in the foremast project
# ln -s ~/.foremast/config.py config.py

__version__ = '2021-10-19'
print('Using configuration from config.py, using version: {}'.format(__version__))

gitlab_token = "<Gitlab API Token to fetch remote configs>"

CONFIG = {
    'base': {
        'domain': 'company.com',
        'envs': 'dev,stage,prod',
        'env_configs': {
            "build": {
                "enable_approval_skip": True
            },
            "stage": {
                "enable_approval_skip": True
            },
            "prod": {
                "enable_approval_skip": False
            }
        },
        'regions': 'us-east-1',
        'git_url': 'https://gitlab.com',
        'gate_api_url': 'http://spinnaker.company.com/api/v1',
        #'gate_ca_bundle': '<x509 CA Auth used by Spinnaker Gate>',
        #'gate_client_cert': '<x509 Client PEM Certificate for API Authentication to Spinnaker Gate>',
        'templates_path': '<Path to root of foremast-templates folder>',
        'runway_base_path': 'runway',
        'default_ec2_securitygroups': {
            'build': [],
            'stage': [],
            'int': [],
            'prod': []
        },
        'default_elb_securitygroups': {
            'build': [],
            'stage': [],
            'int': [],
            'prod': [],
        },
        'default_securitygroup_rules': {}
    },
    'credentials': {
        'gitlab_token': gitlab_token,
        'gate_authentication': {
            #'github': {
            #    'token': '<Github Auth Token here>'
            #}
            'google_iap': {
                'oauth_client_id': '<Google IAP OAuth Client ID>',
                'sa_credentials_path': '<Path to Google Service Account Allowed via GCP IAP Console to login>'
            }
        }
    },
    'formats': {
        'domain': 'company.com',
        'app': '{repo}{project}',
        'iam_policy': 'iam-{project}_{repo}_policy',
        'iam_profile': '{project}_{repo}_profile',
        'jenkins_job_name': 'a_{project}_{repo}',
        's3_app_bucket': '{repo}.{project}.{env}.{domain}',
        'shared_s3_app_bucket': 'shared.{repo}.{project}.{env}.{domain}',
        's3_app_region_bucket': '{repo}.{project}.{region}.{env}.{domain}',
        'shared_s3_app_region_bucket': 'shared.{repo}.{project}.{region}.{env}.{domain}'
    },
    'task_timeouts': {
        "envs": "{\"stage\":{\"deleteScalingPolicy\": 600, \"upsertScalingPolicy\": 600}}"
    },
    'links': {
        'Metrics and Logging': {
            'Prometheus - Metrics': ':9090/metrics',
        }
    }
}
