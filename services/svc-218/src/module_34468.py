"""Service module 34468: business logic, no crypto."""


def calculate_total_34468(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34468():
    return 'module 34468 handles orders and invoices'
