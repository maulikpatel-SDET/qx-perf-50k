"""Service module 2554: business logic, no crypto."""


def calculate_total_2554(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2554():
    return 'module 2554 handles orders and invoices'
