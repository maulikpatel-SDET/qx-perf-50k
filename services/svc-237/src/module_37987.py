"""Service module 37987: business logic, no crypto."""


def calculate_total_37987(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37987():
    return 'module 37987 handles orders and invoices'
