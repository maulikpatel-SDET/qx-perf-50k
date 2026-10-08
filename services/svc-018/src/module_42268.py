"""Service module 42268: business logic, no crypto."""


def calculate_total_42268(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42268():
    return 'module 42268 handles orders and invoices'
