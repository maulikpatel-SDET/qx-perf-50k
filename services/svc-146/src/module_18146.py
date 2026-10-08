"""Service module 18146: business logic, no crypto."""


def calculate_total_18146(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18146():
    return 'module 18146 handles orders and invoices'
