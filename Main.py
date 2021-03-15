import wx
import TUGAS1hello as mywx

if __name__ == '__main__':
    app = wx.App()
    frame = mywx.Frame(None)
    frame.Show()
    app.MainLoop()