"""Service module 46690: business logic, no crypto."""


def calculate_total_46690(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46690():
    return 'module 46690 handles orders and invoices'
