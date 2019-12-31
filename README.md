# Data example with Obspy

## Summary

Working with one-hour long registers of three sensing channels we found:

- Unexpected timing of acquisition: [unexpected-times notebook](./notebook/unexpected-times.ipynb)
- Data preview seems correct: [data-preview notebook](./notebook/data-preview.ipynb)

## Up and running

On bash:

```bash
python -m venv venv
source ./venv/Scripts/activate
pip install -r requirements.txt
jupyter lab
```

## Why not conda?

[Obspy documentation](https://github.com/obspy/obspy/wiki#installation) encourages to work with `conda` but we're working with `pip` and `venv` instead considering recent [not resolved issues](https://github.com/jupyter/notebook/issues/4909) of using `conda` along with JupyterLab.
