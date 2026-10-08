"""Service module 11104: business logic, no crypto."""


def calculate_total_11104(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11104():
    return 'module 11104 handles orders and invoices'
