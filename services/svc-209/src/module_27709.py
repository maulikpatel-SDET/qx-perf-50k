"""Service module 27709: business logic, no crypto."""


def calculate_total_27709(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27709():
    return 'module 27709 handles orders and invoices'
