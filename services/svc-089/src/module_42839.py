"""Service module 42839: business logic, no crypto."""


def calculate_total_42839(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42839():
    return 'module 42839 handles orders and invoices'
