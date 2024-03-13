import win32print

def print_to_printer(printer_name, content):
    # Open a printer
    printer_handle = win32print.OpenPrinter(printer_name)

    # Start a print job
    job_info = win32print.StartDocPrinter(printer_handle, 1, ("Print Job", None, "RAW"))
    win32print.StartPagePrinter(printer_handle)

    # Send content to the printer
    win32print.WritePrinter(printer_handle, content.encode('utf-8'))

    # End the print job
    win32print.EndPagePrinter(printer_handle)
    win32print.EndDocPrinter(printer_handle)
    win32print.ClosePrinter(printer_handle)

# Example content
printer_content = "Hello, this is content sent to the printer!"

# Specify the printer name (you can get it from Control Panel > Devices and Printers)
printer_name = "Your_Printer_Name"

# Print to the specified printer
print_to_printer(printer_name, printer_content)
