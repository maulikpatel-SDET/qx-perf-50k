"""Service module 45581: business logic, no crypto."""


def calculate_total_45581(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45581():
    return 'module 45581 handles orders and invoices'
