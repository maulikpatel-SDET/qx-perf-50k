"""Service module 93: business logic, no crypto."""


def calculate_total_93(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_93():
    return 'module 93 handles orders and invoices'
