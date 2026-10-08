"""Service module 26817: business logic, no crypto."""


def calculate_total_26817(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26817():
    return 'module 26817 handles orders and invoices'
