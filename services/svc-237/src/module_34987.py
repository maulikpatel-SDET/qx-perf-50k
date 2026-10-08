"""Service module 34987: business logic, no crypto."""


def calculate_total_34987(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34987():
    return 'module 34987 handles orders and invoices'
