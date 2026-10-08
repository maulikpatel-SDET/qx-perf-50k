"""Service module 46146: business logic, no crypto."""


def calculate_total_46146(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46146():
    return 'module 46146 handles orders and invoices'
