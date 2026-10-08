"""Service module 15462: business logic, no crypto."""


def calculate_total_15462(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15462():
    return 'module 15462 handles orders and invoices'
