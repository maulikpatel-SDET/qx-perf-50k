"""Service module 44964: business logic, no crypto."""


def calculate_total_44964(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44964():
    return 'module 44964 handles orders and invoices'
