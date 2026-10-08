"""Service module 38131: business logic, no crypto."""


def calculate_total_38131(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38131():
    return 'module 38131 handles orders and invoices'
