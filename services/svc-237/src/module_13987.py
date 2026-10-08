"""Service module 13987: business logic, no crypto."""


def calculate_total_13987(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13987():
    return 'module 13987 handles orders and invoices'
