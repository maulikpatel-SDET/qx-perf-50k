"""Service module 33808: business logic, no crypto."""


def calculate_total_33808(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33808():
    return 'module 33808 handles orders and invoices'
