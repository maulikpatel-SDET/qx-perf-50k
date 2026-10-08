"""Service module 20825: business logic, no crypto."""


def calculate_total_20825(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20825():
    return 'module 20825 handles orders and invoices'
