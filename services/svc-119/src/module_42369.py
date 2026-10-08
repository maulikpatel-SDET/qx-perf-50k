"""Service module 42369: business logic, no crypto."""


def calculate_total_42369(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42369():
    return 'module 42369 handles orders and invoices'
