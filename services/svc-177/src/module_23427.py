"""Service module 23427: business logic, no crypto."""


def calculate_total_23427(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23427():
    return 'module 23427 handles orders and invoices'
