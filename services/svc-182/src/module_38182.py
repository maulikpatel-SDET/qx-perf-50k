"""Service module 38182: business logic, no crypto."""


def calculate_total_38182(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38182():
    return 'module 38182 handles orders and invoices'
