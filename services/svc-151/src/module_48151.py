"""Service module 48151: business logic, no crypto."""


def calculate_total_48151(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48151():
    return 'module 48151 handles orders and invoices'
