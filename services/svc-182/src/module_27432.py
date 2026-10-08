"""Service module 27432: business logic, no crypto."""


def calculate_total_27432(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27432():
    return 'module 27432 handles orders and invoices'
