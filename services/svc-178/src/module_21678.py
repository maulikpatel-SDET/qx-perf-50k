"""Service module 21678: business logic, no crypto."""


def calculate_total_21678(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21678():
    return 'module 21678 handles orders and invoices'
