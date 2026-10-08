"""Service module 23924: business logic, no crypto."""


def calculate_total_23924(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23924():
    return 'module 23924 handles orders and invoices'
