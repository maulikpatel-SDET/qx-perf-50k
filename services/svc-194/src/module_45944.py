"""Service module 45944: business logic, no crypto."""


def calculate_total_45944(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45944():
    return 'module 45944 handles orders and invoices'
