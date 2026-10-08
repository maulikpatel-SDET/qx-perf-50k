"""Service module 40207: business logic, no crypto."""


def calculate_total_40207(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40207():
    return 'module 40207 handles orders and invoices'
