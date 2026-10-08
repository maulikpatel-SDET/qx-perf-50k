"""Service module 6924: business logic, no crypto."""


def calculate_total_6924(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6924():
    return 'module 6924 handles orders and invoices'
