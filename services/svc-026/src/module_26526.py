"""Service module 26526: business logic, no crypto."""


def calculate_total_26526(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26526():
    return 'module 26526 handles orders and invoices'
