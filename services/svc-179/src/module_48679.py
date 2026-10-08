"""Service module 48679: business logic, no crypto."""


def calculate_total_48679(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48679():
    return 'module 48679 handles orders and invoices'
