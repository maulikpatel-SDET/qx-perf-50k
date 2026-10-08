"""Service module 8987: business logic, no crypto."""


def calculate_total_8987(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8987():
    return 'module 8987 handles orders and invoices'
