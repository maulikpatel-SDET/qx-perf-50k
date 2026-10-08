"""Service module 11217: business logic, no crypto."""


def calculate_total_11217(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11217():
    return 'module 11217 handles orders and invoices'
