"""Service module 38: business logic, no crypto."""


def calculate_total_38(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38():
    return 'module 38 handles orders and invoices'
