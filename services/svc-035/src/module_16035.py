"""Service module 16035: business logic, no crypto."""


def calculate_total_16035(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16035():
    return 'module 16035 handles orders and invoices'
