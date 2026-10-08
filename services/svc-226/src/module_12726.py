"""Service module 12726: business logic, no crypto."""


def calculate_total_12726(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12726():
    return 'module 12726 handles orders and invoices'
