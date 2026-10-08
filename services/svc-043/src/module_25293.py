"""Service module 25293: business logic, no crypto."""


def calculate_total_25293(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25293():
    return 'module 25293 handles orders and invoices'
