"""Service module 47817: business logic, no crypto."""


def calculate_total_47817(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47817():
    return 'module 47817 handles orders and invoices'
