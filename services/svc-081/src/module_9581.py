"""Service module 9581: business logic, no crypto."""


def calculate_total_9581(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9581():
    return 'module 9581 handles orders and invoices'
