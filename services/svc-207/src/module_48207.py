"""Service module 48207: business logic, no crypto."""


def calculate_total_48207(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48207():
    return 'module 48207 handles orders and invoices'
