
class BaseWindow(object):
    def __init__(self, size=(512, 512)):
        self.size = size
        self._behaviours = []

    def add_behaviour(self, behaviour):
        self._behaviours.append(behaviour)
        return self

    def show(self):
        raise NotImplementedError()


class Behaviour(object):
    class Params(object):
        """The parameters provided by the window to the behaviours.

        Attributes
        ----------
            window: A reference to the window object
            scene: A reference to the scene
            stop_propagation: bool, when set no more behaviours will be run
            done: bool, when set remove this behaviour from the list
            refresh: bool, when set make sure to redraw the window
        """
        def __init__(self, window, scene):
            self.window = window
            self.scene = scene

            self._stop = False
            self._done = False
            self._refresh = False

        @property
        def stop_propagation(self):
            return self._stop

        @stop_propagation.setter
        def stop_propagation(self, s):
            self._stop = s

        @property
        def done(self):
            return self._done

        @done.setter
        def done(self, d):
            self._done = d

        @property
        def refresh(self):
            return self._refresh

        @refresh.setter
        def refresh(self, r):
            self._refresh = self._refresh or (r == True)

    def behave(self, params):
        raise NotImplementedError()
