"""Service module 49227: business logic, no crypto."""


def calculate_total_49227(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49227():
    return 'module 49227 handles orders and invoices'
