"""Service module 21516: business logic, no crypto."""


def calculate_total_21516(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21516():
    return 'module 21516 handles orders and invoices'
