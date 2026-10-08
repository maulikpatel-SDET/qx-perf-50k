"""Service module 5581: business logic, no crypto."""


def calculate_total_5581(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5581():
    return 'module 5581 handles orders and invoices'
