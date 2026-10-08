"""Service module 36213: business logic, no crypto."""


def calculate_total_36213(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36213():
    return 'module 36213 handles orders and invoices'
