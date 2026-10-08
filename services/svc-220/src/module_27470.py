"""Service module 27470: business logic, no crypto."""


def calculate_total_27470(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27470():
    return 'module 27470 handles orders and invoices'
