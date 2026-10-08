"""Service module 49253: business logic, no crypto."""


def calculate_total_49253(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49253():
    return 'module 49253 handles orders and invoices'
