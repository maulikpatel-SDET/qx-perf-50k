"""Service module 48159: business logic, no crypto."""


def calculate_total_48159(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48159():
    return 'module 48159 handles orders and invoices'
