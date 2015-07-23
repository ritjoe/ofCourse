import pkg_resources
      install_requires=['ofcourse>={version}'],
     )""".format(version=pkg_resources.get_distribution('ofcourse').version),
def push(name, api, domain):
    set_deploy_branch(name, branch, api, domain)
    remote = git_url(name, api, domain)
    return get_app(name, api, domain)['app_url']
def new_app(name, api, domain, wait_until_available=True):
        get_app(name, api, domain)
    api.app_create(name, ['python-2.7'], domain_name=domain)
            app = get_app(name, api, domain)
def get_app(name, api, domain):
    apps = [a for a in api.app_list(domain_name=domain)[1]
            if a.get("name", "") == name]
def git_url(name, api, domain):
    app = get_app(name, api, domain)
def set_deploy_branch(name, branch, api, domain):
    app = get_app(name, api, domain)
        api.app_action('UPDATE', name, domain_name=domain,
                       deployment_branch=branch)