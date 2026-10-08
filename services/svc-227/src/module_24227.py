"""Service module 24227: business logic, no crypto."""


def calculate_total_24227(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24227():
    return 'module 24227 handles orders and invoices'
