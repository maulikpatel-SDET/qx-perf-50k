"""Service module 36987: business logic, no crypto."""


def calculate_total_36987(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36987():
    return 'module 36987 handles orders and invoices'
