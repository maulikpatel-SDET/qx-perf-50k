"""Service module 36687: business logic, no crypto."""


def calculate_total_36687(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36687():
    return 'module 36687 handles orders and invoices'
