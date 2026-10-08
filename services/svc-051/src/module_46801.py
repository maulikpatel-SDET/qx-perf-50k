"""Service module 46801: business logic, no crypto."""


def calculate_total_46801(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46801():
    return 'module 46801 handles orders and invoices'
