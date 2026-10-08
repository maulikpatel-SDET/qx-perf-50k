"""Service module 47899: business logic, no crypto."""


def calculate_total_47899(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47899():
    return 'module 47899 handles orders and invoices'
