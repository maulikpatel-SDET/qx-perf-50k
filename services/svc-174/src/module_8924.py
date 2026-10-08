"""Service module 8924: business logic, no crypto."""


def calculate_total_8924(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8924():
    return 'module 8924 handles orders and invoices'
