import wx

class MainWindow(wx.Frame):
    def __init__(self):
        wx.Frame.__init__( self, None, wx.ID_ANY, "test",
                style=wx.DEFAULT_FRAME_STYLE )
        print wx.Locale(wx.LANGUAGE_DEFAULT)
        dt = MyFileDropTarget( self )
        self.SetDropTarget( dt )
        self.Show(1)

class MyFileDropTarget(wx.FileDropTarget):
    def __init__(self, window):
        wx.FileDropTarget.__init__(self)
        self.window = window

    def OnDropFiles(self, x, y, filenames):
        print("\n%d file(s) dropped at %d,%d:\n" %
                              (len(filenames), x, y))

        for file in filenames:
            print(file + '\n')


def main():
    app = wx.PySimpleApp()
    frame = MainWindow()
    app.MainLoop()

if __name__ == '__main__':
    main()

"""
        dlg = wx.FileDialog(
            self, message="Choose a file", defaultDir=os.getcwd(), 
            defaultFile="", wildcard=wildcard, style=wx.OPEN | wx.MULTIPLE | wx.CHANGE_DIR
            )

        if dlg.ShowModal() == wx.ID_OK:
            # This returns a Python list of files that were selected.
            paths = dlg.GetPaths()

            self.log.WriteText('You selected %d files:' % len(paths))

            for path in paths:
                self.log.WriteText('           %s\n' % path)

        # Compare this with the debug above; did we change working dirs?
        # self.log.WriteText("CWD: %s\n" % os.getcwd())

        # Destroy the dialog. Don't do this until you are done with it!
        # BAD things can happen otherwise!
        dlg.Destroy()

"""

"""
        # In this case we include a "New directory" button. 
        dlg = wx.DirDialog(self, "Choose a directory:",
                          style=wx.DD_DEFAULT_STYLE|wx.DD_NEW_DIR_BUTTON)

        # If the user selects OK, then we process the dialog's data.
        # This is done by getting the path data from the dialog - BEFORE
        # we destroy it. 
        if dlg.ShowModal() == wx.ID_OK:
            pass
        #   self.log.WriteText('You selected: %s\n' % dlg.GetPath())

        # Only destroy a dialog after you're done with it.
        dlg.Destroy()

"""
