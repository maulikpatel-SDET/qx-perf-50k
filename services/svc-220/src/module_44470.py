"""Service module 44470: business logic, no crypto."""


def calculate_total_44470(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44470():
    return 'module 44470 handles orders and invoices'
