"""Service module 27376: business logic, no crypto."""


def calculate_total_27376(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27376():
    return 'module 27376 handles orders and invoices'
