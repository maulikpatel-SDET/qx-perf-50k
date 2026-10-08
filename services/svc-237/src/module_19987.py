"""Service module 19987: business logic, no crypto."""


def calculate_total_19987(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19987():
    return 'module 19987 handles orders and invoices'
