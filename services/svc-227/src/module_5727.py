"""Service module 5727: business logic, no crypto."""


def calculate_total_5727(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5727():
    return 'module 5727 handles orders and invoices'
