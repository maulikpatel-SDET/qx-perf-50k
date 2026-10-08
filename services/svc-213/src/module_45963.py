"""Service module 45963: business logic, no crypto."""


def calculate_total_45963(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45963():
    return 'module 45963 handles orders and invoices'
