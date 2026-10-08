"""Service module 587: business logic, no crypto."""


def calculate_total_587(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_587():
    return 'module 587 handles orders and invoices'
