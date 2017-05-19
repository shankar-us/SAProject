from django.http import FileResponse
from django.shortcuts import render
from django.http import HttpResponse


# def home(request):
#    return render(request, "SAMain\home.html")


def home(request):
    import random
    import django
    import datetime
    import PIL
    import io
    import os

    from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
    from matplotlib.figure import Figure
    from matplotlib.dates import DateFormatter
    from PIL import Image
    from django.contrib.sites.models import Site

    fig=Figure()
    ax=fig.add_subplot(111)
    x=[]
    y=[]
    now=datetime.datetime.now()
    delta=datetime.timedelta(days=1)
    for i in range(10):
        x.append(now)
        now+=delta
        y.append(random.randint(0, 1000))
    ax.plot_date(x, y, '-')
    ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))
    fig.autofmt_xdate()
    canvas=FigureCanvas(fig)
    response=django.http.HttpResponse(content_type='image/png')
    canvas.print_png(response)
    # return response

    fig.savefig('C:\Data\Python\AnacondaWorkspace\Learning\Django\SAEnv\SAProject\SAMain/templates\SAMain/to.png')
    # save the figure to file

    url = 'http://127.0.0.1:8000'
    filepath = 'SAMain\\test.png'
    #ax.close(fig)
    return render(request, 'SAMain\home.html',{'response': filepath})
