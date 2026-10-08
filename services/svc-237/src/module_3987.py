"""Service module 3987: business logic, no crypto."""


def calculate_total_3987(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3987():
    return 'module 3987 handles orders and invoices'
