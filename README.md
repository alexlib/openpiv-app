# openpiv-app
Simple particle image velocimetry analysis app with streamlit. Upload a pair of images or use the included demo and perform Fourier transform based cross-correlation PIV analysis. Adjust the parameters to see how this affects results. For more info about PIV method, see OpenPIV basics https://github.com/OpenPIV/openpiv_basics



<p align="center">
<img src="https://github.com/alexlib/openpiv-app/blob/master/screenshot.jpg" width="700">
</p>

## Run with Docker
From the root dir:
```
    docker build -t alexlib/openpiv-app .
    docker run -p 8501:8501 alexlib/openpiv-app:latest
```
Then visit [localhost:8501](http://localhost:8501/)

## Development
Using [devcontainer](https://code.visualstudio.com/docs/remote/containers), see basic python [example repo](https://github.com/microsoft/vscode-remote-try-python) and [more advanced repo](https://github.com/microsoft/python-sample-tweeterapp). Use [this streamlit docker template](https://github.com/MrTomerLevi/streamlit-docker). Note you cannot docker run at the same time as the devcontainer as the ports clash.


## References
The app is an edited fork of this [great example](https://github.com/robmarkcole/object-detection-app)

## Relevant links
1. OpenPIV example in a Jupyter notebook https://github.com/alexlib/openpiv-python-example
1. OpenPIV website www.openpiv.net
2. PIVPy app for post-processing of PIV data https://github.com/alexlib/pivpy_streamlit_app

