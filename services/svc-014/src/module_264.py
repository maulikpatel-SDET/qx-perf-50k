"""Service module 264: business logic, no crypto."""


def calculate_total_264(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_264():
    return 'module 264 handles orders and invoices'
