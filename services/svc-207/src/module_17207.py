"""Service module 17207: business logic, no crypto."""


def calculate_total_17207(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17207():
    return 'module 17207 handles orders and invoices'
