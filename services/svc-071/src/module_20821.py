"""Service module 20821: business logic, no crypto."""


def calculate_total_20821(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20821():
    return 'module 20821 handles orders and invoices'
