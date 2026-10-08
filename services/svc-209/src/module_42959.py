"""Service module 42959: business logic, no crypto."""


def calculate_total_42959(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42959():
    return 'module 42959 handles orders and invoices'
