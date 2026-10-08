"""Service module 37378: business logic, no crypto."""


def calculate_total_37378(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37378():
    return 'module 37378 handles orders and invoices'
