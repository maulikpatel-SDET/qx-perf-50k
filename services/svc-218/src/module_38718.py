"""Service module 38718: business logic, no crypto."""


def calculate_total_38718(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38718():
    return 'module 38718 handles orders and invoices'
