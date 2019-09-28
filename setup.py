import setuptools

setuptools.setup(
        name="nginx-proxy-start-page",
        version="0.1",
        author="Adam Olech",
        author_email="nddr89@gmail.com",
        description="A landing page for your web applications",
        url="https://git.hopeburn.eu/extinct_potato/nginx-proxy-start-page",
        packages=["npsp"],
        python_requires='>=3.6',
        entry_points={
            "console_scripts": ["npsp = npsp.startpage:main"]
            },
        install_requires=["flask", "nginxparser_eb"],
        include_package_data=True,
        )
