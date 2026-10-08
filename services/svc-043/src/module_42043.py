"""Service module 42043: business logic, no crypto."""


def calculate_total_42043(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42043():
    return 'module 42043 handles orders and invoices'
