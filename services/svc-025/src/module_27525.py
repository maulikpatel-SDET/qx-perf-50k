"""Service module 27525: business logic, no crypto."""


def calculate_total_27525(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27525():
    return 'module 27525 handles orders and invoices'
