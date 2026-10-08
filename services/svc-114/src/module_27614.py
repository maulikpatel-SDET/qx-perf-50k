"""Service module 27614: business logic, no crypto."""


def calculate_total_27614(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27614():
    return 'module 27614 handles orders and invoices'
