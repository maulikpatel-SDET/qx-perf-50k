"""Service module 49035: business logic, no crypto."""


def calculate_total_49035(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49035():
    return 'module 49035 handles orders and invoices'
