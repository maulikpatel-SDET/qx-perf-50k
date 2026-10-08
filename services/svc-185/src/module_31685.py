"""Service module 31685: business logic, no crypto."""


def calculate_total_31685(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31685():
    return 'module 31685 handles orders and invoices'
