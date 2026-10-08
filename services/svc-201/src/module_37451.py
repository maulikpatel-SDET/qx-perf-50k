"""Service module 37451: business logic, no crypto."""


def calculate_total_37451(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37451():
    return 'module 37451 handles orders and invoices'
