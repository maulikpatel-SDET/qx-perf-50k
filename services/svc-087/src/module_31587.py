"""Service module 31587: business logic, no crypto."""


def calculate_total_31587(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31587():
    return 'module 31587 handles orders and invoices'
