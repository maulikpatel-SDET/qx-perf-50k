"""Service module 15687: business logic, no crypto."""


def calculate_total_15687(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15687():
    return 'module 15687 handles orders and invoices'
