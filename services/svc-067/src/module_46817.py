"""Service module 46817: business logic, no crypto."""


def calculate_total_46817(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46817():
    return 'module 46817 handles orders and invoices'
