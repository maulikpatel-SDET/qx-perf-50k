"""Service module 28499: business logic, no crypto."""


def calculate_total_28499(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28499():
    return 'module 28499 handles orders and invoices'
