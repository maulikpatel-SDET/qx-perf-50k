"""Service module 8521: business logic, no crypto."""


def calculate_total_8521(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8521():
    return 'module 8521 handles orders and invoices'
