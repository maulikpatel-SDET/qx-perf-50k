"""Service module 33607: business logic, no crypto."""


def calculate_total_33607(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33607():
    return 'module 33607 handles orders and invoices'
