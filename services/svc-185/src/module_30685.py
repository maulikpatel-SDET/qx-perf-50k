"""Service module 30685: business logic, no crypto."""


def calculate_total_30685(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30685():
    return 'module 30685 handles orders and invoices'
