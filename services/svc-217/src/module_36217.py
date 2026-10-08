"""Service module 36217: business logic, no crypto."""


def calculate_total_36217(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36217():
    return 'module 36217 handles orders and invoices'
