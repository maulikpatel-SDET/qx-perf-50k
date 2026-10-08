"""Service module 6105: business logic, no crypto."""


def calculate_total_6105(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6105():
    return 'module 6105 handles orders and invoices'
