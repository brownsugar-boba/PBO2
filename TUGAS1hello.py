# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class wx.Frame
###########################################################################

class Frame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,400 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.Size( 500,400 ), wx.Size( -1,-1 ) )
		self.SetFont( wx.Font( 12, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Comic Sans MS" ) )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.SetBackgroundColour( wx.Colour( 191, 101, 245 ) )

		wxBoxSizer = wx.BoxSizer( wx.VERTICAL )

		wxBoxSizer.SetMinSize( wx.Size( -1,1 ) )
		self.nama_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.nama_panel.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		self.nama_panel.SetMinSize( wx.Size( 800,-1 ) )

		nama_grid = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText1 = wx.StaticText( self.nama_panel, wx.ID_ANY, u"Dinda Putri Ani", wx.Point( 100,100 ), wx.Size( -1,-1 ), wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText1.Wrap( -1 )

		self.m_staticText1.SetFont( wx.Font( 18, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Comic Sans MS" ) )
		self.m_staticText1.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		nama_grid.Add( self.m_staticText1, 1, wx.EXPAND|wx.ALL, 5 )


		self.nama_panel.SetSizer( nama_grid )
		self.nama_panel.Layout()
		nama_grid.Fit( self.nama_panel )
		wxBoxSizer.Add( self.nama_panel, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.Nim_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.Nim_panel.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		self.Nim_panel.SetMinSize( wx.Size( 800,-1 ) )

		nim_grid = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText2 = wx.StaticText( self.Nim_panel, wx.ID_ANY, u"192410101078", wx.Point( 100,100 ), wx.Size( -1,-1 ), wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText2.Wrap( -1 )

		self.m_staticText2.SetFont( wx.Font( 18, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Comic Sans MS" ) )

		nim_grid.Add( self.m_staticText2, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		self.Nim_panel.SetSizer( nim_grid )
		self.Nim_panel.Layout()
		nim_grid.Fit( self.Nim_panel )
		wxBoxSizer.Add( self.Nim_panel, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.Hello = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.Hello.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		self.Hello.SetMinSize( wx.Size( 800,-1 ) )

		hello_grid = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText3 = wx.StaticText( self.Hello, wx.ID_ANY, u"HELLO WX ^,^ !!!", wx.Point( 100,100 ), wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText3.Wrap( -1 )

		self.m_staticText3.SetFont( wx.Font( 36, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Comic Sans MS" ) )

		hello_grid.Add( self.m_staticText3, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		self.Hello.SetSizer( hello_grid )
		self.Hello.Layout()
		hello_grid.Fit( self.Hello )
		wxBoxSizer.Add( self.Hello, 0, wx.ALIGN_CENTER|wx.ALL, 0 )

		self.m_panel8 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		self.m_bitmap2 = wx.StaticBitmap( self.m_panel8, wx.ID_ANY, wx.Bitmap( u"../Pictures/pandasss.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.m_bitmap2, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		self.m_panel8.SetSizer( bSizer5 )
		self.m_panel8.Layout()
		bSizer5.Fit( self.m_panel8 )
		wxBoxSizer.Add( self.m_panel8, 1, wx.EXPAND |wx.ALL, 0 )


		self.SetSizer( wxBoxSizer )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.MyFrame1OnClose )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def MyFrame1OnClose( self, event ):
		event.Skip()


