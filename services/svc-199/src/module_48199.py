"""Service module 48199: business logic, no crypto."""


def calculate_total_48199(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48199():
    return 'module 48199 handles orders and invoices'
