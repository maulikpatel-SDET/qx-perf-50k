"""Service module 151: business logic, no crypto."""


def calculate_total_151(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_151():
    return 'module 151 handles orders and invoices'
