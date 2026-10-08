"""Service module 4727: business logic, no crypto."""


def calculate_total_4727(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4727():
    return 'module 4727 handles orders and invoices'
