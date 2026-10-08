"""Service module 45211: business logic, no crypto."""


def calculate_total_45211(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45211():
    return 'module 45211 handles orders and invoices'
