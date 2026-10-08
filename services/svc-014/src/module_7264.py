"""Service module 7264: business logic, no crypto."""


def calculate_total_7264(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7264():
    return 'module 7264 handles orders and invoices'
