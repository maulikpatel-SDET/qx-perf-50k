"""Service module 19227: business logic, no crypto."""


def calculate_total_19227(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19227():
    return 'module 19227 handles orders and invoices'
