"""Service module 4643: business logic, no crypto."""


def calculate_total_4643(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4643():
    return 'module 4643 handles orders and invoices'
