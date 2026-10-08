"""Service module 41227: business logic, no crypto."""


def calculate_total_41227(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41227():
    return 'module 41227 handles orders and invoices'
