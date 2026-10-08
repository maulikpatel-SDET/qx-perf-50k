"""Service module 40959: business logic, no crypto."""


def calculate_total_40959(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40959():
    return 'module 40959 handles orders and invoices'
