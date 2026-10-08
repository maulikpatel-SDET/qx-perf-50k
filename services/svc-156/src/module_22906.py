"""Service module 22906: business logic, no crypto."""


def calculate_total_22906(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22906():
    return 'module 22906 handles orders and invoices'
