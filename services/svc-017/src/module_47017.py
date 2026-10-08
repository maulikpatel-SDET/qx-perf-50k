"""Service module 47017: business logic, no crypto."""


def calculate_total_47017(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47017():
    return 'module 47017 handles orders and invoices'
