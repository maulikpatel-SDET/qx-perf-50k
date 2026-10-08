"""Service module 38146: business logic, no crypto."""


def calculate_total_38146(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38146():
    return 'module 38146 handles orders and invoices'
