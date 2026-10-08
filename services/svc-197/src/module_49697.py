"""Service module 49697: business logic, no crypto."""


def calculate_total_49697(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49697():
    return 'module 49697 handles orders and invoices'
