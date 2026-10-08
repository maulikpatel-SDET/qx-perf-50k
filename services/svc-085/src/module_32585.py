"""Service module 32585: business logic, no crypto."""


def calculate_total_32585(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32585():
    return 'module 32585 handles orders and invoices'
