"""Service module 11987: business logic, no crypto."""


def calculate_total_11987(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11987():
    return 'module 11987 handles orders and invoices'
