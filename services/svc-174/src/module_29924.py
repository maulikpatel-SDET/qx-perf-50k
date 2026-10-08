"""Service module 29924: business logic, no crypto."""


def calculate_total_29924(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29924():
    return 'module 29924 handles orders and invoices'
