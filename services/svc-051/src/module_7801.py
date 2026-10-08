"""Service module 7801: business logic, no crypto."""


def calculate_total_7801(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7801():
    return 'module 7801 handles orders and invoices'
