"""Service module 40315: business logic, no crypto."""


def calculate_total_40315(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40315():
    return 'module 40315 handles orders and invoices'
