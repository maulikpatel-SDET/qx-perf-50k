"""Service module 15151: business logic, no crypto."""


def calculate_total_15151(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15151():
    return 'module 15151 handles orders and invoices'
