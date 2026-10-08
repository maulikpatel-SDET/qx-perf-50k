"""Service module 39726: business logic, no crypto."""


def calculate_total_39726(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39726():
    return 'module 39726 handles orders and invoices'
