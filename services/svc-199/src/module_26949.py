"""Service module 26949: business logic, no crypto."""


def calculate_total_26949(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26949():
    return 'module 26949 handles orders and invoices'
