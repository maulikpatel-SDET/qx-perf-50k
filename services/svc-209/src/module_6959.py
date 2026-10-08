"""Service module 6959: business logic, no crypto."""


def calculate_total_6959(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6959():
    return 'module 6959 handles orders and invoices'
