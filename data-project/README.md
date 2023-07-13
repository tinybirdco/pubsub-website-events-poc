## How can I quickly load these Tinybird resources into my Workspace?

* Clone this repository and change to the `./data-project` folder
* Create a new Workspace to host this demo.
* Grab a Token from that Workspace.
* Use the CLI and login/authenticate to your Workspace, `tb auth`.
* Push these resources to the Workspace, `tb push`


## Working with the Tinybird CLI

To start working with data projects as if they were software projects, let's install the Tinybird CLI in a virtual environment.
Check the [CLI documentation](https://docs.tinybird.co/cli.html) for other installation options and troubleshooting.

```bash
virtualenv -p python3 .e
. .e/bin/activate
pip install tinybird-cli
tb auth --interactive
```
