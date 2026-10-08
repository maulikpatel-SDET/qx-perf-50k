"""Service module 24315: business logic, no crypto."""


def calculate_total_24315(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24315():
    return 'module 24315 handles orders and invoices'
