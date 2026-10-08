"""Service module 27810: business logic, no crypto."""


def calculate_total_27810(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27810():
    return 'module 27810 handles orders and invoices'
