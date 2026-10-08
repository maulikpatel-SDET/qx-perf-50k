"""Service module 12202: business logic, no crypto."""


def calculate_total_12202(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12202():
    return 'module 12202 handles orders and invoices'
