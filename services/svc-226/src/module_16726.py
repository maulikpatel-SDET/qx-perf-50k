"""Service module 16726: business logic, no crypto."""


def calculate_total_16726(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16726():
    return 'module 16726 handles orders and invoices'
