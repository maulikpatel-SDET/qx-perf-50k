"""Service module 42227: business logic, no crypto."""


def calculate_total_42227(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42227():
    return 'module 42227 handles orders and invoices'
