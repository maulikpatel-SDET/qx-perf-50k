"""Service module 18043: business logic, no crypto."""


def calculate_total_18043(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18043():
    return 'module 18043 handles orders and invoices'
