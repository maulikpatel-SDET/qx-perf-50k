"""Service module 29076: business logic, no crypto."""


def calculate_total_29076(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29076():
    return 'module 29076 handles orders and invoices'
