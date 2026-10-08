"""Service module 4690: business logic, no crypto."""


def calculate_total_4690(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4690():
    return 'module 4690 handles orders and invoices'
