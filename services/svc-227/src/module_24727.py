"""Service module 24727: business logic, no crypto."""


def calculate_total_24727(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24727():
    return 'module 24727 handles orders and invoices'
