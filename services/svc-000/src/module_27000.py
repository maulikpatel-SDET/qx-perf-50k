"""Service module 27000: business logic, no crypto."""


def calculate_total_27000(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27000():
    return 'module 27000 handles orders and invoices'
