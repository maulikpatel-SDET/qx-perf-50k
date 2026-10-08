"""Service module 17678: business logic, no crypto."""


def calculate_total_17678(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17678():
    return 'module 17678 handles orders and invoices'
