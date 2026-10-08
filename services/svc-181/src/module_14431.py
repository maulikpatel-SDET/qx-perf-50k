"""Service module 14431: business logic, no crypto."""


def calculate_total_14431(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14431():
    return 'module 14431 handles orders and invoices'
