"""Service module 35842: business logic, no crypto."""


def calculate_total_35842(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35842():
    return 'module 35842 handles orders and invoices'
