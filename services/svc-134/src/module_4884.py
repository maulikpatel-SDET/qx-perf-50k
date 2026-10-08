"""Service module 4884: business logic, no crypto."""


def calculate_total_4884(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4884():
    return 'module 4884 handles orders and invoices'
