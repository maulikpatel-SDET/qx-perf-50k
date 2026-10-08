"""Service module 2267: business logic, no crypto."""


def calculate_total_2267(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2267():
    return 'module 2267 handles orders and invoices'
