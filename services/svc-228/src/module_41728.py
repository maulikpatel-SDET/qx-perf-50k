"""Service module 41728: business logic, no crypto."""


def calculate_total_41728(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41728():
    return 'module 41728 handles orders and invoices'
