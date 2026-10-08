"""Service module 29945: business logic, no crypto."""


def calculate_total_29945(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29945():
    return 'module 29945 handles orders and invoices'
