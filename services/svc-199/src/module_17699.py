"""Service module 17699: business logic, no crypto."""


def calculate_total_17699(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17699():
    return 'module 17699 handles orders and invoices'
