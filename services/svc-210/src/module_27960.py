"""Service module 27960: business logic, no crypto."""


def calculate_total_27960(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27960():
    return 'module 27960 handles orders and invoices'
