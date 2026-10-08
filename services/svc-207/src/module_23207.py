"""Service module 23207: business logic, no crypto."""


def calculate_total_23207(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23207():
    return 'module 23207 handles orders and invoices'
