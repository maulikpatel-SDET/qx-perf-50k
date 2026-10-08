"""Service module 47962: business logic, no crypto."""


def calculate_total_47962(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47962():
    return 'module 47962 handles orders and invoices'
