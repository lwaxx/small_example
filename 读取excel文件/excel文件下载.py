import base64
from django.http.response import Http404, HttpResponse
def excel(self):
    # file = get_file('20201224113814900298.xls')
    file = "0M8R4KGxGuEAAAAAAAAAAAAAAAAAAAAAPgADAP7/CQAGAAAAAAAAAAAAAAABAAAAAQAAAAAAAAAAEAAAKQAAAAEAAAD+////AAAAAAAAAAD////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////9////LQAAAAMAAAAEAAAABQAAAAYAAAAHAAAACAAAAAkAAAAKAAAACwAAAAwAAAANAAAADgAAAA8AAAAQAAAAEQAAABIAAAATAAAAFAAAABUAAAAWAAAAFwAAABgAAAAZAAAAGgAAABsAAAAcAAAAHQAAAB4AAAAfAAAAIAAAACEAAAAiAAAAIwAAACQAAAAlAAAAJgAAACcAAAAoAAAA/v////7///8rAAAALAAAAC4AAAD+/////v///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////1IAbwBvAHQAIABFAG4AdAByAHkAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAWAAUA//////////8CAAAAIAgCAAAAAADAAAAAAAAARgAAAAAAAAAAAAAAAGBOF76PLdYBKgAAAEAHAAAAAAAAVwBvAHIAawBiAG8AbwBrAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABIAAgH///////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAGUwAAAAAAABFAFQARQB4AHQARABhAHQAYQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFAACAQEAAAADAAAA/////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAaAwAAAAAAAAUAUwB1AG0AbQBhAHIAeQBJAG4AZgBvAHIAbQBhAHQAaQBvAG4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoAAIB/////wQAAAD/////AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADQAAAOgBAAAAAAAACQgQAAAGBQC7Dc0HwYABAAYGAADhAAIAsATBAAIAAADiAAAAXABwAA0AAUEAZABtAGkAbgBpAHMAdAByAGEAdABvAHIAICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBCAAIAsARhAQIAAADAAQAAPQECAAMAGQACAAAAEgACAAAAEwACAAAArwECAAAAvAECAAAAPQASAAAAAAB0XgkzOAAAAAAAAQBYAkAAAgAAAI0AAgAAACIAAgAAAA4AAgABALcBAgAAANoAAgAAADEAFADwAAAA/3+QAQAAAACGAAIBi1tTTzEAFAAAAAAA/3+QAQAAAACGAAIBi1tTTzEAFAAAAAAA/3+QAQAAAACGAAIBi1tTTzEAFAAAAAAA/3+QAQAAAACGAAIBi1tTTzEAFADwAAAA/3+8AgAAAACGAAIBi1tTTzEAFADwAAAACgCQAQAAAACGAAIBi1tTTzEAFABAAQAACACQAQAAAACGAAIBi1tTTzEAFABAAQAA/3+QAQAAAACGAAIBi1tTTzEAFABAAQAA/3+8AgAAAACGAAIBi1tTTzEAFABAAQAACgCQAQAAAACGAAIBi1tTTzEAFABAAQAA/3+QAQAAAACGAAIBi1tTTzEAFABAAQAACgCQAQAAAACGAAIBi1tTTzEAFADcAAAACQCQAQAAAACGAAIBi1tTTzEAFADcAAAAPwC8AgAAAACGAAIBi1tTTzEAFAAEAQAAPgC8AgAAAACGAAIBi1tTTzEAFADcAAAACgCQAQAAAACGAAIBi1tTTzEAFADcAAAACACQAQAAAACGAAIBi1tTTzEAFAAsAQAAPgC8AgAAAACGAAIBi1tTTzEAFADcAAAAPgCQAQAAAACGAAIBi1tTTzEAFADcAAAAEACQAQAAAACGAAIBi1tTTzEAFADcAAAACQC8AgAAAACGAAIBi1tTTzEAFADcAAAAPgC8AgAAAACGAAIBi1tTTzEAFABoAQAAPgC8AgAAAACGAAIBi1tTTzEAFADcAAAADACQAQAAAQCGAAIBi1tTTzEAFADcAAAANQC8AgAAAACGAAIBi1tTTzEAFADcAAAANQCQAQAAAACGAAIBi1tTTzEAFADcAAAACAC8AgAAAACGAAIBi1tTTzEAFADcAAIAFwCQAQAAAACGAAIBi1tTTzEAFADcAAAAFACQAQAAAQCGAAIBi1tTTzEAFADcAAAAEwCQAQAAAACGAAIBi1tTTzEAFADcAAAAEQCQAQAAAACGAAIBi1tTTzEAFADcAAAACACQAQAAAACGAAIBi1tTTx4EKwAFABMAASIA5f8iACMALAAjACMAMAA7ACIA5f8iAFwALQAjACwAIwAjADAAHgQ1AAYAGAABIgDl/yIAIwAsACMAIwAwADsAWwBSAGUAZABdACIA5f8iAFwALQAjACwAIwAjADAAHgQ3AAcAGQABIgDl/yIAIwAsACMAIwAwAC4AMAAwADsAIgDl/yIAXAAtACMALAAjACMAMAAuADAAMAAeBEEACAAeAAEiAOX/IgAjACwAIwAjADAALgAwADAAOwBbAFIAZQBkAF0AIgDl/yIAXAAtACMALAAjACMAMAAuADAAMAAeBGkAKgAyAAFfACAAIgDl/yIAKgAgACMALAAjACMAMABfACAAOwBfACAAIgDl/yIAKgAgAFwALQAjACwAIwAjADAAXwAgADsAXwAgACIA5f8iACoAIAAiAC0AIgBfACAAOwBfACAAQABfACAAHgRXACkAKQABXwAgACoAIAAjACwAIwAjADAAXwAgADsAXwAgACoAIABcAC0AIwAsACMAIwAwAF8AIAA7AF8AIAAqACAAIgAtACIAXwAgADsAXwAgAEAAXwAgAB4EeQAsADoAAV8AIAAiAOX/IgAqACAAIwAsACMAIwAwAC4AMAAwAF8AIAA7AF8AIAAiAOX/IgAqACAAXAAtACMALAAjACMAMAAuADAAMABfACAAOwBfACAAIgDl/yIAKgAgACIALQAiAD8APwBfACAAOwBfACAAQABfACAAHgRnACsAMQABXwAgACoAIAAjACwAIwAjADAALgAwADAAXwAgADsAXwAgACoAIABcAC0AIwAsACMAIwAwAC4AMAAwAF8AIAA7AF8AIAAqACAAIgAtACIAPwA/AF8AIAA7AF8AIABAAF8AIAAeBC8AFwAVAAFcACQAIwAsACMAIwAwAF8AKQA7AFwAKABcACQAIwAsACMAIwAwAFwAKQAeBDkAGAAaAAFcACQAIwAsACMAIwAwAF8AKQA7AFsAUgBlAGQAXQBcACgAXAAkACMALAAjACMAMABcACkAHgQ7ABkAGwABXAAkACMALAAjACMAMAAuADAAMABfACkAOwBcACgAXAAkACMALAAjACMAMAAuADAAMABcACkAHgRFABoAIAABXAAkACMALAAjACMAMAAuADAAMABfACkAOwBbAFIAZQBkAF0AXAAoAFwAJAAjACwAIwAjADAALgAwADAAXAApAB4EEQCwAAYAATAALgAwADAAXwAgAB4ECwCxAAMAATAAXwAgAOAAFAAAAAAA9f8QAAAAAAAAAAAAAADAIOAAFAABAAAA9f8QAAD0AAAAAAAAAADAIOAAFAABAAAA9f8QAAD0AAAAAAAAAADAIOAAFAACAAAA9f8QAAD0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AAAAAAAAAAAAABsAAAACAA0AFAACAAAAgACA/wAAAAAAAAAADgAFAAJ9CHgAfQgAAAAAAAAAAAAAAAAcAAAABQAJABQAAgAAALKysv8AAAAAAAAAAAoAFAACAAAAsrKy/wAAAAAAAAAABwAUAAIAAACysrL/AAAAAAAAAAAIABQAAgAAALKysv8AAAAAAAAAAAQAFAACAAAA///M/wAAAAAAAAAAfQhBAH0IAAAAAAAAAAAAAAAAHQAAAAMABAAUAAMAMjMFAAAAAAAAAAAAAAANABQAAwAAAAAAAAAAAAAAAAAAAA4ABQACfQgtAH0IAAAAAAAAAAAAAAAAHgAAAAIADQAUAAMAAAADAAAAAAAAAAAAAAAOAAUAAn0ILQB9CAAAAAAAAAAAAAAAAB8AAAACAA0AFAACAAAA/wAA/wAAAAAAAAAADgAFAAJ9CC0AfQgAAAAAAAAAAAAAAAAgAAAAAgANABQAAwAAAAMAAAAAAAAAAAAAAA4ABQABfQgtAH0IAAAAAAAAAAAAAAAAIQAAAAIADQAUAAIAAAB/f3//AAAAAAAAAAAOAAUAAn0IQQB9CAAAAAAAAAAAAAAAACIAAAADAAgAFAADAAAABAAAAAAAAAAAAAAADQAUAAMAAAADAAAAAAAAAAAAAAAOAAUAAn0IQQB9CAAAAAAAAAAAAAAAACMAAAADAAgAFAADAP8/BAAAAAAAAAAAAAAADQAUAAMAAAADAAAAAAAAAAAAAAAOAAUAAn0IQQB9CAAAAAAAAAAAAAAAACQAAAADAAQAFAADADIzBAAAAAAAAAAAAAAADQAUAAMAAAAAAAAAAAAAAAAAAAAOAAUAAn0IQQB9CAAAAAAAAAAAAAAAACUAAAADAAgAFAADADIzBAAAAAAAAAAAAAAADQAUAAMAAAADAAAAAAAAAAAAAAAOAAUAAn0IQQB9CAAAAAAAAAAAAAAAACYAAAADAAQAFAADADIzBwAAAAAAAAAAAAAADQAUAAMAAAAAAAAAAAAAAAAAAAAOAAUAAn0IkQB9CAAAAAAAAAAAAAAAACcAAAAHAAkAFAACAAAAPz8//wAAAAAAAAAACgAUAAIAAAA/Pz//AAAAAAAAAAAHABQAAgAAAD8/P/8AAAAAAAAAAAgAFAACAAAAPz8//wAAAAAAAAAABAAUAAIAAADy8vL/AAAAAAAAAAANABQAAgAAAD8/P/8AAAAAAAAAAA4ABQACfQiRAH0IAAAAAAAAAAAAAAAAKAAAAAcACQAUAAIAAAB/f3//AAAAAAAAAAAKABQAAgAAAH9/f/8AAAAAAAAAAAcAFAACAAAAf39//wAAAAAAAAAACAAUAAIAAAB/f3//AAAAAAAAAAAEABQAAgAAAPLy8v8AAAAAAAAAAA0AFAACAAAA+n0A/wAAAAAAAAAADgAFAAJ9CJEAfQgAAAAAAAAAAAAAAAApAAAABwAJABQAAgAAAD8/P/8AAAAAAAAAAAoAFAACAAAAPz8//wAAAAAAAAAABwAUAAIAAAA/Pz//AAAAAAAAAAAIABQAAgAAAD8/P/8AAAAAAAAAAAQAFAACAAAApaWl/wAAAAAAAAAADQAUAAMAAAAAAAAAAAAAAAAAAAAOAAUAAn0IQQB9CAAAAAAAAAAAAAAAACoAAAADAAQAFAADAGVmCQAAAAAAAAAAAAAADQAUAAMAAAABAAAAAAAAAAAAAAAOAAUAAn0IQQB9CAAAAAAAAAAAAAAAACsAAAADAAQAFAADAAAABQAAAAAAAAAAAAAADQAUAAMAAAAAAAAAAAAAAAAAAAAOAAUAAn0IQQB9CAAAAAAAAAAAAAAAACwAAAADAAgAFAACAAAA/4AB/wAAAAAAAAAADQAUAAIAAAD6fQD/AAAAAAAAAAAOAAUAAn0IVQB9CAAAAAAAAAAAAAAAAC0AAAAEAAcAFAADAAAABAAAAAAAAAAAAAAACAAUAAMAAAAEAAAAAAAAAAAAAAANABQAAwAAAAEAAAAAAAAAAAAAAA4ABQACfQhBAH0IAAAAAAAAAAAAAAAALgAAAAMABAAUAAIAAADG787/AAAAAAAAAAANABQAAgAAAABhAP8AAAAAAAAAAA4ABQACfQhBAH0IAAAAAAAAAAAAAAAALwAAAAMABAAUAAIAAAD/65z/AAAAAAAAAAANABQAAgAAAJxlAP8AAAAAAAAAAA4ABQACfQhBAH0IAAAAAAAAAAAAAAAAMAAAAAMABAAUAAMAZWYIAAAAAAAAAAAAAAANABQAAwAAAAEAAAAAAAAAAAAAAA4ABQACfQhBAH0IAAAAAAAAAAAAAAAAMQAAAAMABAAUAAMAAAAEAAAAAAAAAAAAAAANABQAAwAAAAAAAAAAAAAAAAAAAA4ABQACfQhBAH0IAAAAAAAAAAAAAAAAMgAAAAMABAAUAAMAZWYEAAAAAAAAAAAAAAANABQAAwAAAAEAAAAAAAAAAAAAAA4ABQACfQhBAH0IAAAAAAAAAAAAAAAAMwAAAAMABAAUAAMAzEwEAAAAAAAAAAAAAAANABQAAwAAAAEAAAAAAAAAAAAAAA4ABQACfQhBAH0IAAAAAAAAAAAAAAAANAAAAAMABAAUAAMAZWYFAAAAAAAAAAAAAAANABQAAwAAAAEAAAAAAAAAAAAAAA4ABQACfQhBAH0IAAAAAAAAAAAAAAAANQAAAAMABAAUAAMAzEwFAAAAAAAAAAAAAAANABQAAwAAAAEAAAAAAAAAAAAAAA4ABQACfQhBAH0IAAAAAAAAAAAAAAAANgAAAAMABAAUAAMAAAAGAAAAAAAAAAAAAAANABQAAwAAAAAAAAAAAAAAAAAAAA4ABQACfQhBAH0IAAAAAAAAAAAAAAAANwAAAAMABAAUAAMAAAAHAAAAAAAAAAAAAAANABQAAwAAAAAAAAAAAAAAAAAAAA4ABQACfQhBAH0IAAAAAAAAAAAAAAAAOAAAAAMABAAUAAMAZWYHAAAAAAAAAAAAAAANABQAAwAAAAEAAAAAAAAAAAAAAA4ABQACfQhBAH0IAAAAAAAAAAAAAAAAOQAAAAMABAAUAAMAzEwHAAAAAAAAAAAAAAANABQAAwAAAAEAAAAAAAAAAAAAAA4ABQACfQhBAH0IAAAAAAAAAAAAAAAAOgAAAAMABAAUAAMAAAAIAAAAAAAAAAAAAAANABQAAwAAAAAAAAAAAAAAAAAAAA4ABQACfQhBAH0IAAAAAAAAAAAAAAAAOwAAAAMABAAUAAMAzEwIAAAAAAAAAAAAAAANABQAAwAAAAEAAAAAAAAAAAAAAA4ABQACfQhBAH0IAAAAAAAAAAAAAAAAPAAAAAMABAAUAAMAMjMIAAAAAAAAAAAAAAANABQAAwAAAAAAAAAAAAAAAAAAAA4ABQACfQhBAH0IAAAAAAAAAAAAAAAAPQAAAAMABAAUAAMAAAAJAAAAAAAAAAAAAAANABQAAwAAAAAAAAAAAAAAAAAAAA4ABQACfQhBAH0IAAAAAAAAAAAAAAAAPgAAAAMABAAUAAMAzEwJAAAAAAAAAAAAAAANABQAAwAAAAEAAAAAAAAAAAAAAA4ABQACfQhBAH0IAAAA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AP0ACgABAAMASAAEAAAA/QAKAAEABABIAAUAAAD9AAoAAQAFAEgABgAAAP0ACgABAAYASAAHAAAA/QAKAAEABwBIAAgAAAD9AAoAAQAIAEgACQAAAP0ACgABAAkASAAKAAAA/QAKAAEACgBRAAsAAAD9AAoAAQALAEgADAAAAP0ACgABAAwASAANAAAA/QAKAAEADQBIAA4AAAD9AAoAAQAOAFEADwAAAP0ACgABAA8AUQAQAAAA/QAKAAEAEABRABEAAAD9AAoAAQARAFEAEgAAAP0ACgABABIAUQATAAAA/QAKAAEAEwBIABQAAAD9AAoAAQAUAFEAFQAAAP0ACgABABUAUQAWAAAAAQIGAAEAFgBZAP0ACgACAAAASQAXAAAA/QAKAAIAAQBJABgAAAD9AAoAAgACAEkAGQAAAP0ACgACAAMASQAaAAAA/QAKAAIABABJABsAAAD9AAoAAgAFAEkAHAAAAP0ACgACAAYASQAdAAAA/QAKAAIABwBJAB4AAAD9AAoAAgAIAEkAHwAAAP0ACgACAAkASQAgAAAA/QAKAAIACgBSACEAAAD9AAoAAgALAEkAIgAAAP0ACgACAAwASQAjAAAA/QAKAAIADQBJACQAAAD9AAoAAgAOAFMAJQAAAP0ACgACAA8AUwAmAAAA/QAKAAIAEABTACcAAAD9AAoAAgARAFMAKAAAAP0ACgACABIAUwApAAAA/QAKAAIAEwBJACoAAAD9AAoAAgAUAEkAKwAAAL4ACgACABUAWgBbABYA/QAKAAMAAABKACwAAAD9AAoAAwABAEsALQAAAP0ACgADAAIATAAuAAAA/QAKAAMAAwBNAC8AAAD9AAoAAwAEAEsAMAAAAP0ACgADAAUATgAxAAAA/QAKAAMABgBOADIAAAB+AgoAAwAHAE8AACiLQP0ACgADAAgASwAzAAAA/QAKAAMACQBUADQAAAC9ABIAAwAKAEwAAADwP1UA1vDQBAsA/QAKAAMADABVADUAAAB+AgoAAwANAE8AACiLQAECBgADAA4ASwD9AAoAAwAPAE4AMQAAAAECBgADABAATQD9AAoAAwARAE4ANgAAAP0ACgADABIAXAA3AAAAfgIKAAMAEwBLAB7x0AT9AAoAAwAUAFUAOAAAAAMCDgADABUAXQDIpT/4kUoJQ/0ACgAEAAAASgAsAAAA/QAKAAQAAQBLAC0AAAD9AAoABAACAEwAOQAAAP0ACgAEAAMATQA6AAAA/QAKAAQABABLADAAAAD9AAoABAAFAE4AMQAAAP0ACgAEAAYATgA7AAAAfgIKAAQABwBPAABYg0D9AAoABAAIAEsAMwAAAP0ACgAEAAkAVAA8AAAAvQASAAQACgBMAAAA8D9VANbw0AQLAP0ACgAEAAwAXgA9AAAAfgIKAAQADQBPAABYg0ABAgYABAAOAEsA/QAKAAQADwBOADEAAAABAgYABAAQAE0A/QAKAAQAEQBOADYAAAD9AAoABAASAFwANwAAAH4CCgAEABMASwAe8dAE/QAKAAQAFABVADgAAAADAg4ABAAVAF0A+Nc/+JFKCUO+ADQABQAAAFAAUABQAFAAUABQAFAAUABQAFAAVgBQAFAAUABWAFYAVgBWAFYAUABWAFYAWAAWAL4ANAAGAAAAUABQAFAAUABQAFAAUABQAFAAUABWAFAAUABQAFYAVgBWAFYAVgBQAFYAVgBYABYAvgA0AAcAAABQAFAAUABQAFAAUABQAFAAUABQAFYAUABQAFAAVgBWAFYAVgBWAFAAVgBWAFgAFgC+ADQACAAAAFAAUABQAFAAUABQAFAAUABQAFAAVgBQAFAAUABWAFYAVgBWAFYAUABWAFYAWAAWAL4ANAAJAAAAUABQAFAAUABQAFAAUABQAFAAUABWAFAAUABQAFYAVgBWAFYAVgBQAFYAVgBYABYAvgA0AAoAAABQAFAAUABQAFAAUABQAFAAUABQAFYAUABQAFAAVgBWAFYAVgBWAFAAVgBWAFgAFgC+ADQACwAAAFAAUABQAFAAUABQAFAAUABQAFAAVgBQAFAAUABWAFYAVgBWAFYAUABWAFYAWAAWAL4ANAAMAAAAUABQAFAAUABQAFAAUABQAFAAUABWAFAAUABQAFYAVgBWAFYAVgBQAFYAVgBYABYAvgA0AA0AAABQAFAAUABQAFAAUABQAFAAUABQAFYAUABQAFAAVgBWAFYAVgBWAFAAVgBWAFgAFgC+ADQADgAAAFAAUABQAFAAUABQAFAAUABQAFAAVgBQAFAAUABWAFYAVgBWAFYAUABWAFYAWAAWAL4ANAAPAAAAUABQAFAAUABQAFAAUABQAFAAUABWAFAAUABQAFYAVgBWAFYAVgBQAFYAVgBYABYAvgA0ABAAAABQAFAAUABQAFAAUABQAFAAUABQAFYAUABQAFAAVgBWAFYAVgBWAFAAVgBWAFgAFgD9AAoAEQAAAEUAPgAAAL4AHgARAAoAVwBYAFgAWABXAFcAVwBXAFcAWABXAFcAFQC+AB4AEgAKAFcAWABYAFgAVwBXAFcAVwBXAFgAVwBXABUAvgAeABMACgBXAFgAWABYAFcAVwBXAFcAVwBYAFcAVwAVANcALACmCQAAfAE8AD4BNAEqASoBOAA4ADgAOAA4ADgAOAA4ADgAOAA4ADgAMAAiAD4CEgC2DgAAAABAAAAAAABkAAAAAACgAAQARgBkAB0ADwADBQAFAAAAAQAFAAUABQWZAAIAwAjlAAoAAQAAAAAAAwAVAGcIFwBnCAAAAAAAAAAAAAACAAH/////A0QAAAoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQAAAAIAAAADAAAABAAAAAUAAAAGAAAABwAAAAgAAAAJAAAACgAAAAsAAAAMAAAA/v///w4AAAAPAAAAEAAAABEAAAASAAAAEwAAABQAAAD+////FgAAABcAAAAYAAAAGQAAABoAAAAbAAAAHAAAAP7///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////8JCBAAAQYAD5oC1QcAAAAACAAAAPsP/gKLWXrLXwD///8BAADA/wAAAAAAAMD/AAAAAAAAwP8AAAAAAADA/wAAAAAAAMD/AAAAAAAAwP8AAAAAAADA/wAAAAAAAMD/AAAAAAAAwP8AAAAAAADA/wAAAAAAAMD/AAAAAAAAwP8AAAAAAADA/wAAAAAAAMD/AAAAAAAAwP8AAAAAAAAAAAAAAAEAAAAAAADgAAAAwP8A/v8AAADA/wAAAAEAAAAAAAAAAQAAAAAAAOAAAADA/wAA4AAAAMD/AAAAAQAAAAAAAOAAAADA/wAAAAAAAMD/AAAAAQAAAAAAAAAAAADA/wD+/wAAAAAAAADgAAAAwP8AAAAAAADA/wAAAAAAAMD/AAAAAAAAwP8AAAAAAADA/wD+HwAAAMD/AP4fAAAAwP8AAOAAAADA/wD+HwAAAMD/AADgAAAAwP8A/v8AAADA/wD+/wAAAMD/AP7/AAAAwP8AAOAAAADA/wAA4AAAAMD/AP4fAAAAwP8A/h8AAADA/wAA4AAAAMD/AADgAAAAwP8AAOAAAADA/wAA4AAAAMD/AADgAAAAwP8AAOAAAADA/wAA4AAAAMD/AADgAAAAwP8AAOAAAADA/wAA4AAAAMD/AADgAAAA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"
    file_data = base64.b64decode(file)

    the_file_name = '人行信息报备表.xls'

    try:
        response = HttpResponse(file_data)
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;filename="{0}"'.format(the_file_name)

        return response
    except Exception:
        raise Http404