"""Service module 6817: business logic, no crypto."""


def calculate_total_6817(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6817():
    return 'module 6817 handles orders and invoices'
