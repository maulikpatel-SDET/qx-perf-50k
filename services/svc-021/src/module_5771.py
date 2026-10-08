"""Service module 5771: business logic, no crypto."""


def calculate_total_5771(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5771():
    return 'module 5771 handles orders and invoices'
