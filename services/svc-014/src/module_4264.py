"""Service module 4264: business logic, no crypto."""


def calculate_total_4264(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4264():
    return 'module 4264 handles orders and invoices'
