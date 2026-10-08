"""Service module 20264: business logic, no crypto."""


def calculate_total_20264(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20264():
    return 'module 20264 handles orders and invoices'
