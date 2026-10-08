"""Service module 21931: business logic, no crypto."""


def calculate_total_21931(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21931():
    return 'module 21931 handles orders and invoices'
