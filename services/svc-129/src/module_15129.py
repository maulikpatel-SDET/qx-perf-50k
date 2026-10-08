"""Service module 15129: business logic, no crypto."""


def calculate_total_15129(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15129():
    return 'module 15129 handles orders and invoices'
