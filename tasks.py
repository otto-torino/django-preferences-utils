from invoke import task


@task
def clean_build(c):
    """
    Remove build artifacts
    """
    c.run("rm -fr build/")
    c.run("rm -fr dist/")
    c.run("rm -fr *.egg-info")


@task
def clean_pyc(c):
    """
    Remove python file artifacts
    """
    c.run("find . -name '*.pyc' -exec rm -f {} +")
    c.run("find . -name '*.pyo' -exec rm -f {} +")
    c.run("find . -name '*~' -exec rm -f {} +")


@task
def coverage(c):
    """
    check code coverage quickly with the default Python
    """
    c.run("coverage run --source preferences_utils runtests.py tests")
    c.run("coverage report -m")
    c.run("coverage html")
    c.run("xdg-open htmlcov/index.html")


@task
def test_all(c):
    """
    Run tests on every python version with tox
    """
    c.run("tox")


@task
def clean(c):
    """
    Remove python file and build artifacts
    """
    clean_build(c)
    clean_pyc(c)


@task
def unittest(c):
    """
    Run unittests
    """
    c.run("python manage.py test")


@task(help={'bumpsize': 'Bump either for a "feature" or "breaking" change'})
def release(c, bumpsize=''):
    """
    Package and upload a release
    """
    clean(c)
    if bumpsize:
        bumpsize = '--' + bumpsize

    import preferences_utils
    c.run("python setup.py sdist bdist_wheel")
    c.run("twine upload dist/*")

    c.run('git tag -a {version} -m "build: bumpe version number to {version}"'.format(version=preferences_utils.__version__))
    c.run("git push --tags")
    c.run("git push origin main")
