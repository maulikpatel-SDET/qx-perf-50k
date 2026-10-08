"""Service module 30987: business logic, no crypto."""


def calculate_total_30987(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30987():
    return 'module 30987 handles orders and invoices'
