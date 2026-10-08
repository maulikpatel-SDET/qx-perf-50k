"""Service module 18315: business logic, no crypto."""


def calculate_total_18315(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18315():
    return 'module 18315 handles orders and invoices'
