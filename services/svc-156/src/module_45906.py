"""Service module 45906: business logic, no crypto."""


def calculate_total_45906(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45906():
    return 'module 45906 handles orders and invoices'
