"""Service module 24581: business logic, no crypto."""


def calculate_total_24581(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24581():
    return 'module 24581 handles orders and invoices'
