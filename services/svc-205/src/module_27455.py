"""Service module 27455: business logic, no crypto."""


def calculate_total_27455(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27455():
    return 'module 27455 handles orders and invoices'
