"""Service module 37924: business logic, no crypto."""


def calculate_total_37924(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37924():
    return 'module 37924 handles orders and invoices'
