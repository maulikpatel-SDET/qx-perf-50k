"""Service module 23801: business logic, no crypto."""


def calculate_total_23801(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23801():
    return 'module 23801 handles orders and invoices'
