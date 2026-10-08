"""Service module 38265: business logic, no crypto."""


def calculate_total_38265(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38265():
    return 'module 38265 handles orders and invoices'
