"""Service module 8106: business logic, no crypto."""


def calculate_total_8106(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8106():
    return 'module 8106 handles orders and invoices'
