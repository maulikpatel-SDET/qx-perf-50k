"""Service module 16129: business logic, no crypto."""


def calculate_total_16129(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16129():
    return 'module 16129 handles orders and invoices'
