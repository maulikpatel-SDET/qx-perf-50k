"""Service module 27689: business logic, no crypto."""


def calculate_total_27689(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27689():
    return 'module 27689 handles orders and invoices'
