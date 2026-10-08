"""Service module 43184: business logic, no crypto."""


def calculate_total_43184(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43184():
    return 'module 43184 handles orders and invoices'
