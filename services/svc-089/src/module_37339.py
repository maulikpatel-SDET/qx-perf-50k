"""Service module 37339: business logic, no crypto."""


def calculate_total_37339(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37339():
    return 'module 37339 handles orders and invoices'
