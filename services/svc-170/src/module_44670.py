"""Service module 44670: business logic, no crypto."""


def calculate_total_44670(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44670():
    return 'module 44670 handles orders and invoices'
