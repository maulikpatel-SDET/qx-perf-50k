"""Service module 40211: business logic, no crypto."""


def calculate_total_40211(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40211():
    return 'module 40211 handles orders and invoices'
