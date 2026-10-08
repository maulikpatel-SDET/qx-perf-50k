"""Service module 37921: business logic, no crypto."""


def calculate_total_37921(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37921():
    return 'module 37921 handles orders and invoices'
