"""Service module 8972: business logic, no crypto."""


def calculate_total_8972(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8972():
    return 'module 8972 handles orders and invoices'
