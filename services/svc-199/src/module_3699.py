"""Service module 3699: business logic, no crypto."""


def calculate_total_3699(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3699():
    return 'module 3699 handles orders and invoices'
