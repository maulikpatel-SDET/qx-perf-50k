"""Service module 14726: business logic, no crypto."""


def calculate_total_14726(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14726():
    return 'module 14726 handles orders and invoices'
