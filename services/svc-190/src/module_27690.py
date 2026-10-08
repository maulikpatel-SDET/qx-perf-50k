"""Service module 27690: business logic, no crypto."""


def calculate_total_27690(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27690():
    return 'module 27690 handles orders and invoices'
