"""Service module 8348: business logic, no crypto."""


def calculate_total_8348(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8348():
    return 'module 8348 handles orders and invoices'
