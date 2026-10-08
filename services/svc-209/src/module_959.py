"""Service module 959: business logic, no crypto."""


def calculate_total_959(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_959():
    return 'module 959 handles orders and invoices'
