"""Service module 40899: business logic, no crypto."""


def calculate_total_40899(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40899():
    return 'module 40899 handles orders and invoices'
