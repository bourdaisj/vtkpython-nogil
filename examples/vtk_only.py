import sys

print(f"GIL is enabled: {sys._is_gil_enabled()}")

import vtkmodules.vtkInteractionStyle
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkIOXML import vtkXMLPolyDataReader
import time
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonCore import (
    vtkDoubleArray,
    vtkPoints
)
from vtkmodules.vtkCommonDataModel import (
    vtkCellArray,
    vtkLine,
    vtkPolyData
)
from vtkmodules.vtkFiltersGeneral import vtkWarpVector
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)
import threading

print(f"GIL is enabled: {sys._is_gil_enabled()}")


def get_program_parameters():
    import argparse
    description = 'Read a polydata file.'
    epilogue = ''''''
    parser = argparse.ArgumentParser(description=description, epilog=epilogue,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('filename', help='Torso.vtp')
    args = parser.parse_args()
    return args.filename



def worker():
    """Function that runs in a separate thread"""
    for i in range(50):
        print(f"[Worker] iteration {i}", flush=True)
        time.sleep(1)


def main():
    colors = vtkNamedColors()

    filename = get_program_parameters()

    # Read all the data from the file
    reader = vtkXMLPolyDataReader()
    reader.SetFileName(filename)
    reader.Update()

    mapper = vtkPolyDataMapper()
    mapper.SetInputConnection(reader.GetOutputPort())

    actor = vtkActor()
    actor.SetMapper(mapper)

    renderer = vtkRenderer()
    renderer.AddActor(actor)
    renderer.SetBackground(colors.GetColor3d('cobalt_green'))

    renderWindow = vtkRenderWindow()
    renderWindow.AddRenderer(renderer)
    renderWindow.SetWindowName('WarpVector')

    renderWindowInteractor = vtkRenderWindowInteractor()
    renderWindowInteractor.SetRenderWindow(renderWindow)
    renderWindow.Render()

    thread = threading.Thread(target=worker, daemon=True)
    # Start the thread
    print("[Main] Starting worker thread...")
    thread.start()

    print("starting interactor")
    renderWindowInteractor.Start()


if __name__ == '__main__':
    main()
