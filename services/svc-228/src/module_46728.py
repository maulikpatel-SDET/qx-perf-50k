"""Service module 46728: business logic, no crypto."""


def calculate_total_46728(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46728():
    return 'module 46728 handles orders and invoices'
