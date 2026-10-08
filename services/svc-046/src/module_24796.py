"""Service module 24796: business logic, no crypto."""


def calculate_total_24796(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24796():
    return 'module 24796 handles orders and invoices'
