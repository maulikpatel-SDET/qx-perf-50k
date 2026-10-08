"""Service module 27220: business logic, no crypto."""


def calculate_total_27220(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27220():
    return 'module 27220 handles orders and invoices'
