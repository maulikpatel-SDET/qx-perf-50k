"""Service module 3001: business logic, no crypto."""


def calculate_total_3001(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3001():
    return 'module 3001 handles orders and invoices'
