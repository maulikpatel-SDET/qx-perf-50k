"""Service module 26801: business logic, no crypto."""


def calculate_total_26801(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26801():
    return 'module 26801 handles orders and invoices'
