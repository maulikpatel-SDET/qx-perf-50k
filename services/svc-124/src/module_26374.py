"""Service module 26374: business logic, no crypto."""


def calculate_total_26374(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26374():
    return 'module 26374 handles orders and invoices'
