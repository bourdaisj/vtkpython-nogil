about VTK, there is currently no publicly distributed wheel compatible with a free-threaded python build

current problems: - 'aiohttp._http_writer', which has not declared that it can run safely without the GIL.

python PEP: https://peps.python.org/pep-0703

Running with PYTHON_GIL=0 python app.py forces the GIL to remain disable, 
https://peps.python.org/pep-0703/#immortalization

see https://peps.python.org/pep-0703/#pythongil-environment-variable
actually its PYTHON_GIL


=> demander a Alexy pour build vtk wheel against custom python