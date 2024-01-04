import pyperclip
import AppKit

pb = AppKit.NSPasteboard.generalPasteboard()
pbtypes = pb.types()
pbdata = pb.dataForType_('public.utf8-plain-text')
print(pbdata.decode('utf-8'))
pyperclip.copy(pbdata.decode('utf-8'))
