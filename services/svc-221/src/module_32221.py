"""Service module 32221: business logic, no crypto."""


def calculate_total_32221(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32221():
    return 'module 32221 handles orders and invoices'
