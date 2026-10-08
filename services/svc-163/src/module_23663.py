"""Service module 23663: business logic, no crypto."""


def calculate_total_23663(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23663():
    return 'module 23663 handles orders and invoices'
