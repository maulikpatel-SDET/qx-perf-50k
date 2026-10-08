"""Service module 27348: business logic, no crypto."""


def calculate_total_27348(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27348():
    return 'module 27348 handles orders and invoices'
