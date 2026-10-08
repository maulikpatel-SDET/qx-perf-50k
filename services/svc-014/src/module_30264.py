"""Service module 30264: business logic, no crypto."""


def calculate_total_30264(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30264():
    return 'module 30264 handles orders and invoices'
