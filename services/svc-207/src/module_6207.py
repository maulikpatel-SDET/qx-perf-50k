"""Service module 6207: business logic, no crypto."""


def calculate_total_6207(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6207():
    return 'module 6207 handles orders and invoices'
