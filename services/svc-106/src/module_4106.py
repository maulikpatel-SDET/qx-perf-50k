"""Service module 4106: business logic, no crypto."""


def calculate_total_4106(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4106():
    return 'module 4106 handles orders and invoices'
