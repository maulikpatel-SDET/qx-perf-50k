"""Service module 30801: business logic, no crypto."""


def calculate_total_30801(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30801():
    return 'module 30801 handles orders and invoices'
